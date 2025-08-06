n = int(input("Enter how many element you have to enter inteh list: "))
list = []
for i in range(0,n):
    e = int(input("Enter the element: "))
    list.append(e)
print(list)

for j in range(0, len(list), 2):
    print(list[j], end=" ")