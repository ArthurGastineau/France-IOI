joueur1 = list(input())
joueur2 = list(input())

nb_carte1=len(joueur1)
nb_carte2=len(joueur2)

carte1=0
carte2=0
egalite=0
gagnant=0
while carte1<nb_carte1 and carte2<nb_carte2:
    if joueur1[carte1]==joueur2[carte2]:
        egalite+=1
        carte1+=1
        carte2+=1
    elif joueur1[carte1]<joueur2[carte2]:
        gagnant=1
        break
    else:
        gagnant=2
        break

if carte1==nb_carte1 and carte2==nb_carte2:
    gagnant="="
elif carte1==nb_carte1:
    gagnant=2
elif carte2==nb_carte2:
    gagnant=1
print(gagnant)
print(egalite)
