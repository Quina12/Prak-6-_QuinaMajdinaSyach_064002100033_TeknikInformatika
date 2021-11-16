# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:24:11 2021

@author: Quina
"""
 
print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")  

from math import pi

def luas_permukaan_kubus(s):
    Luas_kubus = 6 * (s**2)
    return Luas_kubus
def luas_permukaan_balok(p,l,t):
    Luas_balok = 2 * ( (p*l) + (p*t) + (l*t) )
    return Luas_balok
def luas_permukaan_tabung(r,t):
    Luas_tabung = 2*pi*r*(r+t)
    return Luas_tabung
def luas_permukaan_kerucut(r,s):
    Luas_kerucut = (pi*r)*(r+s)
    return Luas_kerucut
def luas_permukaan_bola(r):
    Luas_bola = (4*pi)*(r**2)
    return Luas_bola

while True:
    print("\n----Program Menghitung Luas Bangun Ruang----")
    option = input("1.Kubus\n2.Balok\n3.Tabung\n4.Kerucut\n5.Bola\n6.Exit\nPilih nomor : ")
    if option == "1":
        s = int(input("Masukkan rusuk kubus: "))
        luas_permukaan_kubus(s)
        print("Jadi kubus dengan ukuran rusuk:{}, mempunyai luas:{}".format(s, luas_permukaan_kubus(s)))
    elif option == "2":
        p = int(input("Masukkan panjang balok: "))
        l = int(input("Masukkan lebar balok: "))
        t = int(input("Masukkan tinggi balok: "))
        luas_permukaan_balok(p,l,t)
        print("Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}, mempunyai luas:{}".format(p,l,t, luas_permukaan_balok(p,l,t)))
    elif option == "3":
        r = int(input("Masukkan jari-jari tabung: "))
        t = int(input("Masukkan tinggi tabung: "))
        luas_permukaan_tabung(r,t)
        print("Jadi tabung dengan ukuran jari-jari:{}, tinggi:{}, mempunyai luas:{}".format(r,t, luas_permukaan_tabung(r,t)))
    elif option == "4":
        r = int(input("Masukkan jari-jari: "))
        s = int(input("Masukkan garis lukis: "))
        luas_permukaan_kerucut(r,s)
        print("Jadi kerucut dengan ukuran jari-jari:{}, garis lukis:{}, mempunyai luas:{}".format(r,s, luas_permukaan_kerucut(r,s)))
    elif option == "5":
        r = int(input("Masukkan jari-jari: "))
        luas_permukaan_bola(r)
        print("Jadi bola dengan ukuran jari-jari:{}, mempunyai luas:{}".format(r, luas_permukaan_bola(r)))
    elif option == "6":
        print("Terimakasih")
        break
    else:
        print("Invalid input")