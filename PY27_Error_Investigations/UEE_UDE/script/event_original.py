#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Here is the first version of the event() object
# it gets used in the code that follows (where the problem occurs)

import re
import datetime
import requests

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
        return self.status() + ' Event: %s' %self.title

# this version is unchanged from lecture content.  It throws an error as shown below in the output

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
    print(i)
    print ('    Time:  %s' %i.time)
    print ('    Location: %s' %i.location)		