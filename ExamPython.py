import random

from colorama import init
init()
from colorama import Fore, Back, Style
init(autoreset=True)

mot1 = "vaches"
mot2 = "pigeon"
mot3 = "gemmes"
mot4 = "huiler"
mot5 = "fusils"
mot6 = "goudas"
mot7 = "douves"
mot8 = "coques"
mot9 = "oignon"
mot10 = "consul"
mots = [mot1, mot2, mot3, mot4, mot5, mot6, mot7, mot8, mot9, mot10]

a= random.choice(mots)
print(a)

lettre= input("quelle lettre voulez vous chercher? ")

i=0
 
for i in range(len(a)):
    if a[i] == lettre:
         print(Back.RED + lettre, "est présent au caractère n°", i+1)
    else:
        print(Back.YELLOW + lettre,  "est absent au caractère n°", i+1)
    i=i+1  

input()
