def checkCase(s):
    uppercnt = 0
    lowercnt = 0
    spacecnt = 0
    for char in s:
        if char.isupper():
            uppercnt +=1
        elif char.islower():
            lowercnt +=1
        elif char.isspace():
            spacecnt +=1
    return(uppercnt,lowercnt,spacecnt)

sentence = str(input("Enter any string: "))

result = checkCase(sentence)

print(result)