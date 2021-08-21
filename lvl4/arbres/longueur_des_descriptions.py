''''
    Name : Retrouver un produit
    Author : Arthur G
    Date : 20 Aug 2021
'''
import sys
    
if __name__ == '__main__':
    nombre_de_codes = int(sys.stdin.readline())
    codes_objets = [int(i) for i in sys.stdin.readline().split() if i!="\n"]
    codes_objets.insert(0,0)
    data=[0]*20001
    ans=0
    for i in range(1,nombre_de_codes+1):
        if not data[i]:
            val=1
            j=i
            temp=i
            while codes_objets[temp]!=0 and not data[temp]:
                temp = codes_objets[temp]
                if not data[temp]:
                    val+=1
            val+=data[temp]
            k=val
            while not data[j] and k>0:
                data[j]=k
                j=codes_objets[j]
                k-=1
        if ans<data[i]:
            ans=data[i]
    print(ans)
