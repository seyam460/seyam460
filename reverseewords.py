s = input("enter a sentence: ")

words = s.split()

reversed_words = words [::-1]

result = " ".join(reversed_words)
print ("reversed word string: ",result)