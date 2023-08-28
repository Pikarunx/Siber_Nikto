#! usr/bin/env/python
# -*- coding: utf-8 -*-

import os
import time

os.system("apt install figlet")
os.system("clear")
os.system("clear")
os.system("figlet NIKTO ")

print("""
-------------------------Nikto Tooluna Hoş Geldiniz.-------------------------

1)Termux Kullanıcıları İçin 

2)Kali Linux Kullanıcıları İçin

""")

secim = input("Lütfen Hangi Terminali Kullanıyorsanız Rakamını Girin: ")

if (secim == "1"): 
    print("""
    Termux Terminal
    """)
    os.system("git clone https://github.com/sullo/nikto")
    os.system("cd nikto/program")
    hedef = input("Hedef Websitesini Girin: ")
    os.system("perl nikto.pl -h " + hedef)	

elif (secim == "2"):
    print("""
    Linux Terminal
    """)
    site = input("Hedef Websitesini Girin: ")
    os.system("nikto -h " + site)	
    
else:
    print("HATALI SEÇİM YAPTINIZ.PROGRAM KAPATILIYOR...")
    time.sleep(5)             
    
	
