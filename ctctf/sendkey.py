#!/usr/bin/env python

import httplib, sys

def sendkey(key):
    conn = httplib.HTTPConnection("10.217.0.100")
    conn.request("GET",
    "/team/submit_key?token=7d6251fc73922705186fa2eb5bba3e60&key=%s" % (key))
    r1 = conn.getresponse()
    print r1.read()

if __name__ == '__main__':
    try:
        sendkey(sys.argv[1])
    except:
        print "error"
