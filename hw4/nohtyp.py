
import base64

#cipher text
a = 'MGs1NTMzMDhzMG40b3FzNXE3OHA2cHByMTZwbjBxbzI0MjgxcG82czAyNDQzNnFvMTM1MDM1MjQxcHNvNnAxcDlyOXExMnM0cDdwcjM1b24xczNxczhwb3JxMzMzMjk5cjUxNDU3OTE1MTlxNDI4cnE2czhwMnAyN29wOTdzMHBvcjZZ'
#decrypt algorithm
b=int(base64.b64decode(a).decode('rot13')[2:-1], 16)
ans = ''
while b > 0:
    ans += chr(b%131)
    b = int(hex(b/131).strip('L')[-1:1:-1], 16)
    while (b-1) % 777 != 0 and b > 0: 
        b *= 16
        #print "XD", b, (b-1)%777
    b = (b-1)/777
    #print b
print ans[-1:0:-1]

#a =  reduce(lambda h, c: int(hex(777 * h + 1).strip('L')[-1:1:-1], 16) * 131 + c
#    , map(ord, raw_input().strip()))

#a =  __import__('base64').b64encode(hex(pow(
#    reduce(lambda h, c:
#        #(lambda f:   # a+b
#        #    #f(lambda *a: f(lambda *a: ((lambda x: f(lambda *a: x(x)(*a)))(lambda x: f(lambda *a: x(x)(*a)))(*a)))(*a))
#        #    (lambda x: f(lambda *a: x(x)(*a)))
#        #    (lambda x: f(lambda *a: x(x)(*a)))
#        #)
#        #(lambda f:lambda a, b: a & b and f((a | b) ^ a & b, (a & b) << 1) or a | b)
#        ##(1, 2)
#        int(hex(777 * h + 1).strip('L')[-1:1:-1], 16) * 131 + c
         # a*b
#        #((lambda *x: (lambda y: y(y, *x))(lambda y, a, b: [lambda : 0, lambda : y(y, b / 2, a) * 2 + (b % 2 and a)][(not not b)]()))
#        #    (int(hex(777 * h + 1).strip('L')[-1:1:-1], 16), 131), c)
#    , map(ord, raw_input().strip())), 1, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000331L)).decode('rot13'))


##The reversed encryption function
#inp = map(ord, raw_input().strip())
#b=inp[0]
#for i in inp[1:]:
#    print b
#    b = int(hex(777 * b + 1).strip('L')[-1:1:-1], 16) * 131 + i
#print b

def f(a, b):
    if (not not b) == 0:
        return 0
    else:
        return f(b/2,a)*2 + (b%2 and a)

