def threeMax(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else: return c

n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
n3 = int(input("Enter the number: "))

result = threeMax(n1,n2,n3)
print(result)