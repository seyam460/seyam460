tuples_list = [(1,4,7),(2,7,9),(3,5,1)]

target = (2,7,5)
k = 1 
result = min (tuples_list, key=lambda x: abs(x[k] - target[k]))

print (result)