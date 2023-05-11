import random
from math import sqrt
from common import *

####################
# Q14
####################

# retourne p g
# g generateur sur le groupe Z*p => on utilise 3
# p premier sur n bits.


def gen_elgamal_pg(n):

    p = gen_prime(n)

    g = 3

    return p, g

####################
# Q15
####################

# retourne couple cle prive/publique [sk,pk]
# definit tel que sk compris entre (3,p-2)
# pk =  g^sk [p]
# output: [sk,pk]


def gen_elgamal_sk_pk(p, g):

    sk = random.randint(3, p - 2)

    pk = expo_modulaire_fast(sk, g, p)

    return sk, pk

####################
# Q16
####################

# pk_a,sk_a,pk_b,sk_b sont les cles publiques prive de A B modulo p
# retourne le secret partage par A et B


def gen_elgamal_get_secret(pk_a, sk_a, pk_b, sk_b, p):
    secret_A = expo_modulaire_fast(sk_a, pk_b, p)
    secret_B = expo_modulaire_fast(sk_b, pk_a, p)

    if secret_A == secret_B:
        return secret_A
    else:
        return None

####################
# Q17
####################

# chiffrement du message m avec le secret
# output: chaine de charactere c en binaire  represantant c
# cotrainte: secret plus grand que message


def enc_elgamal(m, secret, p):
    # indice transormez le message (et le secret en binaire) en binaire:
    # bin_m = bin(str_to_int(m))[2:]

    bin_m = bin(str_to_int(m))[2:]

    # Chiffrer chaque bit du message avec le secret partagé
    cipher = []
    for bit in bin_m:
        if bit == '0':
            c = expo_modulaire_fast(2, secret, p)
        else:
            c = (expo_modulaire_fast(2, secret, p) * secret) % p
        cipher.append(c)

    cipher_str = ''.join(str(c) for c in cipher)

    return cipher_str

# dechiffrement du message c avec le secret
# output: chaine de charactere m
# cotrainte: secret plus grand que message


def dec_elgamal(c, secret, p):
    return ''

####################
# Q19
####################

# retourne la signatue [r, s]
# sk cle secrete utilise pour signer message m
# m sous forme de texte


def elgamalsignature(g, p, sk, m):

    k = random.randint(1, p-2)

    r = expo_modulaire_fast(k, g, p)

    # Calculer s = (sk - r * sk) * k^-1 mod (p-1)
    k_inv = inverse_modulaire(k, p-1)
    s = ((str_to_int(sk) - r * str_to_int(m)) * k_inv) % (p-1)

    return [r, s]

# r,s signature
# pk cle publique utilise pour signer message m
# m sous forme de texte
# output: bool verifie si signature valide
# true = valid


def elgamalverification(g, p, r, s, m, pk):

    if r < 1 or r > p-1 or s < 1 or s > p-1:
        return False

    v1 = (expo_modulaire_fast(r, pk, p) * expo_modulaire_fast(s, r, p)) % p

    v2 = expo_modulaire_fast(str_to_int(m), g, p)

    if v1 == v2:
        return True
    else:
        return False
