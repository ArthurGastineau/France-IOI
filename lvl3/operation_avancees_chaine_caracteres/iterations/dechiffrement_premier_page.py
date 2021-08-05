lettres=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
grille_decryptage=list(input())
texte=list(input())

for i in range(len(texte)):
    if ord(texte[i])>=ord("A") and ord(texte[i])<=ord("Z"):
        texte[i]=chr(ord(grille_decryptage[lettres.index(texte[i])])-32)
    elif ord(texte[i])>=ord("a") and ord(texte[i])<=ord("z"):
        texte[i]=grille_decryptage[lettres.index(chr(ord(texte[i])-32))]
    print(texte[i],end="")


    