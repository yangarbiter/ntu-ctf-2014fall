import socket
import struct
import re, sys
import time
import random
import sympy

def W(sc, x):
  sc.send(x)

def R(sc):
  time.sleep(0.4)
  return sc.recv(4096)

def PI(sc, x):
  return struct.pack('I', x)

def UI(sc, s):
  return struct.unpack('I', s)[0]

def inv(x, m):
    return sympy.invert(x, m)

if __name__ == '__main__':
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    sc.connect(('csie.ctf.tw', 6072))
    for i in range(11):
        r = R(sc).split('\n')
        print r
        n = int(r[1])
        m3 = int(r[2])
        m13 = int(r[3])

        """
        a = ((m13 - m3 + 2) * inv(3, n)) % n

        b = (m13 - m3 - 1) * inv(3, n)
        c = (b**2 * inv(m3, n) - 1) % n

        m = (a * inv(c, n)) % n
        """

        m = ((m13 + 2*m3 -1) * inv(m13 - m3 + 2, n)) % n
        print m
        W(sc, str(m)+'\n')
    flag = m
    h = hex(int(flag))[2:-1]
    for i in range(0, len(h), 2):
        if int(h[i]+h[i+1], 16) != 13:
            sys.stdout.write(chr(int(h[i]+h[i+1], 16)))
