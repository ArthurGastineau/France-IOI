''''
    Name : Écriture dans une base quelconque 
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
    entierAConvertir,baseArrivee = map(int,input().split())
    temp=entierAConvertir
    data=[]
    for i in range(puissancemax(entierAConvertir,baseArrivee),-1,-1):
        quot,entierAConvertir=divmod(entierAConvertir,baseArrivee**i)
        data.append(quot)
    if data[0] == 0 and temp!=0:
        del data[0]
    sys.stdout.write(str(len(data)) + "\n")
    for i in data:
        sys.stdout.write(str(i)+" ")


