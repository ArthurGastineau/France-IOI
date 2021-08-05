total=int(input())
temp_min=int(input())
temp_max=int(input())
for _ in range(total):
    temp=int(input())
    if temp_min<=temp<=temp_max:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        break