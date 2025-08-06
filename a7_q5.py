n = int(input("Enter the no of elements : "))

mylist = []

for i in range(0, n):
    element = int(input(f"Enter the element number {i+1}: "))
    mylist.append(element)

max = mylist[0]
for i in range(0, len(mylist)):
    if mylist[i] > max:
        max = mylist[i]

print(f"The greatest number in the list is: {max}")