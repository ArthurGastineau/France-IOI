''''
    Name : Lecture binaire
    Author : Arthur G
    Date : 18 Aug 2021
'''
import sys

if __name__ == '__main__':
    ans=0
    n=[int(i) for i in sys.stdin.readline() if i!="\n"]
    length=len(n)
    for i in range(length):
        ans+=n[i]*2**(length-i-1)
    sys.stdout.write(str(ans))


