taxe_act=float(input())
taxe_nouv=float(input())
prix_act=float(input())

prix_init=prix_act*100/(100+taxe_act)
prix_nouv=prix_init*(100+taxe_nouv)/100

print(round(prix_nouv,2))
