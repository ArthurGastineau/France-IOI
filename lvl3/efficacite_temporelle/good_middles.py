''''
    Name : Les bons milieux
    Author : Arthur G
    Date : 18 Aug 2021
'''
import sys

def solve(data):
    ans=[[0 for i in range(128)]for j in range(128)]
    for i in range(nbPoints):
        for j in range(i+1,nbPoints):
                x1 = (data[i][0]+data[j][0])
                y1 = (data[i][1]+data[j][1])
                if x1%2==0 and y1%2==0:
                    ans[x1//2][y1//2]+=1
    res=0
    for i in range(nbPoints):
        if ans[data[i][0]][data[i][1]]:
            res+=1
    return res
if __name__ == '__main__':
    data=[]
    nbPoints=int(input())
    for _ in range(nbPoints):
        x,y=map(int,sys.stdin.readline().split())
        data.append((x,y))
    '''On a donc un tableau avec les cords'''
    print(solve(data))

