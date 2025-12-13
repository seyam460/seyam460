string = input("enter a string: ")
delimiter = input ("enter the delimiter to split by: ")
new_separator = input ("enter the new separator to join with: ")

parts = string.split(delimiter)

result = new_separator.join(parts)

print ("result: ",result)