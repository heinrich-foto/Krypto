#!/usr/bin/env python
 
"""Performs a meet-in-the-middle attack on an RSA-encrypted 
ciphertext C assuming the plaintext M can be factorized into 
	M = M_1 * M_2 with M_1, M_2 <2**b.

"""
 
import os
import sys
import argparse
import re
import random

import gmpy2


def rsa_mitm(n, e, c, b):
    S = random.randint(pow(2,b)/2 , pow(2,b))
    T = random.randint(pow(2,b)/2 , pow(2,b))
    n=gmpy2.mpz(n)
    cs=[gmpy2.mpz()]*(S)
    print S
    print T
    print n

    for s in range(1,S):
        cs[s] = gmpy2.mpz( gmpy2.c_mod(gmpy2.div(c,( gmpy2.powmod(s,e,n))) , n) )
        #print (s,cs[s])
    S_ = (T)/100
    for t in range(1,T):
        for s in range(1,S):
            if cs[s] == (gmpy2.powmod(t,e,n)):
                print (s,s*t)
                return s*t
    print cs
    return "Plaintext nicht gefunden"

def rsa_(n,e,c,b):
    T = pow(2,b)
    n=gmpy2.mpz(n)
    c=gmpy2.mpz(c)
    cs=[gmpy2.mpz()]*(T)
    # counter = 0
    # T_ = T/100
    # percent= 1
    for r in range(1,T):
        cs[r] = gmpy2.c_mod(gmpy2.div(c,gmpy2.powmod(r,e,n)),n)
        # counter += 1
        # if (counter >= T_):
        #     print percent
        #     percent +=1
        #     counter = 0
    #cs.sort()
    print cs
    for s in range (1, T):
        try:
            index=cs.index(gmpy2.powmod(s,e,n))
            #print (gmpy2.c_mod(index*s,n),cs[index],gmpy2.powmod(s,e,n) )
            return index*s
        except ValueError:
            #print (s,gmpy2.powmod(s,e,n))
            # counter += 1
            # if (counter >= T_):
            #     print percent
            #     percent -=1
            #     counter = 0

def main(arguments):
 
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('n', help="RSA modules.", type=argparse.FileType('r'), default="n.txt")
    parser.add_argument('e', help="Public RSA exponent.", type=int)
    parser.add_argument('c', help="Ciphertext.", type=argparse.FileType('r'), default="c.txt")
    parser.add_argument('b', help="Maximum bit length of the factors.", type=int, nargs='?', default=20)
 
    args = parser.parse_args(arguments)

    n = gmpy2.mpz(''.join(re.findall("[-+]?\d+[\.]?\d*", args.n.read())))
    c = gmpy2.mpz(''.join(re.findall("[-+]?\d+[\.]?\d*", args.c.read())))

    # print rsa_mitm( n , args.e , c , args.b )
    print rsa_( n , args.e , c , args.b )


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))