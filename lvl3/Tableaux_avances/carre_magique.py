n = int(input())
def test(values):
    occurences=[0]*(n**2)
    for i in values:
        if i>n**2 or i<1:
            return 1
        else:
            occurences[i-1]+=1
    for i in range(n):
        if occurences[i]!=1:
            return 1
    return 0
result=True
carre=[[]]
values=[]
for i in range(n):
    a=list(input().split())
    a=[int(i) for i in a]
    for j in a:
        values.append(j)
    carre.append(a)
data=[]
values.sort()
tests=test(values)
if tests==1:
    result=False
else:
    for row in range(1,n+1):
        somme_col=0
        somme_row=0
        for col in range(n):
            somme_col+=carre[row][col]
            somme_row+=carre[col+1][row-1]
        data.append(somme_col)
        data.append(somme_row)
    somme_diag1=0
    somme_diag2=0
    for x in range(n):
        somme_diag1+=carre[x+1][x]
        somme_diag2+=carre[x+1][n-x-1]
    data.append(somme_diag1)
    data.append(somme_diag2)
    val=data[0]
    for i in data:
        if i!=val:
            result=False
            break

if result==True:
    print("yes")
else:
    print("no")


