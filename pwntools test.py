import sys
import base64
from Crypto.Util.number import *
from pwn import *

test_bytes = bytes.fromhex(
    '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

inv_test_bytes = bytes([~byte & 0xFF for byte in test_bytes])
inv_test_bytes

xor(test_bytes, inv_test_bytes)
