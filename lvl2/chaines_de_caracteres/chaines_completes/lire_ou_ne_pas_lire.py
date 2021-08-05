nbLivres=int(input())
max=0
for _ in range(nbLivres):
    s=input()
    length=len(s)
    if length>max:
        max=length
        print(s)