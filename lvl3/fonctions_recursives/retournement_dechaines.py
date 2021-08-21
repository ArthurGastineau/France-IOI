''''
    Name : retournement de chaîne
    Author : Arthur G
    Date : 18 Aug 2021
'''
def recur(debut,fin):
    print (ligne[debut],end="")
    if debut == fin:
        return
    else:
        recur(debut-1,fin)

if __name__ == '__main__':
    ligne=[i for i in input()]
    fin = len(ligne)-1
    recur(fin,0)

