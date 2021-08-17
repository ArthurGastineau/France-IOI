''''
    Name : Carte des cavernes
    Author : Arthur G
    Date : 17 Aug 2021
'''
def solve(num,s):
    ordre=[]
    x = 0
    y = 0
    for i in s:
        y+=1
        if i == '(':
            x+=1
            ordre.append(i)
        elif i == ')':
            if len(ordre)>0 and ordre[-1] == '(':
                del ordre[-1]
                x-=1
            else:
                return 0
    if x==0 and y==num:
        return 1
    else:
        return 0
if __name__ == '__main__':
    nombre_de_caracteres=int(input())
    expression=input()
    #1 si valide 0 autrement
    print(solve(nombre_de_caracteres,expression))