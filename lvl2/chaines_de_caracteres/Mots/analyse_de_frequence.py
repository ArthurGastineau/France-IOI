first_ligne=list(input().split())
nblignes=int(first_ligne[0])
nbMots=int(first_ligne[1])
occurences=[0]*101

for i in range(nblignes):
    mots=list(input().split(" "))
    for i in range(len(mots)):
        occurences[len(mots[i])]+=1

for i in range (len(occurences)):
    if occurences[i]!=0:
        print(i,":",occurences[i])

