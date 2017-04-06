#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Draft Version ... presented to illustrate how the problem shifts and how later solutions address this
#   * In this version, several solutions from Stack Overflow are added into the code.
#   * the result is that one encode error is solved but another one shifts to a decode error
#   * one suggested solution for decode is used and though it worked for others, it fails here

import requests
import datetime
import re

class event(object):
    def __init__(self, title, time, location):
        self.title = title
        self.time = time
        self.location = location
    
    def day(self):
        try:
            day = re.findall('\w+', self.time)[:3]
            day = ' '.join(day)
            try: 
                return datetime.datetime.strptime(day, "%d %b %Y")
            except ValueError:
                return datetime.datetime.strptime(day, "%d %B %Y")
        except ValueError:
            return self.time
    
    def status(self):
        if isinstance(self.day(), datetime.datetime):
            now = datetime.datetime.now()
            if now < self.day():
                return 'Upcoming'
            elif now - self.day() < datetime.timedelta(days=1):
                return 'Today'
            else:
                return 'Missed'
        else:
            return 'Unknown'
        
    def __str__(self):     
        return str_Intl(self.status() + ' Event: %s' %self.title.encode('utf-8'))    # call to str_Intl is part of bug fix
        # a.encode('utf-8')

# this function created instead of modifying __str__ because in testing, this error cropped up
# both in the use of a print() satement all by itself, and in an event.__str__ call

def str_Intl(strng):   
    try:
        strng2 = strng.encode('utf-8')
        rtnVal = str(strng2)           # if str() throws an error, we have a problem (which is why it is here)
                                       # note that in our code though, we really already know that inputs are string
                                       # so if it weren't for the try test on str() using it might be redundant
    except UnicodeEncodeError as uee:
        print("Warning!")
        print("%s: %s" %(type(uee), uee))
        chrStartIndx = len("'ascii' codec can't encode character ")
        chrEndIndx = str(uee).find(" in position ")
        replStr = str(uee)[chrStartIndx:chrEndIndx] 
        startIndx = (chrEndIndx+1) + len("in position ")
        endIndx = str(uee).find(": ordinal")
        oIndx = int(str(uee)[startIndx:endIndx])
        print("Character %d cannot be processed by print() or str() and will be replaced." %(oIndx))
        print("---------------------")
        rtnVal = (strng[0:oIndx] + ("\"%s\"" %replStr) + strng[(oIndx+1):])
        rtnVal = str_Intl(rtnVal)    # recursive fuction call
        
    except UnicodeDecodeError as ude:
        # early testing with this line from stack overflow did not work for us:
        # strng.encode('utf-8').strip()
        # this solution also strips off the problem characters without outputting what they were
        
        print("Warning!")
        print("%s: %s" %(type(ude), ude))
        # earlier use of .encode() fixed one issue and bypassed the UnicodeEncodeError handling
        # it then triggered this error for one of the other cases, so now we trying other solutions:
        
        rtnVal = strng.encode('utf-8').strip()
        rtnVal = str_Intl(rtnVal)
        
    except Exception as ee:
        # when calling this code in a loop, you lose one string and get this error message output instead
        # but the loop can continue over the rest of the data
        rtnVal = "String data coult not be processed. Error: %s : %s" %(type(ee), ee)
    return rtnVal    
    
text = requests.get('https://www.python.org/events/python-user-group/').text
timePattern = '<time datetime="[\w:+-]+">(.+)<span class="say-no-more">([\d ]+)</span>(.*)</time>'
locationPattern = '<span class="event-location">(.*)</span>'
titlePattern = '<h3 class="event-title"><a href=".+">(.*)</a></h3>'

time = re.findall(timePattern, text)
time = [''.join(i) for i in time]
location = re.findall(locationPattern, text)
title = re.findall(titlePattern, text)

events = [event(title[i], time[i], location[i]) for i in range(len(title))]

for i in events:
    print (30*'-')
    print(i)                                          # bug fix: i is in events, so this calls __str__ in the object
    print ('    Time    :  %s' %i.time)
    print (str_Intl('    Location: %s' %i.location))  # when bug happened here, had to add str_Intl as bug fix