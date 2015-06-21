#!/usr/bin/env python
 
"""Performs a meet-in-the-middle attack on an RSA-encrypted 
ciphertext C assuming the plaintext M can be factorized into 
	M = M_1 * M_2 with M_1, M_2 <2**b.

"""
 
import os
import sys
import argparse
import re
 

def rsa_mitm(n, e, c, b):
    T = 2 ^ (a*l)
    for (r in range(T)):
        x[i] = (c / r ^ e ) mod n
    for (s in range(T)):
        if s ^e mod N == x_r:
            return r*s mod n

def main(arguments):
 
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('n', help="RSA modules.", type=argparse.FileType('r'), default="n.txt")
    parser.add_argument('e', help="Public RSA exponent.", type=int)
    parser.add_argument('c', help="Ciphertext.", type=argparse.FileType('r'), default="c.txt")
    parser.add_argument('b', help="Maximum bit length of the factors.", type=int, nargs='?', default=20)
 
    args = parser.parse_args(arguments)

    n = int(''.join(re.findall("[-+]?\d+[\.]?\d*", args.n.read())))
    c = int(''.join(re.findall("[-+]?\d+[\.]?\d*", args.c.read())))

    print rsa_mitm( n , e , c , b )


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))