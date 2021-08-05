def solve(plateau,N):
    #test lignes 
    for row in range(N):
        occurence1=0
        occurence2=0
        for col in range(N):
            if plateau[row][col]=="1"and occurence2<5:
                occurence1+=1
                occurence2=0
            elif plateau[row][col]=="2"and occurence1<5:
                occurence2+=1
                occurence1=0
            else:
                if occurence1>=5:
                    return 1
                occurence1=0
                if occurence2>=5:
                    return 2
                occurence2=0
        if occurence1>=5:
            return 1
        occurence1=0
        if occurence2>=5:
            return 2
        occurence2=0
    #test colonnes 
    for col in range(N):
        occurence1=0
        occurence2=0
        for row in range(N):
            if plateau[row][col]=="1"and occurence2<5:
                occurence1+=1
                occurence2=0
            elif plateau[row][col]=="2" and occurence1<5:
                occurence2+=1
                occurence1=0
            else:
                if occurence1>=5:
                    return 1
                occurence1=0
                if occurence2>=5:
                    return 2
                occurence2=0
        if occurence1>=5:
            return 1
        occurence1=0
        if occurence2>=5:
            return 2
        occurence2=0
    #test des diganonales, il y a 2+(N-5)*4 diagonales dans le plateau a teste  
    #diago obligatoires
    occurence1=0
    occurence2=0
    occurence11=0
    occurence22=0
    for i in range(N):
        #sens1
        if plateau[i][i]=="1" and occurence2<5:
                occurence1+=1
                occurence2=0
        elif plateau[i][i]=="2" and occurence1<5:
            occurence2+=1
            occurence1=0
        else:
            if occurence1>=5:
                return 1
            occurence1=0
            if occurence2>=5:
                return 2
            occurence2=0
        #sens2
        if plateau[i][N-i-1]=="1" and occurence22<5:
            occurence11+=1
            occurence22=0
        elif plateau[i][N-i-1]=="2" and occurence11<5:
            occurence22+=1
            occurence11=0
        else:
            if occurence11>=5:
                return 1
            occurence11=0
            if occurence22>=5:
                return 2
            occurence22=0
    if occurence1>=5 or occurence11>=5:
        return 1
    if occurence2>=5 or occurence22>=5:
        return 2
    #autre diagonales
    if N>5:
        #depart en haut
        for i in range(1,N-5+1):
            #depart cote haut-gauche vers col=N-1
            occurence1=0
            occurence2=0
            for x in range(i,N):
                if plateau[x-i][x]=="1"and occurence2<5:
                    occurence1+=1
                    occurence2=0
                elif plateau[x-i][x]=="2" and occurence1<5:
                    occurence2+=1
                    occurence1=0
                else:
                    if occurence1>=5:
                        return 1
                    occurence1=0
                    if occurence2>=5:
                        return 2
                    occurence2=0
            if occurence1>=5:
                return 1
            if occurence2>=5:
                return 2

            #depart cote haut-droit vers col=0
            occurence11=0
            occurence22=0
            for x in range(N-i-1,-1,-1):
                if plateau[N-i-1-x][x]=="1"and occurence22<5:
                    occurence11+=1
                    occurence22=0
                elif plateau[N-i-1-x][x]=="2" and occurence11<5:
                    occurence22+=1
                    occurence11=0
                else:
                    if occurence11>=5:
                        return 1
                    occurence11=0
                    if occurence22>=5:
                        return 2
                    occurence22=0
            if occurence11>=5:
                return 1
            if occurence22>=5:
                return 2
        #depart en bas
        for i in range(1,N-5+1):
            #depart bas-gauche vers col=N-1
            occurence1=0
            occurence2=0
            for x in range(i,N):
                if plateau[N-x][x]=="1"and occurence2<5:
                    occurence1+=1
                    occurence2=0
                elif plateau[N-x][x]=="2" and occurence1<5:
                    occurence2+=1
                    occurence1=0
                else:
                    if occurence1>=5:
                        return 1
                    occurence1=0
                    if occurence2>=5:
                        return 2
                    occurence2=0
            if occurence1>=5:
                return 1
            if occurence2>=5:
                return 2
            #depart bas-droit vers col=0
            occurence11=0
            occurence22=0
            for x in range(N-i-1,-1,-1):
                if plateau[x+i][x]=="1"and occurence22<5:
                    occurence11+=1
                    occurence22=0
                elif plateau[x+i][x]=="2" and occurence11<5:
                    occurence22+=1
                    occurence11=0
                else:
                    if occurence11>=5:
                        return 1
                    occurence11=0
                    if occurence22>=5:
                        return 2
                    occurence22=0
            if occurence11>=5:
                return 1
            if occurence22>=5:
                return 2
    #si pas de combinaison trouve renvoye 0
    return 0
 

N = int(input())
plateau=[[]]
for i in range(N):
    a=list(input().split(" "))
    a=[i for i in a]
    plateau.append(a)
del plateau[0]
#On a le plateau dans un tableau 2d
if N<5:
    print(0)
else:
    print(solve(plateau,N))