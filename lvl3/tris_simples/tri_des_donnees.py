if __name__ == '__main__':
    N=int(input())
    niveau_bacs=[int(i) for i in input().split()]
    res=[]
    for i in range(N):
        min=10**8+1
        for j in range(i,N):
            if niveau_bacs[j]<min:
                min=niveau_bacs[j]
                ind=j
        niveau_bacs[ind],niveau_bacs[i]=niveau_bacs[i],niveau_bacs[ind]
        res.append(min)
    for i in res:
        print(i,end=" ")
    '''niveau_bacs.sort()
    for i in niveau_bacs:
        print(i,end=" ")'''