mylist = [1, 2, 3, 4, 5]
sublist = mylist[0:len(mylist)-1]  
last_element = [mylist[-1]]        

mylist = last_element + sublist  
print(mylist)
