#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 17:40:24 2022

@author: fannyshehabi
"""


import sys

file = sys.stdin.read()
liste = file.splitlines()

def inverse(mat):
    a, b = mat[0]
    c, d = mat[1]
    det = a*d - b*c
    return [[d/det, -b/det], [-c/det, a/det]]


l = []
for i in range(0, len(liste) - 1, 3):
    l.append([liste[i], liste[i + 1]])

res = []
for i in range(0, len(l)):
    a, b = l[i][0].split()
    c, d = l[i][1].split()
    a, b, c, d = int(a), int(b), int(c), int(d)
    A = [[a, b], [c, d]]
    res.append(inverse(A))

for i in range(1, len(res) + 1):
    print("Case", i, end="")
    print(":")
    for elt in res[i - 1]:
        for i in range(len(elt) - 1):
            print(int(elt[i]), end=" ")
        print(int(elt[len(elt) - 1]))