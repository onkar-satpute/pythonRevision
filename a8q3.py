import math

dict1 = {1: 10, 2: 20, 3: 30}

sumresult = sum(dict1) 
mult =  math.prod(dict1.values())
print(sumresult)
print("Multiplication is: ", mult)


nmult = 1
for values in dict1.values():
    nmult *= values
print(nmult)