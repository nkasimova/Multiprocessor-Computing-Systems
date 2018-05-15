#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    try:
        article_id, text = line.strip().split('\t', 1)
    except ValueError as e:
        continue
    texr = ' ' + text + ' '
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    words = words[1:-1]
    words = list(set(words))
    for word in words:
        print "%s\t%d" % (word.lower(), 1)

