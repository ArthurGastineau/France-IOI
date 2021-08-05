import math
lettres=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

nom1,nom2=map(str,input().split())
amour1=0
amour2=0
for i in nom1:
    amour1+=lettres.index(i)
for i in nom2:
    amour2+=lettres.index(i)
while amour2>=10:
    amour2=[(amour2//(10**i))%10 for i in range(math.ceil(math.log(amour2, 10)), -1, -1)][bool(math.log(amour2,10)%1):]
    res=0
    for i in amour2:
        res+=i
    amour2=res
while amour1>=10:
    amour1=[(amour1//(10**i))%10 for i in range(math.ceil(math.log(amour1, 10)), -1, -1)][bool(math.log(amour1,10)%1):]
    res=0
    for i in amour1:
        res+=i
    amour1=res
print(amour1,amour2)
