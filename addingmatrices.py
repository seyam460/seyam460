A = [
    [1,2,3],
    [4,5,6]
]
B = [
    [7,8,9],
    [1,4,6]
]
Add_result = []

for i in range (len(A)):
    row = []
    for j in range (len(A[0])):
        row.append (A[i][j] + B[i][j])
    Add_result.append(row)

sub_result = []
for i in range (len(A)):
    row = []
    for j in range (len(A[0])):
        row.append(A[i][j]-B[i][j])
    sub_result.append(row)

print("Addition result:")
for row in Add_result :
  print(row)

print ("subtraction result: ")
for row in sub_result:
  print(row)

    