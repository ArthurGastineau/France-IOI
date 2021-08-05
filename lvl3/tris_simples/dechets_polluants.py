# + valeur elevee + polluant
# M : nombre de bacs camion et N : nombre de bas stock
N,M = map(int,input().split())
data = [int(i) for i in input().split()]
print(data)
ans=[]
for i in range(M):
    ans.append(max(data))
    data.remove(ans[i])
for i in ans:
    print(i,end=" ")
