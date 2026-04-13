student = {
    "name": "rakib",
    "age": 25,
    "course": "python"
}
print (student)

print (student["name"])
print (student["age"])

student["grade"] = "A"
student["nickname"]= "playboy+nazifa lover"
print (student)

for key,value in student.items():
    print(key,":",value)
