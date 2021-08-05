def main():
    occurence=[0]*26
    nb_lettres=0
    lettres=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    phrase=input()
    phrase_maj=phrase.upper()
    for i in phrase_maj:
        if ord(i)>=ord("A") and ord(i)<=ord("Z"):
            occurence[lettres.index(i)]+=1
            nb_lettres+=1
    for i in occurence:
        print(round(i/nb_lettres,6))

main()