#!/usr/bin/env python3
# decode_ws.py - decode Part C (trailing whitespace) directly from committed ws.txt

import subprocess

def get_ws_blob():
    """Return the committed ws.txt content as a list of lines."""
    try:
        # make sure we are on the correct branch
        subprocess.run(["git", "checkout", "steg-whitespace"], check=True, stdout=subprocess.DEVNULL)
        # get committed blob of ws.txt
        result = subprocess.run(["git", "show", "HEAD:ws.txt"], check=True, capture_output=True)
        lines = result.stdout.splitlines()
        return [line.decode('latin1') for line in lines]
    except subprocess.CalledProcessError:
        print("Error: ws.txt not found in HEAD. Check branch.")
        return []

def decode_trailing_whitespace(lines):
    """Decode trailing spaces/tabs into ASCII characters."""
    out = []
    for line in lines:
        # remove newline only, preserve trailing spaces/tabs
        line = line.rstrip('\n')
        # find last trailing whitespace run
        i = len(line)-1
        while i >=0 and line[i] not in (' ', '\t'):
            i -= 1
        if i < 0:
            continue
        start = i
        while start >=0 and line[start] in (' ', '\t'):
            start -= 1
        tail = line[start+1:i+1]  # only trailing whitespace

        # convert whitespace to bits
        bits = ''.join('1' if c=='\t' else '0' for c in tail)

        # take all 8-bit chunks
        for j in range(0, len(bits), 8):
            byte = bits[j:j+8]
            if len(byte) == 8:
                out.append(chr(int(byte,2)))
    return ''.join(out)

if __name__ == "__main__":
    lines = get_ws_blob()
    if not lines:
        print("No lines to decode.")
    else:
        part_c = decode_trailing_whitespace(lines)
        print("Part C (decoded):", part_c)
