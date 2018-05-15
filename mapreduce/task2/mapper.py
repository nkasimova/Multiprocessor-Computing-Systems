#!/usr/bin/env python

import sys
import time
from datetime import date

for line in sys.stdin:
    try:
        user_id, date_, url, diff = line.strip().split('\t', 3)
    except ValueError as e:
        continue
    url = url.split('/')[2]
    if (url[0:4] == "www."):
        url = url.split("www.")[1]
    week_day = date.fromtimestamp(date_).isoweekday() 
    count = 0
    if (week_day >= 6):
        count = 1
    print "%s\t%d" % (url, count)


