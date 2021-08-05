ligne = input()
liste=list(ligne)
for i in range(len(liste)):
    if liste[i] == " ":
        liste[i]="_"
for i in liste:
    print(i,end="")