#!/usr/bin/env python

import os

stage = (os.getenv("STAGE") or "development").upper()

output = "we are running in %s" % stage

if stage.startswith("PROD"):
    output = "DANGE!!! " + output

print(output)
#STAGE= prod
# chmod u+x working_with_environment_variables.py
