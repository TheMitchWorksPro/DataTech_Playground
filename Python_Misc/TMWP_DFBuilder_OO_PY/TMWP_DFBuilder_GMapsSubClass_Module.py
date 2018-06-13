
# coding: utf-8

# general libraries
import pandas as pd

## required for Google Maps API code
import os

## for larger data and/or make many requests in one day - get Google API key and use these lines:
# os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_Key"
## for better security (PROD environments) - install key to server and use just this line to load it:
# os.environ.get('GOOGLE_API_KEY')

# set up geocode
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut
import time
from time import localtime, strftime
from abc import ABCMeta, abstractmethod
import pandas as pd

def getNow():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

class DFBuilder(object, metaclass=ABCMeta):       # sets up abstract class
    '''DataFrame Builder abstract class.  Sets up logic to be inherited by objects that need to loop over a DataFrame
and cache the results.  Original use case involves making API calls to the web which can get interrupted by 
errors and server timeouts.  This object stores all the logic to build up and save a DataFrame a small number of 
records at a time.  Then a subclass can define an abstract method in the base class as to what we want to do to 
the input data.  Original use case added in content extracted form the web to a new column.  But subclasses can 
be built to do more. Initialization argumens: endRw, time_delay. endRw = number of records to cache at a time
when building outDF.  time_delay is number of seconds delay between each cycle of the loop that builds outDF.'''
    def __init__(self,endRw,time_delay):          # abstract classes can be subclassed
        self.endRow=endRw                         # but cannot be instantiated
        self.delay=time_delay
        self.tmpDF=pd.DataFrame()   # temp DF will be endRow rows in length
        self.outDF=pd.DataFrame()   # final DF build in sets of endRow rows so all is not lost in a failure
        self.lastIndex = None
        self.statusMsgGrouping = 100
        
    def __str__(self):
        return ("Global Settings for this object: \n" +  
                "endRow: " + str(self.endRow) + "\n" + 
                "delay:  " + str(self.delay) + "\n" + 
                "statusMsgGrouping: " + str(self.statusMsgGrouping) + "\n"
                "Length of outDF: " + str(len(self.outDF)) + "\n" +
                "nextIndex: " + str(self.lastIndex))       
                 # if continuing build process with last added table - index of next rec.
        
    @abstractmethod                               # abstract method definition in Python
    def _modifyTempDF_(): pass                    # This method will operate on TempDF inside the loop
    
    def set_statusMsgGrouping(self, newValue):
        '''Change number of records used to determine when to provide output messages during buildOutDF().
Default is 100 records.  newValue=x sets this to a new number. Note that If endRow is not a factor of 
statusMsgGrouping output may appear at unexpected intervals. endRow sets the number of rows to cache to
outDF in each iteration of the build loop.'''
        
        self.statusMsgGrouping = newValue
        print(self)
        
    def set_timeDelay(self, newValue):
        '''Change number of seconds in time delay between requests while creating outDF().
Default is 1 second.  newValue=x sets this to a new number.'''
        self.delay = newValue
        print(self)
        
    def set_endRow_OutDf_caching(self, newValue):
        '''Change value of endRow which controls how many rows to cache at a time within buildOutDF().
Default is 5.  If something goes wrong and you have to restart the process, this value also represents
the maximum number of requests you will lose.  The rest will have already been added to outDF.
newValue=x sets this to a new number.'''
        self.endRow = newValue
        print(self)
    
    def buildOutDF(self, inputDF):
        '''Scans inputDF using self.endRow rows (default of 5) at a time to do it.  It then calls in logic
from _modifyTempDF()_ to make changes to each subset of rows and appends tiny tempDF onto an outDF.  When the 
subclass is using a web API, self.delay tells it how much time to delay each iteration of the loop. Should
this function fail in the middle, outDF will have all work up to the failure.  
This can be saved out to a DF or csv.  The function can be run again on a subset of the data 
(the records not encountered yet before the failure).'''
    
        lenDF = len(inputDF)
        print("Timestamp: ", getNow())
        print("Processing inputDF with length of: ", lenDF)
        print("Please wait ...")
        endIndx = 0

        i = 0
        while i < lenDF:
            # print("i: ", i)
            endIndx = i + self.endRow
            if endIndx > lenDF:
                        endIndx = lenDF

            # print("Range to use: ", i, ":", endIndx)
            if i % self.statusMsgGrouping == 0:
                print(getNow(), "Now processing index: ", i)

            self.tmpDF = inputDF[i:endIndx].copy(deep=True)
            self._modifyTempDF_()
            time.sleep(self.delay)
            self.outDF = self.outDF.append(self.tmpDF) 
            self.lastIndex = endIndx 
            i = endIndx
            # print("i at end of loop: ", i)        
          
        self.reindex_OutDF()
        print("Process complete. %d records added to outDF." %(self.lastIndex))
        print("Timestamp: ", getNow())
        
    def reindex_OutDF(self):
        '''Reindex OutDF using same settings that are used internally for the index during its creation.
This is like doing: outDF.reset_index(drop=True, inplace=True).'''
        self.outDF.reset_index(drop=True, inplace=True)


