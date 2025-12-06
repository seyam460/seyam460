num =int(input("enter a numer: "))
num2 = str(num)
n= len(str(num2))
sum1 = 0 

for digits in num2:
    sum1 += int(digits) ** n

if sum1 == num:
    print("This number is armstrong number: ",num)
else :
    print ("This is not a armstrong number: ",num)