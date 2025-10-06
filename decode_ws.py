#!/usr/bin/env python3
# decode_ws.py - decode Part C (trailing whitespace) from committed ws.txt

import subprocess

def get_ws_blob():
    """Return the committed ws.txt content as a list of lines."""
    try:
        # ensure we are on the correct branch
        subprocess.run(["git", "checkout", "steg-whitespace"], check=True, stdout=subprocess.DEVNULL)
        # get committed blob
        result = subprocess.run(["git", "show", "HEAD:ws.txt"], check=True, capture_output=True)
        lines = result.stdout.splitlines()
        return [line.decode('latin1') for line in lines]
    except subprocess.CalledProcessError:
        print("Error: ws.txt not found in HEAD. Check branch.")
        return []

def decode_trailing_whitespace(lines):
    """Decode trailing whitespace into ASCII characters using a bitstream."""
    bits_stream = ""
    for line in lines:
        line = line.rstrip('\n')
        # find trailing whitespace
        i = len(line) - 1
        while i >= 0 and line[i] not in (' ', '\t'):
            i -= 1
        if i < 0:
            continue
        start = i
        while start >= 0 and line[start] in (' ', '\t'):
            start -= 1
        tail = line[start+1:i+1]
        bits_stream += ''.join('1' if c=='\t' else '0' for c in tail)

    # decode 8-bit chunks
    out = []
    for j in range(0, len(bits_stream), 8):
        byte = bits_stream[j:j+8]
        if len(byte) == 8:
            out.append(chr(int(byte, 2)))
    return ''.join(out)

if __name__ == "__main__":
    lines = get_ws_blob()
    if not lines:
        print("No lines to decode.")
    else:
        part_c = decode_trailing_whitespace(lines)
        print("Part C (decoded):", part_c)
