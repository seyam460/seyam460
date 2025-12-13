string = input("enter a string: ")

vowels = {'a','e','i','o','u'}

if vowels.issubset(set(string)):
    print ("the string contains all vowels")

else :
    print ("the string does not contain all vowels")