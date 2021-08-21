''''
    Name : Collage d'affiches
    Author : Arthur G
    Date : 18 Aug 2021
'''
import sys
if __name__ == '__main__':
    nbRequetes = int(input())
    data=[]
    for _ in range(nbRequetes):
        info = sys.stdin.readline().split()
        if info[0] == "Q":
            sys.stdout.write(str(len(data))+ "\n")
        elif info[0] == "C":
            hauteur = int(info[1])
            while len(data) !=0 and data[-1]<= hauteur:
                del data[-1]
            data.append(hauteur)