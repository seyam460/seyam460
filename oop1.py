#property-decorator
#class employee:
    #company_name = "ostad publications"

    #def __init__(self,name,salary):
        #self.name = name 
        #self._salary = salary

    #@property
    #def salary(self):
        #return self._salary
    #@salary.setter
    #def salary(self,new_salary):
        #self.salary = new_salary


#ob1 = employee("rahim",40000)
#print(ob1.salary)
#print(ob1.get_salary)
#ob1.salary = 50000
#print(ob1._salary)

# association , aggregetion and composition 

#class laptop:
    #def __init__(self,brand):
        #self.brand = brand
#class student:
    #def __init__(self,name):
       # self.name = name 
        #self.laptop = laptop 
    #def #show_laptop_info(self):
        #print(f"{self.name} has a laptop named {self.laptop}")

#lp1 = laptop("asus")
#student = student("rahim",lp1)
#student.show_laptop_info()

#agreegetion --> has a relationship 

#class department:
    #def __init__(self,name):
        #self.name = name 
#class university :
    #def __init__(self, name, departments):
        #self.name = name 
        #self.departments = departments 
    #def add_department(self , department):
         #self.departments.append(department)   
    #def show_departments(self):
        #return [department.name for department in self.departments]
#un1 = university("ABC")
#dep1 = department("programming")
#dep2 = department("math")
#un1.add_department(dep1)
#un1.add_department(dep2)
#print(un1.show_departments())

# 4 principal of oop:
#inheritance , abstraction , polymorphism , encapsulation

class grandfather :
    def __init__(self,color , first_name):
        self.color = color 
        self.first_name = first_name 
    def gf_method(self):
        print("I am from grandfather")

class father(grandfather):
    def __init__(self, hobby,color,first_name):
        super().__init__(color ,first_name)
        self.hobby = hobby
    def father_method(self):
        print("I am from Gfather")
    
class children (father , grandfather):
    def __init__(self, fashion):
        self.fashion = fashion

        
GF1 = grandfather("blue","chowdhury")
F1 = father("cricket", "red", "chowdhury")
print(F1.hobby)
print(F1.color)
print(F1.first_name)
c1 = children("test")
c1.gf_method()
c1.father_method()
print(c1.fashion)


#hierarchical:

class vehicle:
    def engine_type(self):
        print("Vehicle has an engine")
class car(vehicle):
    def num_doors(self):
        print("car has 4 doors")
class truck(vehicle):
    def load_capacity(self):
        print("truck can carry 10 tons")

car = car()
car.engine_type()
car.num_doors()
Truck = truck()
Truck.engine_type()
Truck.load_capacity()

#hybrid:
class shape:
    def area(self):
        print("calculating area ")
class polygon(shape):
    def sides(self):
        print("polygon has multiple sides")
class rectange(polygon):
    def __init__(self, length,breadth):
        self.length = length 
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
rec = rectange(10,5)
rec.sides()
print(rec.area())

# 2nd pillar(polymorphisom):
#poly --> multiple 
#morphisom --> form

#1.method overriding
class Grandfather:
    def greet(self):
        print("Grandfather says")

class father(Grandfather):
    def greet(self):
        print("father says")

class children(father):
    def greet(self):
        print("children says")

gf = Grandfather()
f = father()
c = children()

gf.greet()
f.greet()
c.greet()


#method overloading :

class shape:
    def area(self, a ,b = 10): # default value diteh hobe 
        return a*b
    
    
p = shape()
print(p.area(12))
print(p.area(12,10))


#design pattern --> singleton

class singleton :
    _instance = None  # class variable 

    def __new__(cls):
        if cls._instance is None :
            cls._instance = super(singleton,cls).__new__(cls)
            return cls._instance
ob1 = singleton()
ob2 = singleton()
print(ob1 is ob2)

#factory design pattern --> 

class car:
    def driver(self):
        return "driving car" 
class bike :
    def driver(self):
        return "riding a car"
class vehiclefactory:
    @staticmethod
    def get_vehicle(type):
        if type == "car":
            return car()
        elif type == "bike":
            return bike()
        else :
            return ValueError("unknown bike")
        
vehicle = vehiclefactory.get_vehicle("car")
print(vehicle.driver())

