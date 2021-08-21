''''
    Name : Retrouver un produit
    Author : Arthur G
    Date : 19 Aug 2021
'''
import sys
    
if __name__ == '__main__':
    nombre_de_codes = int(sys.stdin.readline())
    positions = [int(i) for i in sys.stdin.readline().split() if i!="\n"]
    nombre_description = int(sys.stdin.readline())
    codes_objets = [int(i) for i in sys.stdin.readline().split() if i!="\n"]
    for i in range(nombre_description):
        if positions[codes_objets[i]-1]==0:
            sys.stdout.write(str(codes_objets[i])+"\n")
        else:
            data=[]
            debut=codes_objets[i]
            data.append(debut)
            while positions[debut-1] != 0:
                data.append(positions[debut-1])
                debut=positions[debut-1]
            data=data[::-1]
            for i in data:
                sys.stdout.write(str(i)+" ")
            sys.stdout.write("\n")