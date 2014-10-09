#HW2

###0x02 - Lottery (Tag: Pwnable)
Send it with a very long number it would exec /bin/sh.

###0x02 - Traverse (Tag: Shellcode)
A naive way to triverse through link list and check each value in key would need 18 bytes.
Use op code popa and check only half of the bits in key could shorten 1 byte each way.

Alternative way: search for string "FLAG" in whole heap from the head of linked-list. (14 bytes)

Source code: traverse.s
