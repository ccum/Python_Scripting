#!/usr/bin/env python

import argparse

parse = argparse.ArgumentParser()

parse.add_argument('filename', help='the file to read')
parse.add_argument('--limit', '-l', type=int, help = 'the number of lines to read')
parse.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args=parse.parse_args()
print(args.filename)

with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]
    
    for line in lines:
        print(line.strip()[::-1])

#chmod u+x parsing_ command_line_parameters.py