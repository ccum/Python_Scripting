#!/usr/bin/env python
import glob
import os
import shutil
import json
import re

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory alredy exists")

#get a list of receipts

#receipts = glob.glob("./new/reciept-[0-9]*.json")
receipts = [f for f in glob.iglob('./new/reciept-[0-9]*.json')
            if re.match('./new/reciept-[0-9]*[02468].json', f) ]
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name =path.split('/')[-1]
    destination = path.replace('new','processed')
    shutil.move(path, destination)
    print("moved '%s' to '%s'" % (path, destination))

print("Receipt subtotal: $%.2f" % round(subtotal , 2))

