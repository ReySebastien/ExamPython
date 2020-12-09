import random

from colorama import init
init()
from colorama import Fore, Back, Style

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

a="bonjour"
lettre= input("quelle lettre voulez vous chercher? ")
i=0
 
for i in range(len(a)):
    if a[i] == lettre:
         print(lettre, "est présent au caractère n°", i+1)
    else:
        print(lettre,  "est absent au caractère n°", i+1)
    i=i+1  

input()