import sys

def plusProche(valeurs,cible,borne_inf,borne_sup):
    val_inf = valeurs[borne_inf]
    val_sup = valeurs[borne_sup]
    if borne_inf == borne_sup:
        return val_inf
    elif borne_inf+1 == borne_sup:
        if abs(val_inf-x)<=abs(val_sup-x):
            return val_inf
        else:
            return val_sup
    else:
        m = (borne_inf + borne_sup) // 2
        if  cible > valeurs[m]:
            return plusProche(valeurs,cible,m,borne_sup)
        else:
            return plusProche(valeurs,cible,borne_inf,m)

N=int(input())
densites=[int(i) for i in input().split()]
densites.sort()
Q=int(input())
for _ in range(Q):
    x=int(input())
    print(plusProche(densites,x,0,N-1))