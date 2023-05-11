import random
import sys
from math import sqrt
from common import *

####################
# Q9
####################

# input: n
# output: e,d,N
def gen_rsa(n):
    p = gen_prime(n)
    q = gen_prime(n)
    N = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while pgcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = inverse_modulaire(phi, e)
    return e, d, N
    
####################
# Q10
####################    
    
# e exponent
# N modulo
# m message
# output: c
# message/cipher sous forme de nombre
def enc_rsa(m, e, N):
    return expo_modulaire_fast(e, m, N)

# d exponent
# N modulo
# c cipher 
# output m   
# message/cipher sous forme de nombre
def dec_rsa(c, d, N):
    return expo_modulaire_fast(d, c, N)

####################
# Q11
####################

# e exponent
# N modulo
# m message sous forme de texte
# output: c sous forme de nombre
def RSAcipher(e, N, m):
    m_int = str_to_int(m)
    return enc_rsa(m_int, e, N)

# d exponent
# N modulo
# c cipher sous forme de nombre
# output: m message sous forme de texte

def RSAdecipher(d, N, c):
    m_int = dec_rsa(c, d, N)
    return int_to_str(m_int)

####################
# Q13
####################

# d exponent
# N modulo
# m message sous forme de texte
# output: sig
def RSAsignature(d, N, m):
    m_int = str_to_int(m)
    return enc_rsa(m_int, d, N)

# e exponent
# N modulo
# m message sous forme de texte
# sig signature
# output: bool verifie si signature valide
# true = valid
def RSAverification(e, N, m, sig):
    m_int = RSAdecipher(e, N, sig)
    if m == m_int:
        return True
    else:
        return False
