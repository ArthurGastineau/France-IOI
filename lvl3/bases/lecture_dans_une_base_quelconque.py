''''
    Name : Lecture dans une base quelconque
    Author : Arthur G
    Date : 18 Aug 2021
'''

'''
    Votre programme doit lire un entier baseDépart, la base de départ, puis un entier nbChiffres, 
    le nombre de chiffres de l'entier à lire en base baseDépart. Votre programme doit ensuite lire 
    sur la ligne suivante nbChiffres entiers correspondant à l'écriture en base baseDépart de l'entier à convertir. 
    Il doit alors afficher cet entier sous le format classique.
'''
import sys

if __name__ == '__main__':
    ans=0
    baseDepart,nbChiffres = map(int,input().split())
    Chiffres = [int(i) for i in sys.stdin.readline().split()]
    for i in range(nbChiffres):
        ans+=Chiffres[i]*baseDepart**(nbChiffres-i-1)
    sys.stdout.write(str(ans))


