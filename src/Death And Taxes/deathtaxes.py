#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:27:52 2023

@author: fannyshehabi
"""

class Stock:
    
    def __init__(self):
        self.actions = 0
        self.prix_moyen = 0
        self.gain_final = 0
        self.mort = False
    
    def achat(self, x, y):
        new_actions = self.actions + x
        self.prix_moyen = (self.actions * self.prix_moyen + x * y) / new_actions
        self.actions = new_actions
    
    def vente(self, x, y):
        self.actions -= x
    
    def division(self, x):
        self.actions *= x
        self.prix_moyen /= x
    
    def fusion(self, x):
        self.prix_moyen *= x
        self.actions //= x
    
    def deces(self, y):
        self.mort = True
        if y > self.prix_moyen:
            impot = (y - self.prix_moyen) * 0.3
            self.gain_final = self.actions * (y - impot)
        else:
            self.gain_final = self.actions * y
    
    def getProfit(self):
        return self.gain_final

s = Stock()
while not s.mort:
    elt = input().split()
    if len(elt) == 3:
        cmd, x, y = elt
        if cmd == "buy":
            s.achat(int(x), int(y))
        elif cmd == "sell":
            s.vente(int(x), int(y))
    elif len(elt) == 2:
        cmd, x = elt
        x = int(x)
        if cmd == "split":
            s.division(x)
        elif cmd == "merge":
            s.fusion(x)
        elif cmd == "die":
            s.deces(x)

print(s.getProfit())
            