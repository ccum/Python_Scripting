#!/usr/bin/env python

import random
import os
import json

count = os.getenv("FILE_COUNT") or 100
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for indentifier in range(1,count +1):
    amount = random.uniform(1.0, 1000.0)
    content = {
        'topic' : random.choice(words),
        'value' : "%.2f" % amount
    }
    with open('./new/reciept-%s.json' % indentifier, 'w') as f:
        json.dump(content,f)