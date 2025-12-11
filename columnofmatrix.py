matrix = [
    [4,5,6],
    [1,2,3],
    [7,12,5]
]

k=1 
column = []
for row  in matrix :
    column.append(row[k])

print("k-th column: ",column)
