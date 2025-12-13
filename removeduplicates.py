string = input ("enter a string: ")

result = " "

for ch in string :
    if ch not in result :
        result += ch

print ("result: ",result)