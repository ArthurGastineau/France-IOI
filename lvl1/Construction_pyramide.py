max_pierres=int(input())
taille=0
pierres=0
if pierres>=max_pierres:
    taille=0
    pierre=0
else:
    while pierres<=max_pierres:
        taille+=1
        pierres+=(taille)**2
    pierres-=(taille)**2
    taille-=1
print(taille)
print(pierres)