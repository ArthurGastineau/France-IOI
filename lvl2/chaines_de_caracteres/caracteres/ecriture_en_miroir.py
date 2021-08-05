nbLignes=int(input())

for _ in range(nbLignes):
    s=list(input())
    res=[]
    for i in range(len(s)-1,-1,-1):
        print(s[i],end="")
    print()
