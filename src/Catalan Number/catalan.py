#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:03:31 2023

@author: fannyshehabi
"""

import sys
sys.setrecursionlimit(5000)

def binom(n, k):
    prod = 1
    for i in range(k):
        prod = (prod * (n - i)) // (i + 1)
    return prod

dico = {0: 1, 1: 1}


def catalan(n):
    if n in dico:
        return dico[n]
    else: 
        dico[n] = (4 * n - 2) * catalan(n-1) // (n + 1) 
        return dico[n]

#ent = input()
ent = sys.stdin.read()

liste = ent.splitlines()

q = int(liste[0])

for i in range(q):
    x = int(liste[i+1])
    print(catalan(x))
