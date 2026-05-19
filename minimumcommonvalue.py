def getcommon(num1: list[int] , num2: list[int]) -> int :
    i , j = 0 , 0

    while i< len(num1) and j< len(num2) :
        if num1[i] == num2[j]:
            return num1[i]
        elif num1[i]<num2[j] :
            i+=1
        else :
            j+=1


num1 = [1,2,5]
num2=[2,4]
result = getcommon(num1 , num2)
print(result)


   