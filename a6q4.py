string = str(input("Enter any String: "))
count = 0
for char in string:
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print("The vowels in given strings are ", count)