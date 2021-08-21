''''
    Name : Fractale : triangle de Sierpinski
    Author : Arthur G
    Date : 17 Aug 2021
'''
def recur(x1,z1,x2,z2):
    if x2-x1==1 and z2-z1==1:
        tab[x1][z1]=1
        tab[x1][z2]=1
        tab[x2][z1]=1
        tab[x2][z2]=0
        return
    recur(x1,z1,x1+(x2-x1)//2,z1+(z2-z1)//2)
    recur(x1+(x2-x1)//2+1,z1,x2,z1+(z2-z1)//2)
    recur(x1,z1+(z2-z1)//2+1,x1+(x2-x1)//2,z2)
    
        
if __name__ == '__main__':
    n=int(input())
    tab=[[0 for i in range(n)] for j in range(n)]
    if n==1:
        print("#")
    else:
        recur(0,0,n-1,n-1)
        for k in range(n):
            for j in range(n-k):
                if(tab[k][j]):
                    print("#",end="")
                else:
                    print(" ",end="")
            print()


