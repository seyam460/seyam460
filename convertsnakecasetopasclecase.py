snake_str = input("enter a snake_case string: ")

words = snake_str.split('_')
pascal_case = " "

for word in words :
    pascle_case += word.capitalize()

print ("pascalcase: ",word)