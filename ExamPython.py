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

TableauMot = random.choice(mots)
print(TableauMot)

lettre = input("quelle lettre voulez vous chercher? ")

i=0
j = 0
nombreLettre = 0


def Position(TableauMot):
    for i in range(len(TableauMot)):
        if TableauMot[i] == lettre:
            print(Back.RED + lettre, "est présent au caractère n°", i+1)

def Tentative(TableauMot):
    lettre = 0
    for i in TableauMot:
        for j in Essai:
            if i == j: 
                lettre = lettre + 1
            else:
                lettre = lettre
    print("il y a", lettre, "lettres correspondante à votre essai !")

def CompteurLettre(TableauMot):
    compteur = 0
    for i in TableauMot:
        if lettre == i:
            compteur = compteur + 1
    print("il y à", compteur, lettre, "dans votre mot")

Position(TableauMot)
CompteurLettre(TableauMot)
Essai = input ("essayez de trouver le mot ")
Tentative(TableauMot)



input()