#builder design pattern -->

class computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu 
        self.ram = ram 
        self.storage = storage 
    def __str__(self):
        return f"computer with {self.cpu} CPU, {self.ram} RAM, {self.storage} STORAGE."

    
class computerbuilder:
    def __init__(self):
        self.cpu = None 
        self.ram = None 
        self.storage = None 
    def set_cpu(self,cpu ):
        self.cpu = cpu
        return self
    def set_ram(self, ram):
        self.ram = ram
        return self
    def set_storage(self, storage):
        self.storage = storage 
        return self
    def build(self):
        return computer(self.cpu, self.ram , self.storage)

builder = computerbuilder()
computer = builder.set_cpu("Intel i9").set_ram("32Gb").set_storage("1TB SSD").build()
print(computer)

class calcualtor:
    def add(self, a , b):
        return a+b
    def multiply(self , a , b):
        return a * b
    
calc = calcualtor()
print(calc.add(5 , 3))
print(calc.multiply(4 , 7))

class person:
    def __init__(self , name , age , bf):
        self.name = name 
        self.age = age 
        self.bf = bf
    def celebrtiy_brithday(self):
        self.age += 1
        print(f"Happy brithday {self.name}! I am your {self.bf} boyfd!! many many happy returns of the day !!Tou are now {self.age}")

p1 = person("zuma", 20 , 'saha***')
p1.celebrtiy_brithday()
p1.celebrtiy_brithday()



class playlist:
    def __init__(self , name):
        self.name = name
        self.songs = []
    def add_song(self , song):
        self.songs.append(song)
        print(f"added : {song}")
    def remove_song(self , song):
        if song in self.songs:
            self.songs.remove(self , song)
            print(f"Removed: {song}")
    def show_songs(self):
        print(f"Playlist {self.name} :")
        for song in self.songs:
            print(f"- {song}")

my_Playlist = playlist('Favourites')
my_Playlist.add_song("Bhojphuri")
my_Playlist.add_song("Bolo Naa")
my_Playlist.show_songs()

class car:
    def __init__(self , brand , model):
        self.barmd = brand 
        self.model = model
    def move(self):
        print("Drive!")
class boat:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
    def move(self):
        print("sail!")
class plane:
        def __init__(self , brand , model):
            self.brand = brand 
            self.model = model
        def move(self):
            print("Fly!")

car1 = car("Ford" , "Mustang")
boat1 = boat("Ibiza" , "Touring 20")
plane1 = plane("Boeing" , "747")
for x in(car1 , boat1 , plane1):
    x.move()

  
class person:
    def __init__(self , name, age):
        self.name = name 
        self._age = age
    def get_age(self):
        return self._age 
    def set_age(self , age):
        if age > 0 :
            self._age = age
        else:
            print("Age must be positive")

p1 = person("tobias" , 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age)


class student:
    def __init__(self , name):
        self.name = name 
        self._grade = 0
    def set_grade(self , grade):
        if 0 <= grade <= 100:
            self._garde = grade 
        else:
            print("garde must be between 0 and 100")
    def get_grade(self):
        return self._grade 
    def get_status(self):
        if self._grade >= 60:
            return "passed"
        else:
            return "failed"
student = student("emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

class outer:
    def __init__(self):
        self.name = "outer class"
class Inner:
    def __init__(self):
        self.name = "Inner class"
    def display(self):
        print("This is the inner class")
Outer = outer()
print(Outer.name)

#class car:
    #def __init__(self , brand , model):
        #self.brand = brand 
        #self.model = model
        #self.engine = self.Engine()

#class engine:
    #def __init__(self):
        #self.status = "off"
    #def start(self):
        #self.status = "Running"
        # print("Engine started")
    #def stop(self):
       # self.status = "off"
        #print("Engine stopped")
    #def drive(self):
       # if self.engine.status == "Running":
          #  print(f"Driving the {self.brand} {self.model}")
     #   else:
         #   print("start the emgine firts!")
#Car = car("Toyota" , "corolla")
#Car.drive()
#Car.engine.start()
#Car.driven()

#random practive (modules):

#import random 
#help(random)
#print(dir(random))

#collections module :

#import collections

#print(collections.__doc__)





    
      
        
    
    




        
    











        