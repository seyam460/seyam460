with open ("example.html", "r") as file :   # creating a file object and opening the file in read mode
    content = file.read()
    print(content)


with open ("example.html", "w") as file :  # creating a file object and opening the file in write mode
    file.write ("this is my first code in Django and i am a software developer working in daffodil international university")


import os
os.rename ("example.html", "new_example.html")  # renaming the file from example.html to new_example.html



# error Handling :
try :
    with open ("non_existent_file.txt", "r") as file :
        content = file.read()
        print(content)
except FileNotFoundError :
    print("The file does not exist. Please check the file name and try again.")

