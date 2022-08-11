'''
    Name : Anti-virus
    Author : Arthur G
    Date : 22 Aug 2021
'''

import sys

def solve(n, s):
   i = 0
   while n != 0 and i < len(s):
      if s[i] == "?":
         n //= 10
         i += 1
      elif int(s[i])-0 != n % 10:
         return False
      else:
         n //= 10
         i += 1
   if n != 0 or i != len(s):
      return False
   return True


def database():
    data = [0]*(nombre_de_produits+1)
    for i in range(1, nombre_de_produits+1):
        if not data[i]:
            val = 1
            j = i
            temp = i
            while positions[temp] != 0 and not data[temp]:
                temp = positions[temp]
                if not data[temp]:
                    val += 1
            val += data[temp]
            k = val
            while not data[j] and k > 0:
                data[j] = k
                j = positions[j]
                k -= 1
    return data


if __name__ == '__main__':
   nombre_de_produits = int(sys.stdin.readline())
   positions = [int(i) for i in sys.stdin.readline().split() if i != "\n"]
   positions.insert(0, 0)
   masque = [i for i in sys.stdin.readline() if i != "\n"]
   masque.reverse()
   length_of_positions = database()
   ans = []
   for i in range(1, nombre_de_produits+1):
      if solve(i, masque):
         ans.append([length_of_positions[i], i])
   ans = sorted(ans, key=lambda x: x[0])
   for i in range(len(ans)):
       sys.stdout.write(str(ans[i][1])+" ")
