''''
    Name : versurs de Hanoï
    Author : Arthur G
    Date : 17 Aug 2021
'''
def recur(de,vers,n):
    if n==1:
        print(de," -> ",vers)
        return
    if( de==1 and vers==3)or(de==3 and vers==1):
         x=2
    if(de==2 and vers==3)or(de==3 and vers==2):
         x=1
    if(de==1 and vers==2)or(de==2 and vers==1):
         x=3
    recur(de,x,n-1)
    print(de," -> ",vers)
    recur(x,vers,n-1)

if __name__ == '__main__':
    n=int(input())
    recur(1,3,n)




