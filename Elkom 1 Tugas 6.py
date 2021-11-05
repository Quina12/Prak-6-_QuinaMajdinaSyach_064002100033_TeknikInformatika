# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:20:19 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

print("\n NIM : 064002100033 -> GANJIL")

print("\n MENGHITUNG JARAK TEMPUH GLBB")

def glbb(v0, t, a):
    s = (v0*t) + 0.5 * (a*t**2)
    print(f"\n Jarak tempuh jika kecepatan awal = {v0}, waktu = {t}, dan percepatan = {a} adalah {s}")
    return s    
    
v0 = int(input(" Masukkan angka v0 : "))
t = int(input(" Masukkan angka t : "))
a = int(input(" Masukkan angka a : "))

glbb(v0, t, a)