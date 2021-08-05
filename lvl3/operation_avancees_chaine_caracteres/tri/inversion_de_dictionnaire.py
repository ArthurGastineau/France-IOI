nbMots = int(input())
dict1=[]
dict2=[]
for i in range(nbMots):
    mot1,mot2=map(str,input().split())
    dict1.append(mot2)
    dict2.append(mot1)
mem=dict1.copy()
dict1.sort()
dic2=[0]*nbMots
for i in range(nbMots):
    dic2[i]=dict2[mem.index(dict1[i])]
for i in range(nbMots):
    print(dict1[i],dic2[i])
