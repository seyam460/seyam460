import datetime 

today = datetime.datetime.today()
print(today)

import math

x= math.sqrt(100)
print(x)

pi = math.pi
print(pi)

fruits = ["apple","banana","orange","mango"]
for fruit in fruits:
    print(fruits)

for i in range(4):
    print(i, fruits[i])

s = 'abcd'
type(s)

'bangladesh'
print('bangladesh' *2) 

print(len('bangladesh'))

name = 'rakib'
name = name.upper()
print(name)

name1 = name.lower()
print(name1)

name2 = name.capitalize()
print(name2)

s= 'bangladesh'
print(s.find('bangla'))

country = 'canada'
print(country.startswith("cana"))

print(country.endswith('da'))

i = 1
while i <=10:
    print(i)
    i= i+1