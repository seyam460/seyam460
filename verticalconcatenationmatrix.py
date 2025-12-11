matrix = [
    ["g","i","g"],
    ["i","b","r"],
    ["f","h","a"]
]
rows = len (matrix )
cols = len (matrix[0])

result = []

for c in range (cols):
    temp = " "
    for r in range(rows):
        temp +=matrix[r][c]
    result.append(temp)

print ("vertical concanation: ",result)