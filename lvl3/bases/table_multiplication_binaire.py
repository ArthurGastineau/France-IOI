''''
    Name : Table de multiplication binaire
    Author : Arthur G
    Date : 18 Aug 2021
'''

import sys

def puissancemax(n):
    ans=1
    i=0
    while ans <= n:
        i+=1
        ans*=2
    return i

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    max = t*t
    for j in range(1,t+1):
        for i in range(1,t+1):
            n=i*j
            temp=i*j
            data=[]
            for i in range(puissancemax(n),-1,-1):
                quot,n=divmod(n,2**i)
                data.append(quot)
            if data[0] == 0 and temp!=0:
                del data[0]
            for k in data:
                sys.stdout.write(str(k))
            sys.stdout.write("\t")
        sys.stdout.write("\n")

    

