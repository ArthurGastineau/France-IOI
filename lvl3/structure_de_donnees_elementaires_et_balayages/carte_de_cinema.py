''''
    Name : Carte de cinéma
    Author : Arthur G
    Date : 17 Aug 2021
'''
def solve(cartes):
    data=[0]*1000000
    for i in cartes:
        data[i]+=1
        if data[i]==2:
            return i
    return -1
if __name__ == '__main__':
    clients=int(input())
    cartes = [int(i) for i in input().split()]
    print(solve(cartes))
