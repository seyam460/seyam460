import re

def validate_password(s):
    pattern = r'^[a-z]+[!@#$%]+[0-9]+$'
    
    if re.match(pattern, s):
        return True
    else:
        return False

print(validate_password("abc@123"))     
print(validate_password("a!9"))         
print(validate_password("Abc@123"))     
print(validate_password("abc123"))      
print(validate_password("abc@"))        
print(validate_password("@abc123"))     
