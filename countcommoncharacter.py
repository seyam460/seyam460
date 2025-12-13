S1= input ("enter the 1st string: ").lower()
S2 = input ("enter the 2nd string: ").lower()
set1 = set(S1)
set2 = set(S2)

common_chars = set1.intersection(set2)

print ("common characters: ",common_chars)
print ("count: ",len(common_chars))