#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 12:25:11 2023

@author: fannyshehabi
"""

import sys
from collections import defaultdict

ent = sys.stdin.read()
#ent = input()

liste = ent.splitlines()

n, d = map(int, liste[0].split())
compte =  defaultdict(lambda: 0)


for elt in map(int, liste[1].split()):
    compte[elt // d] += 1

res = 0
for n in compte.values():
    res += (n * (n-1)) // 2 
print(res)