def solve(min_abs1,max_abs1,min_ord1,max_ord1,min_abs2,max_abs2,min_ord2,max_ord2):
    #bors dans un autre carre
    if min_abs2>=max_abs1 or max_abs2<=min_abs1 or min_ord2>=max_ord1 or max_ord2<=min_ord1 :
        print("NON")
        return
    else :
       print("OUI")
       return 

t =int(input())
for _ in range(t):
    min_abs1=int(input())
    max_abs1=int(input())
    min_ord1=int(input())
    max_ord1=int(input())
    min_abs2=int(input())
    max_abs2=int(input())
    min_ord2=int(input())
    max_ord2=int(input())
    solve(min_abs1,max_abs1,min_ord1,max_ord1,min_abs2,max_abs2,min_ord2,max_ord2)