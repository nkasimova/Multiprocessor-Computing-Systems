#!/usr/bin/env python

import sys

current_key = None
sum_weekdays = 0
sum_day_off = 0
for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
        count = int(count)
    except ValueError as e:
        continue
    if current_key != key:
        if current_key:
            print "%s\t%d\t%d" % (current_key, sum_weekdays, sum_day_off)
        sum_weekdays = 0
        sum_day_off = 0
        current_key = key
    if (count == 0):
        sum_weekdays += 1
    else:
        sum_day_off += count

if current_key:
    print "%s\t%d\t%d" % (current_key, sum_weekdays, sum_day_off)

