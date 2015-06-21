#!/usr/bin/env python
 
"""Performs a meet-in-the-middle attack on an RSA-encrypted 
ciphertext C assuming the plaintext M can be factorized into 
	M = M_1 * M_2 with M_1, M_2 <2**b.

"""
 
import os
import sys
import argparse
import re
import random, math
 

def rsa_mitm(n, e, c, b):
    S = random.randint(pow(2,b)/2 , pow(2,b))
    T = random.randint(pow(2,b)/2 , pow(2,b))
    cs=[0]*S
    print S
    print T
    print n
    for s in range(S):
        cs[s] = (c/(pow(s+1,e))) % n

    for t in range(T):
        for s in range(S):
            if cs[s] == (pow(t+1,e)):
                return s*t
    print cs
    return "Plaintext nicht gefunden"

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

    print rsa_mitm( n , args.e , c , args.b )


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))