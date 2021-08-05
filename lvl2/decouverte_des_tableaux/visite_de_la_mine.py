#gauche=1
#droite=2
#droit=3
#monter=4
#descendre=5

deplacements=int(input())
mouvements=[]
for _ in range(deplacements):
    mouvements.append(int(input()))
arriere=list(reversed(mouvements))

for i in range(deplacements):
    if arriere[i]==4:
        arriere[i]=5
    elif arriere[i]==5:
        arriere[i]=4
    elif arriere[i]==1:
        arriere[i]=2
    elif arriere[i]==2:
        arriere[i]=1
for i in arriere:
    print(i)