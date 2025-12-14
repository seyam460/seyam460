import re 
s = input("enter a string: ")
numbers = re.findall(r'\d+',s)

for num in numbers :
    print (num)