''''
    Name : Premier absent
    Author : Arthur G
    Date : 18 Aug 2021
'''
import sys
if __name__ == '__main__':
    n,p=map(int,sys.stdin.readline().split())
    data=[False]*(250001)
    min=0
    for i in range(p):
        eleve = int(sys.stdin.readline())
        eleve-=1
        if eleve < p:
            data[eleve]=True
        while min < n and data[min]:
            min+=1
        if min == n:
            sys.stdout.write("-1"+"\n")
        else:
            sys.stdout.write(str(min+1)+"\n")