''''
    Name : 0 + 0 = la tête à Toto
    Author : Arthur G
    Date : 17 Aug 2021
'''
def recur(ans,n):
    if n!=0:
        ans=[i for i in ans]
        for i in range(len(ans)):
            if ans[i] == '0':
                ans[i]="(0 + 0)"
        x=""
        for i in ans:
            x+=i
        recur(x,n-1)
    else:
        print("0 = "+ans)
    
        
if __name__ == '__main__':
    n=int(input())
    ans ="0"
    recur(ans,n)


