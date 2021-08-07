nbAutomobiles=int(input())
ordre_arrive=[int(i) for i in input().split()]
#il faut donc trier la liste dans l'ordre croissant avec le moins de modifications possibles
depassements=0
data=[]
val=1
while val<nbAutomobiles:
    ind=ordre_arrive.index(val)
    for i in range(ind,val-1,-1):
        temp=ordre_arrive[i]
        ordre_arrive[i]=ordre_arrive[i-1]
        ordre_arrive[i-1]=temp
        data.append(ordre_arrive[i])
        data.append(temp)
        depassements+=1
    val+=1
print(depassements)
for i in range(depassements):
    print(data[i*2],data[i*2+1])
