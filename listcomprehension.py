li = ["apple","banana","orange"]

fruits = [fruits.capitalize() for fruits in li]
print(fruits)

li_len = [len(x) for x in li]
print(li_len)

cube_list = [x*x*x for x in range(1, 11) if x % 2 == 1 ]
print(cube_list)

square_list = [x*x for x in range (1, 11) if x%2 == 1]
print(square_list)

even_number = [x for x in range(1, 100) if x % 2 == 0]
print(even_number)

li = [(1, 'one'), (2, 'two'), (3, 'three')]
dt = {k:v for k, v in li}
print(dt)
dt= {v:k for k, v in li}
print(dt)

s = 'abcfshgjkllhh'
unique_letters ={c for c in s }
print(unique_letters)

colors_choice = [{'meesi','blue'}, {'ronaldo','green'}, {'mbappe','orange'}]
colors_dt = {name: color for name,color in colors_choice}
print(colors_dt)

colors_set = {color for color in colors_dt.values()}
print(colors_set)



odd_number = [x for x in range(1, 100) if x % 2 != 0]
print(odd_number)

fp = open('myfile.txt', 'w')

fp.write("this is a test file")

fp.close()

def f():
      pass 
      
      print (type(f))

class car:
      make = 'toyota' 
      def move() :
            print("the car is moving")

print (car.make)
car.move()

x = car
print (car)
print(type(x))


class fraction:
      def __init__(self,n ,d):
            self.numerator = n
            self.denominator = d



#user_input = input("what is your name?")
#a = "Good morning, {}. How are you?".format(user_input)
#print(user_input)
#print (a)

 # string ar uses:
age = 31
f_name = "IKram"
l_name = "Khan"
txt = "I am {f_name} {l_name}. I am {age} years old".format(l_name = l_name , f_name = f_name , age= age)
txt2 = f"I am {f_name} {l_name}. I am {age} years old"

print(txt2)

# math function :

import math 
x = 4.5 
y = 4.1
print(math.ceil(x)) # upore sob cheye kacher purno number 
print(math.ceil(y))

a = 4.5
b = 0.004
print(math.floor(a)) # nciher dikhe sob cheye kacher purno number 
print(math.floor(b))

#round number:
# 3.1 - 3.49 --> floor hoye jabe = 3
# 3.51 - 3.99 --> ceil hoye jabe = 4
tax = 420.35
print(round(tax))
tax2 = 420.56
print(round(tax2))


#conditional statement :
#ekta equal thakleh holo assignment operator 
#2 ta equal thakleh comparison bujhay 

#indentation: iteration basically holo print er aghe compiler 3 ta space create kore niche nije nije 
rain = 10
if rain == 1:
     print ("i will go to school today")
else :
      print("i will not to go school today")    

a = 10 
if a % 2 == 0:
      print ("the number is even")
else :
      print("the number is odd")

x = 20
if x > 0 :
      print("the number is positive")
elif x < 0 :
      print ("the number is negetive")
else :
      print("the number is zero")


#s = "hello"
#print(list(s))
#print(s.append([1,2,3]))
#print(s.index(2))

li = ["apple", 1,2,3, "banana"]
print(li.reverse())

#tuple = immutable 

t= (1, 3 ,4)
t_r = tuple(reversed(t))
print (t)
print(t_r)

a = [1,2,3, "sakif", 5,6,7]
for i in a :
      if type(i) == type ('b'):
            break
      else :
            print (i)

for i in a :
      if type(i) == type('a'):
            continue
      else :
            print(i)


a = [10, 20, 40 ,79]

new_result = [i for i in a if i%2 == 0]
print(new_result)

a = [1,2 ,3 ,4, 5]
result = 0
i =0
n = len(a)
while i<n :
      result = result + a[i]
      i= i+1
print(result)

a = [-10, 20 ,30,-40,-50]

i = 0
while i<len(a):
      if a[i]<0:
            a[i] = 0
      i = i+1

print(a)

#set{} -->unordered --> indexing kore value pawa jabe na 
#immutable --> no update 
# no duplicates 

a = {1,2,3}
b = {3,2,6}
c = a.intersection(b)
d = a.union(b)
print(d)
print(c)

#dictionary{}
#key value pair 
#indexing ar sujogh naii 
#key gula immutable hote hobe 

a = {'rahim' : 12, 'karim': 14, 'jobbar': 20}
print(type(a))
for i in a.values():
      print(i)
      print(a.keys(),a.values())

for k,v in a.items():
      print(f"key name: {k}, values{v}")

a = [1,8,9]
b = ["mango", "banana", "pineapple"]

