
import binascii, sympy

p = 1625450042535909011445240376867
q = 1667188025682557916066408577777

c = 2471127468490475711245908980882847002501927735481574400484385
e = 65537

modInv = lambda x, m: int(sympy.invert(x, m))

phi = (p-1)*(q-1)
d = modInv(e, phi)
msg = pow(c, d, p*q)
print(binascii.unhexlify(hex(msg)[2:-1]))
