import random
import sys
from math import sqrt


####################
# Q1
###################

# retourne le pgcd de deux entiers naturels
def pgcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# algo euclide etendu
# retourne d,u,v avec pgcd(a,b)=d=ua+vb
def euclide_ext(a,b):
    if b == 0:
        return a, 1, 0

    d, u_prev, v_prev = euclide_ext(b, a % b)
    u = v_prev
    v = u_prev - (a // b) * v_prev
    return d, u, v
    
####################
# Q2
####################

# retourne un entier b dans [1,N-1] avec ab=1 modulo N
def inverse_modulaire(N,a):
    d, u, v = euclide_ext(N, a)
    if d == 1:
        return u % N
    else:
        return None

####################
# Q3
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
def expo_modulaire(e, b, n):
    result = 1
    b = b % n  # Réduit la base modulo n
    operations = 0  # Compteur d'opérations

    while e > 0:
        if e % 2 == 1:
            result = (result * b) % n
            operations += 1  # Compte le produit modulo n
        e = e // 2
        b = (b * b) % n
        operations += 2  # Compte la multiplication et le modulo

    print("Nombre d'opérations '×' effectuées:", operations)
    return result



####################
# Q4
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
# O(log(e)) operations
def expo_modulaire_fast(e,b,n):

    result = 1
    b = b % n  # Réduit la base modulo n
    operations = 0  # Compteur d'opérations

    bin_e = bin(e)[2:]  # Représentation binaire de l'exposant
    bin_e = bin_e[::-1]  # Inverse la représentation binaire

    # Effectue les élévations au carré successives
    for i in range(len(bin_e)):
        if bin_e[i] == '1':
            result = (result * b) % n
            operations += 1  # Compte le produit modulo n
        b = (b * b) % n
        operations += 2  # Compte la multiplication et le modulo

    print("Nombre d'opérations '×' effectuées:", operations)
    return result

    
    return 0

####################
# Q5
####################

# retourne la liste des nombres premiers <= n
# methode du crible d Eratosthene
def crible_eras(n):
    primes = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    primes_only = []
    for p in range(2, n):
        if primes[p]:
            primes_only.append(p)
    return primes_only

        
####################
# Q6
####################
# input: n  
# input: t number of tests
# test if prime according to fermat
# output: bool if prime 
def test_fermat(n, t):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    while t > 0:
        a = random.randint(2, n - 2)
        if expo_modulaire_fast(n-1,a, n) != 1:
            return False
        t -= 1
    return True

####################
# Q7
####################

# input: n
# output: r and u coefficient
# for rabin test 
# returns r,u such that 2^r * u = n and u is odd
def find_ru(n):
    r = 0
    u = n
    while u % 2 == 0:
        u //= 2
        r += 1
    return r, u

####################
# Q8
####################

#n entier
#a entier dans [1,n-2]
#pgcd(a,n)=1
#retourne True , si a est un temoin de Rabin de non-primalite de n
def temoin_rabin(a, n):
    r, u = find_ru(n-1)
    x = expo_modulaire_fast(u, a, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(r - 1):
        x = expo_modulaire_fast(2, x, n)
        if x == n - 1:
            return False
    return True


#n entier a tester, t nombre de tests
#retourne True , si n est premier
#retourne False , avec proba > 1-(1/4)**t, si n est compose
def test_rabin(n, t):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for _ in range(t):
        a = random.randrange(2, n - 1)
        if temoin_rabin(a, n):
            return False
    return True
            
# prime generator
# output: n range for prime number
# utilise votre implementation de rabin (ou la plus effice si rabin non dispo)
# pour generer un nombre premier sur n bits.
# range de n: p = random.randint(pow(2,n-1),pow(2,n)-1)
def gen_prime(n):
    while True:
        p = random.randint(pow(2, n - 1), pow(2, n) - 1)
        if test_rabin(p, 5):  # 5 est un choix arbitraire pour le nombre de tests
            return p

####################
# Helper functions for rsa/elgamal
####################

# Helper function
# convert str to int
def str_to_int(m):
    s = 0
    b = 1
    for i in range(len(m)):
        s = s + ord(m[i])*b
        b = b * 256
    return s

# Helper function
# convert int to str
def int_to_str(c):
    s = ""
    q,r = divmod(c,256)
    s = s+str(chr(r))
    while q != 0:
        q,r = divmod(q,256)
        s = s+str(chr(r))
    return s
