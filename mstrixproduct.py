a =[[1,4,5],[7,3],[4],[46,7,3]]

product = 1
for row in a: 
    for num in row:
        product *= num

print ("product: ",product)
