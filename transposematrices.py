A = [
    [1,2],
    [2,3],
    [5,6]
]
rows = len(A)
col = len(A[0])

transpose = []

for c in range (col):
    new_row = []
    for r in range(rows):
        new_row.append(A[r][c])
    transpose.append(new_row)

print("transpose matrix: ")
for rows in transpose :
    print(rows)