print(list(zip(a,b))) #list thekee dictionary teh convert kore 2 ta list ka dictionary teh convert
print(dict(zip(a,b)))

#dictionary comprehension 

nums = list(range(0,10))

result = {i: "even" if i%2 == 0 else "odd" for i in nums}
print(result)

#guess the number game:

secret_number = 7
attempts = 0

while True :
      guess = int(input("guess the number in range(1-10): "))
      attempts = attempts + 1 

      if guess == secret_number :
            print(f"you got it in {attempts} tries! ")
            break
      elif guess > secret_number:
            print("too high !! try again!")
      else :
            print("too low! try agian! ")

      

a = list(range(1,1001))
for i in a :
      if i%2 == 0:
            print(i)

#continue --> ignore koro 
#break --> loop thamai deoo 
for i in range(11):
      if i % 3 == 0:
            continue 
      else :
            print(i)

#list --> mutable(update or delete or add korteh pare)
a = [1,2,3, "rahim", 5.9,0]
a.append(102)
print(a)
#list ar moddhe jhode eksathe string and int data type thake taile sort kora jaii nhh
# 1 2 3 4 5 --> ascending --> choto theke boro hoyeche 
# 5 4 3 2 1 --> descending --> boro theke choto hocche 

a.remove(2)
print(a)

#tuple --> (immutable data structures)
#tuple list theke kichu ta fast kaj kore 


# set --> no indexing ,unordered , duplicate neoya jabe nhh 
#intersection --> common point 
#union --> all point print kore daeee 
#set ar moddhe aisob function kaj kore 

#dictionary --> key value pair thakbe 
#key ghula immutable hote hobe(string,tuple,int)


for i in range(1,6):
      for j in range(1,i+1):
            print(j, end = " ")

      print()

#find the first number divisible by both 7 and 5 between 1 to 100
for i in range(1,101):
      if i%5 == 0 and i%7 == 0:
            print(i)
            break


#function --> 2 types 
# 1.built in function --> already banano ache 
# 2. user defined function --> programmer nijer moto kore ekta function bananbe 

def my_first_name():
      a = 10
      b = 20 
      print(a+b)
my_first_name()

def add_two_numbers(c,d): # argument 
        print(c+d)
add_two_numbers(5,10)
add_two_numbers(2,8)  #parameters 

def multiply_two_numbers(e,f) :
         return e * f
result = multiply_two_numbers(12,2)
print(result)

def hello():
      return "hello how are you"
greetings = hello()
print(greetings)

def addition(a,b):
      result = sum(a,b)
      return result 

def addition(*args): #multiple parameters pass kore capture kore 
      print(args)
      return sum(args)
r = addition (12,10,2,7,5)
print(r)

def my_func(f_name, l_name,age):
      print(f"my name is {f_name} {l_name}. I am {age} years old")

my_func("rahim","khan",25)

#lambda function --> annonymous function --> unnanmed 
#lambda argument :expression --> likhar niyom 
square = lambda x: x*x
print(square(4))

add = lambda a,b : a+b
print (add(1,2))

students = [('rahim',50), ('karim', 44), ('fahim',65)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


#map
nums = [1,3,5,6,8]
#sq_nums = list(map(square korteh chacci, kar upor apply korteh chacci))
sq_nums = list(map(lambda x : x*x, nums))
print(sq_nums)

#filter 
even = list(filter(lambda x: x%2 == 0,nums))
print(even)

#reduce :
import functools 
sum = functools.reduce(lambda x,y: x+y, nums )
print(sum)

# scope --> a region where a variable is accessible 
# LEGB 
# l --> local
# E --> enclosing 
# G --> global 
# B --> built in scope 

n == 100 # global variable 
def outer():
      n = " "
      def inner():
            n = ""
            print(n)

      inner()
outer()

#file handling:
#file = open('name.txt', 'r')
#content = file.raed 
#print(content) 
#append method --> add kore content 
#import  os 
# error vs exceptions 

try: # je code e exception thakte pare 
      with open("rahim.txt", 'r') as f:
            print(f.read())
except FileNotFoundError:
      print("file not found")


def add_ten(n):
      m = n + 10
      return m
another_num = add_ten(50)
another_num1= add_ten(60)
print(another_num)
print(another_num1)

#error --> code run hobe 
#indentation , syntax, compile time error 

#Exception : 100 ta value 
# run time a error dekhai 

#try --> cesta kortechi (tar mane sekhane vul thakbe)
#except --> catch --> (error dhori)

try :
      with open('rahim.txt','r') as f:
            content = f.read

except Exception as e :
      print("some error occurred !!", e)


def check_file(filename):
      if not filename.endswith('.txt')

print("hello.txt".endswith("png"))


