import socket
import struct
import re
import time
import random
import sympy

_mrpt_num_trials = 50 # number of bases to test

#http://rosettacode.org/wiki/Miller-Rabin_primality_test
def is_probable_prime(n):
    #Miller-Rabin
    assert n >= 2
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True # no base tested showed n as composite

def gen_prime(a, b):
    while True:
        r = random.randint(a, b)
        if is_probable_prime(r):
            return r

#CHT from http://rosettacode.org/wiki/Chinese_Remainder_Theorem#Python
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
def chinese_remainder(n, a, lena):
    p = i = prod = 1; sm = 0
    for i in range(lena): prod *= n[i]
    for i in range(lena):
        p = prod / n[i]
        sm += a[i] * mul_inv(p, n[i]) * p
    return sm % prod

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

def get_fp():
    p = gen_prime(2**101, 2**200)

    def gen_enc(a):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        sc.connect(('csie.ctf.tw', 6027))
        R(sc)
        W(sc, str(p)+'\n')
        W(sc, str(a)+'\n')
        enc = R(sc)
        enc = enc.replace('One more magic number please :)\n', '')
        return int(enc.replace('Here is your pfrliamge.\n', ''))

    a = gen_enc(2)
    b = gen_enc(4)
    c = gen_enc(8)

    f2 = ((b-c) * inv((a-b)%p, p)) % p
    ff = (a-b) * inv((f2 - f2**2)%p, p)

    return (a - ((ff*f2)%p) ) % p, p

if __name__ == '__main__':
    n = []
    a = []
    for i in range(5):
        fp, p = get_fp()
        a.append(fp)
        n.append(p)
    h = hex(int(chinese_remainder(n, a, len(a))))[2:-1]
    print h.decode('hex')

