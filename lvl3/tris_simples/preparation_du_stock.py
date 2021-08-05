#classer les bacs du moins poluant au plus
def findIndex(value,data):
    index=0
    while index<len(data) and data[index]<value:
        index+=1
    return index
# M : nombre a iserer et N : nombre de bacs stock
N,M = map(int,input().split())
data = [int(i) for i in input().split()]
new = [int(i) for i in input().split()]
index=[]
for i in range(M):
    new_index=findIndex(new[i],data)
    index.append(new_index)
    data.insert(new_index,new[i])
#output
for i in index:
    print(i,end=" ")
print()
for i in data:
    print(i,end=" ")