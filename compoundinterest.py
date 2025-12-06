p = int(input("enter principal amount: "))
r = int(input("rate of interest: "))
t = int(input("enter time in years: "))

Amt = p * ((1 + r / 100) ** t)  
CI = Amt - p
print("compound interest: ", CI)
