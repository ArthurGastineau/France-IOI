''''
    Name : Changement de base
    Author : Arthur G
    Date : 18 Aug 2021
'''

import sys

def puissancemax(n,baseArrivee):
    ans=1
    i=0
    while ans <= n:
        i+=1
        ans*=baseArrivee
    return i
if __name__ == '__main__':
    ans=0
    baseDepart,baseArrivee,tailleDepart = map(int,input().split())
    entierAConvertir=[int(i) for i in sys.stdin.readline().split()]
    #transforme en decimal
    entier_decimal=0
    for i in range(tailleDepart):
        entier_decimal+=entierAConvertir[i]*baseDepart**(tailleDepart-i-1)
    #transformation dans la base souhaitee
    data=[]
    temp=entier_decimal
    for i in range(puissancemax(entier_decimal,baseArrivee),-1,-1):
        quot,entier_decimal=divmod(entier_decimal,baseArrivee**i)
        data.append(quot)
    if data[0] == 0 and temp!=0:
        del data[0]
    for i in data:
        sys.stdout.write(str(i)+" ")


