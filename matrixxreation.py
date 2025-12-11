n = int(input("enter a number: "))

matrix = []
num = 1
for i in range (n):
    row = []
    for j in range (n):
        row.append(num)
        num+= 1
    matrix.append (row)

print ("generated n*n matrix: ")
for row in matrix :
    print (row)
