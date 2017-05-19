#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# This version of the code assumes we want to to see warnings and error content along with as much of the output
# as can be processed around the characters causing the problem

''' Here we see code designed to find the mis-behaving characters, output as much as we know about them
    (text originally captured in the error messages when the code halted), output as much as possible of
    the non-misbehaving content, and continue to run.  
    
    The output when the error is encountered is ugly, but this is deliberate.  It shows all errors triggers and
    highlights the recursive nature of this solution for future study.
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-  

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
        return str_Intl(self.status() + ' Event: %s' %self.title)    # call to str_Intl is part of bug fix

# this function created instead of modifying __str__ because in testing, this error cropped up
# both in the use of a print() satement all by itself, and in an event.__str__ call

def str_Intl(strng):   
    try:
        rtnVal = str(strng)
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
    except Exception as ee:
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
    print(i)                                         # bug fix: i is in events, so this calls __str__ in the object
    print ('    Time    :  %s' %i.time)
    print (str_Intl('    Location: %s' %i.location)) # when bug happened here, had to add str_Intl as bug fix