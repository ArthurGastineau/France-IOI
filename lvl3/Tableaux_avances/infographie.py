nbLignes,nbColonnes=map(int,input().split())
nbRectangles=int(input())
data=[[]]
for i in range(nbRectangles):
    a=list(input().split())
    data.append([a[0],a[1],a[2],a[3],a[4]])
image=[["." for i in range(nbColonnes)]for j in range(nbLignes)]
ligne=[]
for i in range(1,nbRectangles+1):
    for row in range(int(data[i][0]),int(data[i][2])+1):
        for col in range(int(data[i][1]),int(data[i][3])+1):
            image[row][col]=data[i][4]
for i in range(len(image)):
    for j in image[i]:
        print(j,end="")
    print()
