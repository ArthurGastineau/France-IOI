lettre=input()
nbLignes=int(input())
occurence=0
for _ in range(nbLignes):
    ligne=input()
    liste=list(ligne)
    for i in liste:
        if i == lettre:
            occurence+=1
print(occurence)