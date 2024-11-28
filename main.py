import numpy as np
import math
# Algebre

# Multiples et diviseurs dans n, nombres premiers
def diviseurs(n):
    diviseurs = []
    for i in range(1, n + 1):
        if n % i == 0:
            diviseurs.append(i)
    return diviseurs


def multiples(n):  # multiples de n jusaqu'a n^2
    multiples = []
    for i in range(1, n + 1):
        multiples.append(i * n)
    return multiples


def nombresPremiers(n):
    premiers = []
    for i in range(2, n + 1):
        if len(diviseurs(i)) == 2:
            premiers.append(i)
    return premiers


print(diviseurs(10), multiples(10), nombresPremiers(100))


# PGCD et PPCM dans Z. Applications ???
def PGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def PPCM(a, b):
    return a * b // PGCD(a, b)


def estCongruModn(a, b, n):
    if (a - b) % n == 0:
        return True
    else:
        return False


print(PGCD(10, 15), PPCM(10, 15), estCongruModn(10, 15, 5))


# Suites

# Suites numériques. Limites

# Suites définies par récurrence. Applications
def u(n):
    u = 1
    for i in range(1, n + 1):
        u = 3 * u + 2
    return u


def f(x):
    return x ** 2


def derivee(a, epsilon): # approximation de la dérivée de f en a (epsilon petit)
    return (f(a + epsilon) - f(a)) / epsilon

