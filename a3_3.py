n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))
n3 = int(input("Enter the number 3: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} is the greater number")
elif n2 < n3:
    print(f"{n3} is greater number")
else:
    print(f"{n2} is greater number")
