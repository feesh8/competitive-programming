#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:14:43 2023

@author: fannyshehabi
"""

s = input()
t = input()

n = len(s)
m = len(t)

# Départ dans s où commence la sous séquence de t
lst = [-1 for _ in range(m)]

count = 0
last = -1

for i in range(n):
    for j in range(m-1, 0, -1):
        if s[i] == t[j]:
            lst[j] = lst[j-1]
    if t[0] == s[i]:
        lst[0] = i
    if t[m-1] == s[i] and lst[m-1] >= 0:
        count += (lst[m-1] - last) * (n - i)
        last = lst[m - 1]
print(count)
