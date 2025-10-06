#!/usr/bin/env python3
# decode_ws.py
import sys

def trailing_ws_bits(s):
    # get trailing whitespace only (strip trailing newline first)
    i = len(s)-1
    while i>=0 and s[i] not in (' ', '\t'):
        i -= 1
    if i < 0:
        return ""  # no trailing ws
    # collect trailing ws (from first trailing ws char to end)
    start = i
    while start>=0 and s[start] in (' ', '\t'):
        start -= 1
    tail = s[start+1:len(s)]
    # map to bits: ' ' -> 0, '\t' -> 1
    bits = ''.join('1' if c=='\t' else '0' for c in tail)
    return bits

def bits_to_char(bits):
    if len(bits) < 8:
        bits = bits.rjust(8, '0')  # pad if necessary
    return chr(int(bits[:8], 2))

with open('ws.txt', 'rb') as f:
    chars = []
    for raw in f:
        try:
            line = raw.decode('utf-8', errors='ignore')
        except:
            line = raw.decode('latin1', errors='ignore')
        bits = trailing_ws_bits(line.rstrip('\n'))
        if bits:
            ch = bits_to_char(bits)
            chars.append(ch)
    print(''.join(chars))
