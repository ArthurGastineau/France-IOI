positions=int(input())
changements=int(input())
table=[]
#pour chaque place on atrribue le numero de la personne
for _ in range(positions):
    table.append(int(input()))

for _ in range(changements):
    position1=int(input())
    position2=int(input())
    temp=table[position1]
    table[position1]=table[position2]
    table[position2]=temp

for i in table:
    print(i)
