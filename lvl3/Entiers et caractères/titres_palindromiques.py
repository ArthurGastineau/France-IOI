def main():
    nbLivres = int(input())
    for _ in range(nbLivres):
        sauv=input()
        nom=sauv.lower()
        nom=list(nom)
        i=0
        length=len(nom)
        while i<length:
            if nom[i] == ' ':
                nom.remove(' ')
                length-=1
            else:
                i+=1
        palyndrome=[]
        for j in range (len(nom)-1,-1,-1):
            palyndrome.append(nom[j])
        if nom==palyndrome:
            print(sauv)
        
main()