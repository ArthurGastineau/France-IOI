''''
    Name : état du stock
    Author : Arthur G
    Date : 17 Aug 2021
'''
if __name__ == '__main__':
    type_produits = int(input())
    produits_par_type = [int(i) for i in input().split()]
    operations = int(input())
    for _ in range(operations):
        numero,quantite = map(int,input().split())
        produits_par_type[numero-1]+=quantite
    for i in produits_par_type:
        print(i,end=" ")

