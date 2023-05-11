import random
import sys
from math import sqrt
from common import *
from rsa import *
import mpmath
from sympy import solve
from sympy.abc import x

####################
# Q20
####################
def smallN_attack(e,N,c):
    m = mpmath.root(c,e)
    return int(m)

####################
# Q21
####################
def commonFactor_attack(e1, N1, c1, e2, N2):
    p = pgcd(N1, N2)
    
    # Factorize N1
    q = N1 // p
    
    phi = (p - 1) * (q - 1)
    d = inverse_modulaire(phi, e1)
    m = pow(c1, d, N1)
    return m

####################
# Q22
####################
from sympy.ntheory.modular import solve_congruence

def resteChinois(e_123, n_1, c_1, n_2, c_2, n_3, c_3):
    # Use sympy's built in solve_congruence function to find a solution to the system of equations
    crt_solution = solve_congruence((c_1, n_1), (c_2, n_2), (c_3, n_3))
    
    if crt_solution is None:
        return None  # No solution could be found

    crt_solution, _ = crt_solution  # We only need the first part of the solution

    # Compute the eth root of the solution. This is equivalent to RSA decryption.
    m = crt_solution ** (1 / e_123)
    return int(m)


    
####################
# Q23
####################
# todo
