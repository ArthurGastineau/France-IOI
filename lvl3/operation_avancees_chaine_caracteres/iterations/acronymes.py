acronymes=list(input())
nbLivres=int(input())
for i in range(nbLivres):
    livre=input()
    resultat=list(livre).copy()
    livre_maj=livre.upper()
    livre_maj=livre_maj.split()
    livre_maj=list(livre_maj)
    initiales=[mot[0] for mot in livre_maj]
    if initiales==acronymes:
        espaces=len(acronymes)
        for i in range(len(resultat)):
            if (i==0 or resultat[i-1]==" "):
                print(resultat[i].upper(),end="")
            else:
                print(resultat[i].lower(),end="")    
        print()