class GMapsLoc_DFBuilder(DFBuilder): 
    '''This class inherits DFBuilder.buildOutDF() which makes use of data extraction and nodification functions in
this subclass.  endRw sets number of rows to process at a time while building outDF (default=5). time_delay 
can set the time delay between loop iterations to help prevent licensing issues and related server timeouts.
Default is 1 second. Initialization arguments: endRw, time_delay, return_null.
 * endRw controls grouping: process endRow rows at a time and add to outDF (default is 5).
 * time_delay has default of 1 second and sets how much time to wait each request whild building outDF.
 * return_null, if False, records error text formatted as "_<errTxt>_" for records that failed to process.
   Set to True to have it return blank records when errors occur instead (default is False).'''
    def __init__(self, endRw=5,time_delay=1, return_null=False):           
        super().__init__(endRw,time_delay)
        self.rtn_null = return_null
        self.timeout = 10
        self.location = ""  # stores last location accessed using getGeoAddr
        
    def __str__(self):
        outStr = (super().__str__() + "\n" +
                  "rtn_null: " + str(self.rtn_null) + "\n" +
                  "timeout: "  + str(self.timeout) + "\n")
        if isinstance(self.location, (type(None), str)):
            outStr = outStr + "location (last obtained): " + str(self.location)
        else:
            outStr = outStr + "location (last obtained): " + str(self.location.raw)
            
        return outStr

    def set_ServerTimeout(self, newValue):
        '''Change number of seconds for the server timeout setting used during web requests.
Default is 10 second.  newValue=x sets this to a new number.'''
        self.timeout = newValue
        print(self)    
    
    def testConnection(self, lat=48.8588443, lon=2.2943506):
        '''Test getGeoAddr() function to prove connection to Google Maps is working.  Use this ahead of
performing much larger operations with Google Maps.'''
        return self.getGeoAddr(lat, lon)
        
    def getGeoAddr(self, lt, lng, timeout=10, test=False, rtn_null=False):
        '''Make call to Google Maps API to return back just the address from the json location record.  Errors
should result in text values to help identify why an address was not returned.  This can be turned off and 
records that failed can bring back just an empty field by setting rtn_null to True. timeout = server timeout 
and has a default that worked well during testing.  '''
        
        try:
            self.location = geolocator.reverse(str(lt) + ", " + str(lng), timeout=timeout)
            if test == True:
                print("===============================")
                print("Address:\n")
                print(self.location)
                print("===============================")
                rtnVal = self.location
            else:
                rtnVal = self.location.address
        except GeocoderTimedOut as gEoTo:
            print(type(gEoTo))
            print(gEoTo)
            self.location = None
            rtnVal = "_" + str(eee).upper().replace(' ', '_').replace(':', '') + "_"
            ## old error text: "_TIME_OUT_ERROR_ENCOUNTERED_"
        except Exception as eee:
            print(type(eee))
            print(eee)  
            self.location = None
            rtnVal = "_" + str(eee).upper().replace(' ', '_').replace(':', '') + "_"
        finally:
            # time_delay is not included here and should be incorporated into
            # the loop that calls this function if desirable

            if rtn_null==True and self.location is None:
                return ""
            else:
                return rtnVal
        
    def _modifyTempDF_(self, test=False):
        '''Add Address Field to tempDF based on lat, lon (latitude/longitude field values in inputDF)'''
        self.tmpDF["Address"] = self.tmpDF.apply(lambda x: self.getGeoAddr(lt=x.lat,lng=x.lon, 
                                     timeout=self.timeout,test=False, rtn_null=self.rtn_null), axis=1)


