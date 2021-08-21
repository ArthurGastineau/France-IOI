'''
    Name : Carton commun
    Author : Arthur G
    Date : 20 Aug 2021
'''

import sys

def solve(code1,code2):
    path1 = findPath(code1)
    path2 = findPath(code2)
    for i in path2:
        for j in path1:
            if i == j:
                return i
    return 0

def findPath(code):
    path=[]
    path.append(code) # il se contient lui meme
    if codes_objets[code] == 0:
        return path
    else:
        debut=codes_objets[code]
        path.append(debut)
        while codes_objets[debut] != 0:
            path.append(codes_objets[debut])
            debut=codes_objets[debut]
        return path

if __name__ == '__main__':
    nombre_de_codes = int(sys.stdin.readline())
    codes_objets = [int(i) for i in sys.stdin.readline().split() if i != "\n"]
    codes_objets.insert(0,0)
    nombre_de_couples = int(sys.stdin.readline())
    for _ in range(nombre_de_couples):
        code1,code2 = map(int,sys.stdin.readline().split())
        print(solve(code1,code2))


    
