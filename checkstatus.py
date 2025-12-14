def check_status(a, b, flag):
    if not flag:
        return (a >= 0 and b < 0) or (a < 0 and b >= 0)
    else:
        return a < 0 and b < 0
print (check_status(5,-3,False))
print (check_status(-2,-4,True))
print (check_status(3,4,False))