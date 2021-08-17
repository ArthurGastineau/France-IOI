if __name__ == '__main__':
    N=int(input())
    matieres=[]
    for _ in range(N):
        matieres.append(input())
    ans=sorted(matieres, key=str)
    for i in ans:
        print(i)