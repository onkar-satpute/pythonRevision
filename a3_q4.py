gender = int(input("Enter gender if male 1 if female 0: "))
if gender == 1 or gender == 0:
    age = int(input("Enter age: "))
    height = int(input("Enter the hieght: "))

    if gender == 1:
        if height > 160 and age > 30:
            print("Condition satisfied")
        else: 
            print("Not eligible")
    elif gender == 0:
        if height > 155 and age > 25:
            print("Condition satisfied")
        else: 
            print("Not eligible")
else:
    print("Enter the proper gender")