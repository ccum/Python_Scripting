#!/usr/bin/env python

from time import localtime, strftime, mktime

start_time = localtime()
print("timer start at %s" % strftime("%X",start_time))

#wait for unser input
raw_input("please press Enter to continue...")

stop_time =  localtime()
difference =  mktime(stop_time) -  mktime(start_time)

print ("timer stop at %s"  %  strftime("%X", stop_time))
print ("total time : %s seconds" % difference)

#chmod u+x using_standard_library_packages.py