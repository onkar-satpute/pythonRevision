n = int(input("Enter the number of element in the list: "))

list = []

for i in range(0, n):
    element = int(input(f"Enter the element no. {i+1}: "))
    list.append(element)

print(list[::-1])
list.reverse()
print(list)
