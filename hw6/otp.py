
import itertools

#ACC = [ord(' '), ord('{'), ord('}'), ord('\'')] + range(48, 58) + range(65, 91) + range(97, 123)
ACC = [ord(' ')] + range(ord('a'), ord('z')+1) + range(ord('A'), ord('Z')+1)
#ACC = range(32, 127)
accept = [ACC[i]^ACC[j] for i in range(len(ACC)) for j in range(len(ACC))]

with open("otp-bcb81a8e326fe8950d712237beb0f169.enc", "r") as f:
    ciphers = f.readlines()
    r = []
    ci = []
    for cipher in ciphers:
        ci.append([])
        for i in range(0,len(cipher)-1,2):
            ci[-1].append(int(cipher[i]+cipher[i+1], 16))

"""
candidates = []
for i in range(300):
    keys = []
    candidates.append([])
    for k in range(256):
        for c in ci:
            if (k ^ c[i]) not in ACC:
                break
        if c == ci[-1]:
            keys.append(k)
    for c in ci:
        candidates[-1].append([])
        for k in keys:
            candidates[-1][-1].append(k^c[i])

print candidates[1]
for i in range(40):
    for c in candidates[i][-1]:
        print chr(c),
    print ""
"""
plain = """In cryptography, a one-time pad (OTP) is an encryption technique that
cannot be cracked if used correctly. In this technique, a plaintext is paired
with random, secret key (or pad). Then, each bit or character of the plaintext
is encrypted by combining it with the corresponding bit or character from the
pad using modular addition. If the key is truly random, is at least as long as
the plaintext, is never reused in whole or in part, and is kept completely
secret, then the resulting ciphertext will be impossible to decrypt or
break.[1][2] It has also been proven that any cipher with the perfect secrecy
property must use keys with effectively the same requirements as OTP keys.[3]
However, practical problems have prevented one-time pads from being widely
used."""

print len(plain), len(ci[0])
key = []
for i in range(len(plain)-1):
    key.append(ord(plain[i]) ^ ci[0][i])

for k in range(10):
    for i in range(min(len(plain), len(ci[k]))):
        print chr(key[i] ^ ci[k][i]),
