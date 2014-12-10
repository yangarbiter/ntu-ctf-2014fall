#!/usr/bin/env python

import socket, struct, re, base64, time

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sc.connect(('csie.ctf.tw', 16060))

def W(x):
  sc.send(x)
  #time.sleep(0.05)

def R():
  return sc.recv(40960)

def go(s):
    R()
    W('a\n') #15
    R()
    W(s+'\n')
    cipher = R()
    #print cipher
    return base64.b64decode(cipher[8:])

#uid: 97, passwor
#d: ccccccccccccc
#cccc, flag: FFFF
#FFFFFFFFFFFFFFFF
"""
R()
W('a'*18+'\n') 
R()
W('c'*15+'\n')
print R()
exit()
"""

FLAG = ''
for i in range(7):
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    sc.connect(('csie.ctf.tw', 16060))
    base = go('c'*(20-i))
    #print base64.b64encode(base[32:48])
    for k in range(32, 128):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        sc.connect(('csie.ctf.tw', 16060))
        ret = go('c'*13 + 'c'*(7-i) + ', flag: ' + FLAG + chr(k))
        #print base64.b64encode(ret[32:48])
        if ret[32:48] == base[32:48]:
            FLAG += chr(k)
            break
    print FLAG

for i in range(16):
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    sc.connect(('csie.ctf.tw', 16060))
    base = go('c'*(13-i))
    for k in range(32, 128):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        sc.connect(('csie.ctf.tw', 16060))
        ret = go('c'*13 + (', flag: '+FLAG)[-15:] + chr(k))
        #print base64.b64encode(ret[32:48])
        if ret[32:48] == base[32:48]:
            FLAG += chr(k)
            break
    print FLAG



