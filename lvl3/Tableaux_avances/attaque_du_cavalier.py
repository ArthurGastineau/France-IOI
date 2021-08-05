#lettre maj : piece blanche
#afficher yes si un cavalier blanc peut se deplacer vers une case blanche
def solve(x,y,plateau):
    if 1<=x+2<9 and 0<=y+1<8 and ord(plateau[x+2][y+1])<=ord("z") and ord(plateau[x+2][y+1])>=ord("a"):
        return 1
    elif 1<=x+2<9 and 0<=y-1<8 and ord(plateau[x+2][y-1])<=ord("z") and ord(plateau[x+2][y-1])>=ord("a"):
        return 1
    elif 1<=x-2<9 and 0<=y+1<8 and ord(plateau[x-2][y+1])<=ord("z") and ord(plateau[x-2][y+1])>=ord("a"):
        return 1
    elif 1<=x-2<9 and 0<=y-1<8 and ord(plateau[x-2][y-1])<=ord("z") and ord(plateau[x-2][y-1])>=ord("a"):
        return 1
    elif 1<=x+1<9 and 0<=y+2<8 and ord(plateau[x+1][y+2])<=ord("z") and ord(plateau[x+1][y+2])>=ord("a"):
        return 1
    elif 1<=x+1<9 and 0<=y-2<8 and ord(plateau[x+1][y-2])<=ord("z") and ord(plateau[x+1][y-2])>=ord("a"):
        return 1
    elif 1<=x-1<9 and 0<=y+2<8 and ord(plateau[x-1][y+2])<=ord("z") and ord(plateau[x-1][y+2])>=ord("a") :
        return 1
    elif 1<=x-1<9 and 0<=y-2<8 and ord(plateau[x-1][y-2])<=ord("z") and ord(plateau[x-1][y-2])>=ord("a") :
        return 1
    else:
        return 0

def main():
    plateau=[[]]
    for i in range(8):
        a=list(input())
        a=[i for i in a]
        plateau.append(a)
    res=False
    for row in range(1,9):
        for col in range(0,8):
            if plateau[row][col]=="C":
                if solve(row,col,plateau)==1:
                    res=True
    if res==True:
        print("yes")
    else:
        print("no")
    
main()