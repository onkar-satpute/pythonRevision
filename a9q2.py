def sumlist(list1):
    add = 0
    for i in list1:
        add = add + i
    return add

n = int(input("How many values you have enter: "))

l = []
for i in range(n):
    element = int(input("Enter the value: "))
    l.append(element)

result = sumlist(l)
print(result)