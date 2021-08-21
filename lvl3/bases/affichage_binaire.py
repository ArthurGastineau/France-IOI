''''
    Name : Affichage binaire
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
    n=int(sys.stdin.readline())
    temp=n
    data=[]
    for i in range(puissancemax(n),-1,-1):
        quot,n=divmod(n,2**i)
        data.append(quot)
    if data[0] == 0 and temp!=0:
        del data[0]
    for i in data:
        sys.stdout.write(str(i))
    

