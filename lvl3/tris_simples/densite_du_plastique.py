import sys
def dicho(valeurs, cible):
    borne_inf = 0
    borne_sup = len(valeurs)
    if borne_sup == 0:
      return False
    while True:
        m = (borne_inf + borne_sup) // 2
        if borne_inf == m:
          return valeurs[borne_inf] == cible
        if valeurs[m] > cible:
            borne_sup = m
        else:
            borne_inf = m
if __name__ == '__main__':
    N=int(input())
    densites=[int(i) for i in input().split()]
    densites.sort()
    Q=int(input())
    for _ in range(Q):
        x=int(input())
        if dicho(densites,x):
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")