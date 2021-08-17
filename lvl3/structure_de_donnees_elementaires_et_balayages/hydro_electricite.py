''''
    Name : Hydroélectricité
    Author : Arthur G
    Date : 17 Aug 2021
'''
if __name__ == '__main__':
    long_centrale,long_riviere = map(int,input().split())
    forces = [int(i) for i in input().split()]
    maximum=0
    for i in range(long_centrale):
        maximum+=forces[i];
    temp=maximum
    for i in range(long_centrale,long_riviere):
        temp+=forces[i]-forces[i-long_centrale]
        if(temp>maximum):
            maximum=temp
    print(maximum)
