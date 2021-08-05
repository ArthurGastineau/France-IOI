#Lectrue rapide
import sys
ligne = sys.stdin.readline()

#Ecriture rapide
import sys
texte = "ABCDE"
entier = 42
sys.stdout.write("Texte : ")
sys.stdout.write(texte)
sys.stdout.write(str(entier) + "\n")

#Utiliser une fonction main

def main():
    y=1

main()

#Concaténation de liste/tableau
#tres lent
nbItems = 5*1000
liste = []
for item in range(nbItems):
   liste = liste + [item % 10]
#alternative rapide 1
nbItems = 5*1000
liste = [item % 10 for item in range(nbItems)]
#alternative 2
nbItems = 5*1000
liste = []
for item in range(nbItems):
   liste.append(item % 10)
#alternative 3
nbItems = 5*1000
liste = [None] * nbItems
for item in range(nbItems):
   liste[item] = item % 10

#Iterateurs (connait pas taille tableau)
#lent
maxItems = 5*1000
listeTemp = [None] * maxItems
nbItems = 0
for item in range(maxItems):
   if item % 7 == 0:
      listeTemp[nbItems] = item % 10
      nbItems = nbItems + 1
liste = [None] * nbItems
for item in range(nbItems):
   liste[item] = listeTemp[item]
listeTemp = []
#rapide
maxItems = 5*1000
liste = [item % 10 for item in range(maxItems) if item % 7 == 0]
#tres rapide
def maListe(nbItems):
   for item in range(nbItems):
      if item % 7 == 0:
         yield item % 10
maxItems = 5*1000
liste = [item for item in maListe(maxItems)]
#liste = list( maListe(maxItems)) #meme dernier ligne

#Concaténisation rapide de chaine de caracteres
#lent
nbItems = 10*1000
for item in range(nbItems):
   print(item)
#rapide
nbItems = 10*1000
message = "\n".join( map( str, range(nbItems) ) )
print(message)

#si besoin d'appeller une fonction plus de 10000fois 
import sys
sys.setrecursionlimit(1000)