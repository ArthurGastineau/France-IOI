''''
    Name : Moyenne hexadécimale
    Author : Arthur G
    Date : 18 Aug 2021
'''

import sys
import math

def puissancemax(n,base):
    ans=1
    i=0
    while ans <= n:
        i+=1
        ans*=base
    return i

def hexa_to_decim(n):
    for i in range(len(n)):
        if ord(n[i]) <= 70 and ord(n[i])>=65:
            n[i]= int(ord(n[i])-55)
        else:
            n[i]=int(n[i])
    return n

def decim_to_hexa(n):
    temp=n
    data=[]
    for i in range(puissancemax(n,16),-1,-1):
        quot,n=divmod(n,16**i)
        if quot>=10:
            data.append(chr(55+quot))
        else:
            data.append(quot)
    if data[0] == 0 and temp!=0:
        del data[0]
    data=[str(i) for i in data]
    return data

def hexa(n):
    length=len(n)
    ans=0
    for i in range(length):
        ans+=n[i]*16**(length-i-1)
    return ans
    
if __name__ == '__main__':
    n = [i for i in sys.stdin.readline() if i!="\n"]
    n=hexa(hexa_to_decim(n))
    data=[]
    for _ in range(n):
        data.append(hexa(hexa_to_decim([i for i in sys.stdin.readline() if i!="\n"])))
    moyenne=decim_to_hexa(math.floor(sum(data)/len(data)))
    res=""
    for i in moyenne:
        res+=i
    sys.stdout.write(res)
    

    

