dict1 = {'a': 1, 'b': 2, 'c': 3, 'd':4}

keyvalue = input("Enter the key to find: ")


if keyvalue in dict1.keys():
    print("present")
else: 
    print("absent")