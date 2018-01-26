#!/usr/bin/env python

user = {'admin': True, 'active': True, 'name': 'Cesar'}

if user['admin'] and user['active']:
    print ("ACTIVE - (ADMIN) %s" % user['name'])
else:
    print (user['name'])

