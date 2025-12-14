def neg(n):
    for i in range(n,1):
        print (i) 

def pos(n):
    for i in range (n-1,-1,-1):
        print (i)

n = int(input("enter a number: "))

if n<0:
    neg(n)
elif n>0:
    pos(n)
else :
    print(0)