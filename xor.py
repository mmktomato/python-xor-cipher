#!/usr/bin/env python3

import sys
import argparse
from getpass import getpass
from pathlib import Path
from hashlib import sha256

def get_seed(key):
    return sha256(key.encode('utf-8')).digest()

def parse_args():
    parser = argparse.ArgumentParser(description='XOR cipher')
    parser.add_argument('infile', help='input file path')
    parser.add_argument('outfile', help='output file path')
    parser.add_argument('--key', help='encryption password')

    args = parser.parse_args()

    if args.key is None:
        key = getpass()
    else:
        key = args.key

    return (Path(args.infile), Path(args.outfile), key)

def validate_args(infile, outfile, seed):
    if not infile.is_file():
        sys.exit('"{}" is not a file.'.format(infile))

    if infile.stat().st_size < len(seed):
        sys.exit('infile must be larger than {} bytes.'.format(len(seed)))

    if outfile.is_file():
        sys.exit('"{}" is already exists.'.format(outfile))

if __name__ == '__main__':
    (infile, outfile, key) = parse_args()
    seed = get_seed(key)
    validate_args(infile, outfile, seed)

    with infile.open('rb') as f_in:
        with outfile.open('wb') as f_out:
            i = 0
            while f_in.peek():
                c = ord(f_in.read(1))
                j = i % len(seed)
                b = bytes([c ^ seed[j]])
                f_out.write(b)
                i = i + 1

