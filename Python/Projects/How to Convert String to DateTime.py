#!/usr/bin/env python3
from datetime import datetime
from dateutil import parser

date = 'May 4 2004 7:14AM'
print(type(date))

date_time = datetime.strptime(date, '%b %d %Y %I:%M%p')
print(date_time)
print(type(date_time))

date_time = parser.parse('May 4 2004 7:14AM')
print(date_time)
print(type(date_time))
