def convertisseur(valeur):
    length=len(valeur)
    lettre=valeur[length-1]
    if lettre=="m":
        valeur[0]=round(float(valeur[0])*(1/0.3048),6)
        valeur[length-1]="p"
    if lettre=="g":
        valeur[0]=round(float(valeur[0])*0.002205,6)
        valeur[length-1]="l"
    if lettre=="c":
        valeur[0]=round(float(valeur[0])*1.8+32,6)
        valeur[length-1]="f"
    for i in valeur:
        print(i,end=" ")
    print()

nombre=int(input())
for _ in range(nombre):
    valeur=list(input().split())
    convertisseur(valeur)
