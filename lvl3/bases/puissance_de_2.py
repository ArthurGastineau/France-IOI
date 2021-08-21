''''
    Name : Puissance de 2
    Author : Arthur G
    Date : 18 Aug 2021
'''
import sys
if __name__ == '__main__':
    n=int(sys.stdin.readline())
    ans=1
    while ans <= n:
        ans*=2
    sys.stdout.write(str(ans//2))