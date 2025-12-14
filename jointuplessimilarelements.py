data = [(1,2),(2,3),(3,6),(6,7),(7,8)]

result_dict = {}

for t in data :
    key = t[0]
    if key not in result_dict:
        result_dict[key] = []
    result_dict[key].extend(t[1:])

result = [(k, *v) for k,v in result_dict.items()]

print (result)