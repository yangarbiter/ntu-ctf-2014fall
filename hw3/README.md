#HW3

###0x03 - fmtrop (Tag: Pwnable)
This service reads until the character 'n' and echos it back.

This service has a vulnerability in format string and buffer overflow. Use format string to get the ASLR shift and canary then call gets and system to get the flag.

Source code: fmtrop.py
