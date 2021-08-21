''''
    Name : Plus long palindrome
    Author : Arthur G
    Date : 18 Aug 2021
'''
import sys

def solve(s)-> str:
        maxLen=0
        ans=""
        if len(s)==0:
            return 0
        elif s.count(s[0])==len(s):
            return s
        else:
            for i in range(len(s)):
                if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                    start=i-maxLen-1
                    maxLen+=2
                    continue

                if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                    start=i-maxLen
                    maxLen+=1
            return s[start:start+maxLen]
if __name__ == '__main__':
    print(len(solve(sys.stdin.readline())))