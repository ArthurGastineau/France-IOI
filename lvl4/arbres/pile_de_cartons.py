'''
    Name : Pile de cartons
    Author : Arthur G
    Date : 21 Aug 2021
'''
import sys
def solve(ind):
    global data
    if data[ind][0]!=0:
        for i in range(1,len(data[ind])):
            display("A",data[ind][i])
            solve(data[ind][i])
            display("R",data[ind][i])
def display(letter,carton):
    sys.stdout.write(""+str(letter)+" "+str(carton)+"\n")
if __name__ == '__main__':
    nbCartons = int(sys.stdin.readline())
    data=[[]]*(nbCartons+1)
    for i in range(nbCartons+1):
        data[i] = [int(j) for j in sys.stdin.readline().split() if j != "\n"]
    piles=[data[0][i] for i in range(1,len(data[0]))]
    for i in range(len(piles)):
        display("A",piles[i])
        solve(piles[i])
        display("R",piles[i])