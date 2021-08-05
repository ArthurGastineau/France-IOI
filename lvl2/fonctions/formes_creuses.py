nombre_X=int(input())
nombre_ligne_rectangle=int(input())
nombre_colonne_rectangle=int(input())
nombre_ligne_triangle=int(input())

for _ in range(nombre_X):
    print("X",end="")
print()
for i in range(nombre_ligne_rectangle):
    for j in range(nombre_colonne_rectangle):
        if i==0 or i==nombre_ligne_rectangle-1:
            print("#",end="")
        elif j==0 or j==nombre_colonne_rectangle-1:
            print("#",end="")
        else:
            print(" ",end="")
    print()
for i in range(nombre_ligne_triangle+1):
    if i==0 or i==1 or i==nombre_ligne_triangle:
        for _ in range(i):
            print("@",end="")
    else:
        for j in range(i):
            if j==0 or j==i-1:
                print("@",end="")
            else:
                print(" ",end="")
    print()

        
