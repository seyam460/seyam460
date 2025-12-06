start = int(input("enter start of interval: "))
end = int(input("enter end of interval: "))

for num in range(start,end+1):
    if num>1 :
        for i in range(2,num):
            if num % i == 0:
                break 

else :
    print("prime numbers:",num)
