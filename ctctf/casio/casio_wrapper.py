#!/usr/bin/python2

import subprocess, sys, select, os

src = os.environ['REMOTE_HOST']
#if not src.endswith('.201'):
#    exit(1)

f = open('/var/tmp/ctc/casio.log-' + os.environ['REMOTE_HOST'], 'a')
ns = '/var/tmp/wrap/c84eb09f-e040-4221-8508-c6c5b3e792a9'
p = subprocess.Popen([
    ns, '-Ur', ns, '-m', '/bin/bash', '--norc', '-c', '''
mount --bind /srv /tmp
mount --bind /srv /usr/bin
mount --bind /srv /var/tmp/ctf
mount --bind /srv /var/tmp/ctc
mount --bind /home/flags /temp
mount --bind /var/tmp/wrap/04985a98-0411-48cf-b9b7-193d0b28381c /home/flags
exec {} -U /home/casio/casio
'''.format(ns)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

with open('/home/flags/casio', 'r') as ff:
    flag = ff.read().strip('\n')

#if os.environ['REMOTE_HOST'] != '127.0.0.1':
#       exit()
src = os.environ['REMOTE_HOST']

f.write('starts\n')
count = 0
count4 = 0
notok = ['1 47 134590464 134520432 134515376', '1 98 134590465 134520432 134515376', '1 105 134590466 134520432 134515376', '1 110 134590467 134520432 134515376', '1 47 134590468 134520432 134515376']
cancelnext = False

while True:
    readable, writable, exceptional = select.select([sys.stdin, p.stdout], [], [])
    if count >= 3000 and '10.217.2' in src:
        exit()
    if count4 == len(notok) and '10.217.4' in src:
        exit()

    if p.stdout in readable:
        data = os.read(p.stdout.fileno(), 2048)
        if len(data) ==2048:
            count += 1
        if notok[count4] in data:
            count4 += 1
        if 'flagcatxxdbase64' in data:
            data = 'w' * len(data)
        if data == '': break
        data = data.replace(flag, 'w'*len(flag))
        f.write(src + "==> my stdin # " + data + '\n')
        try:
            os.write(sys.stdout.fileno(), data)
        except Exception:
            f.write("p stdin error")
            break

    if sys.stdin in readable:
        data = os.read(sys.stdin.fileno(), 2048)
        if data == '': break
        if len(data) ==2048:
            count += 1
        try:
            data.index('134520432')
            os.kill(p.pid, 15)
            exit(1)
        except Exception:
            pass
        try:
            data.index('29263339')
            os.kill(p.pid, 15)
            exit(1)
        except Exception:
            pass
        try:
            data.index('wget')
            os.kill(p.pid, 15)
            exit(1)
        except Exception:
            pass
        try:
            data.index('crontab')
            os.kill(p.pid, 15)
            exit(1)
        except Exception:
            pass
        try:
            data.index('cat /home/flags/casio')
            os.kill(p.pid, 15)
            exit(1)
        except Exception:
            pass
        try:
            data.index('cat /temp/casio')
            os.kill(p.pid, 15)
            exit(1)
        except Exception:
            pass
        f.write(src + "==> sys.stdin # " + data + '\n')
        try:
            os.write(p.stdin.fileno(), data)
        except Exception:
            f.write("socket error")
            break
f.write('XD' + str(count) + '\n')
f.write('XDX' + str(count4) + '\n')
