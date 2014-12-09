#!/usr/bin/env python

import socket, struct, re, base64, time, random

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sc.connect(('csie.ctf.tw', 6060))

def W(x):
  sc.send(x)
  time.sleep(0.3)

def R():
  return sc.recv(40960)

target = \
"NfHBHcVs1MzChTWg/yPibl97EcV9e566VfocKI60xhOVG/ko1PVQ2g9F5etdzLiAwPhczk8zPqJ99ohkKWehVg=="

target = base64.b64decode(target)

ans = [0]*64

for i in range(1, 4):
    c1 = []
    for j in range(16):
        c1.append(random.randint(0, 255))

    for j in range(15, -1, -1):
        for k in range(len(c1)):
            c1[k] ^= (16-j) ^ (15-j)

        al = ''
        for k in range(0xff):
            c1[j] = k
            c = ''.join(map(chr, c1)) + target[i*16:(i+1)*16]
            al += base64.b64encode(c)+'\n'
        W(al)
        t = R().split('\n')

        for k in range(0xff):
            if t[k] == 'true':
                break

        c1[j] = k
        ans[i*16+j] = (16-j) ^ k ^ ord(target[(i-1)*16+j])
        print ans

s = ''
for i in ans:
    s += chr(i)
print s
