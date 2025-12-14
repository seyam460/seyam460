def in_trouble(j_angry, s_angry):
    if (j_angry and s_angry) or (not j_angry and not s_angry):
        return True
    else:
        return False
print(in_trouble(True, True))     
print(in_trouble(False, False))   
print(in_trouble(True, False))    
print(in_trouble(False, True))    
