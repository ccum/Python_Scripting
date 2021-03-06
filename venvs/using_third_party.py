#!/usr/bin/env python

import sys
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url', help='URL to store the content of')
parser.add_argument('filename', help='the filename to store the content under')
parser.add_argument('--content-type', '-c',
                default='html',
                choices=['html', 'json'],
                help='the content-type of the URL being requested')

args = parser.parse_args()

res = requests.get(args.url)

if res.status_code >=400:
    print("Error code received: %s" % res.status_code)
    sys.exit(1)

if args.content_type == 'json':
    try:
        content = res.json()
    except ValueError:
        print("Error: Content in not JSON")
        sys.exit(1)
else:
    content = res.text

with open(args.filename, 'w') as f:
    f.write(content.encode("UTF-8"))
    print("Content writte to '%s'" % args.filename)
