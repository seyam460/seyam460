String = input("enter a string: ")

words = String.split()

for word in words:
    if len(word) % 2 == 0:
        print (word)