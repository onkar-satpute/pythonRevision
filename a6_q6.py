string = str(input("Enter any String: "))
character = str(input("Enter any character: "))
count = 0
idx = -1

for char in string:
    idx += 1
    if character == char:
        count += 1
        print(idx)
if count > 0:
    print(f"The character present in the string with {count} times")