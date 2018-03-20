#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in the word fle')

arg = parser.parse_args()
snippet = arg.snippet.lower()

words = open('/usr/share/dict/words').readlines()

matches= []

# for word in words:
#     if snippet in word.lower():
#         matches.append(word)

print([word.strip() for word in words if snippet in word.lower()]) 

#chmod x+u contains.py       
#contains.py Keith