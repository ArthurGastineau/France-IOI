''''
    Name : Entre deux
    Author : Arthur G
    Date : 18 Aug 2021
'''
def recur(n,taille):
    if taille<0:
        return
    else:
        print(n,end=" ")
        recur(n+1,taille-1)

if __name__ == '__main__':
    n,m = map(int,input().split())
    taille = m-n
    recur(n,taille)

