special_chars = "!@#$%^&*()@#%^?><:;|"

string = input ("enter a string: ")

valid = True

for ch in string :
    if ch in special_chars:
        valid = False 
        break 

if valid :
    print ("string accepted")

else :
    print ("string contains special characters and is rejected")