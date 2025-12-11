def is_palindrome(s):
    return s == s[::-1]

text = input ("enter a string: ")

if is_palindrome(text):
    print("palindrome")
else:
    print ("not palindrome")
    