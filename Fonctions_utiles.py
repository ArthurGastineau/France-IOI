#Transforme un nombre en liste de digits
import math
amour1=999
amour1=[(amour1//(10**i))%10 for i in range(math.ceil(math.log(amour1, 10)), -1, -1)][bool(math.log(amour1,10)%1):]