#!/usr/bin/env python



with open('example.txt', 'a') as xmen_file:
    xmen_file.write('\nhola 5\n')

xmen_file = open('example.txt')
for line in xmen_file:
    print line

xmen_file.close()

#chmod u+x interacting_with_files.py