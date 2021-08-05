def solve(x,y):
    if x<0 or x>90 or y<0 or y>70:
        print("En dehors de la feuille")
        return
    elif x>10 and x<85 and y>10 and y<55:
        if x>25 and x<50 and y>20 and y<45:
            print("Dans une zone jaune")
            return
        else:
            print("Dans une zone bleue")
            return
    elif (x>15 and x<45 and y>60 and y<70) or (x>60 and x<85 and y>60 and y<70):
        print("Dans une zone rouge")
        return
    else:
        print("Dans une zone jaune")
        return
    

nombre_jetons = int(input())
for _ in range(nombre_jetons):
    x=int(input())
    y=int(input())
    solve(x,y)