nbPages=int(input())
for j in range(2,nbPages+1):
    page=list(input())
    if j%2==0:
        k=3*j
    else:
        k=-5*j
    for i in range(len(page)):
        if ord(page[i])>=ord("A") and ord(page[i])<=ord("Z"):
            page[i]=chr((ord(page[i])-ord("A")-k)%26+ord("A"))
        elif ord(page[i])>=ord("a") and ord(page[i])<=ord("z"):
            page[i]=chr((ord(page[i])-ord("a")-k)%26+ord("a"))
        print(page[i],end="")
    print()

