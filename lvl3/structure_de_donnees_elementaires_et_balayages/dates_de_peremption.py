''''
    Name : Dates de péremption
    Author : Arthur G
    Date : 17 Aug 2021
'''
if __name__ == '__main__':
    data=[]
    operations = int(input())
    for _ in range(operations):
        quantite,type_operation = map(int,input().split())
        # ope = 0 si vente, autrement represente date de peremption produit 1998_11_04 sans "_"
        if quantite>0:
            for i in range(quantite):
                data.append(type_operation)
        else:
            for i in range(abs(quantite)):
                del data[-1]
    print(min(data))
