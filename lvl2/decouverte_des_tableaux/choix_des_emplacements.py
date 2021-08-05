nbEmplacmeents=int(input())

liste=[]

for i in range(nbEmplacmeents):
    liste.append(int(input()))

for i in range(len(liste)):
    print(liste.index(i))