''''
    Name : Nombre encadré
    Author : Arthur G
    Date : 17 Aug 2021
'''
def recur(ans,crochets):
    if crochets!=0:
        ans.append("]")
        ans.insert(0,"[")
        recur(ans,crochets-1)
    return ans
        
if __name__ == '__main__':
    val,crochets = map(int,input().split())
    ans=[]
    ans.append(val)
    ans2=recur(ans,crochets)
    res=""
    for i in ans2:
        res+=str(i)
    print(res)