n = int(input("Enter any number: "))

isPrime = 0

if n == 2 or n == 3:
    isPrime = 1
else:
    for i in range(2,(n//2)+1):
        if n%i==0:
            isPrime = 0
            break
        else:
            isPrime = 1
if isPrime:
    print("Given number is prime number")
else: 
    print("Not prime")