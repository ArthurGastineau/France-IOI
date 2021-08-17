if __name__ == '__main__':
    nbBacs=int(input())
    data=[]
    for _ in range(nbBacs):
        idBac,nivPollution=map(int,input().split())
        data.append((nivPollution,idBac))
    data.sort()
    for i in data:
        print(i[1],i[0])