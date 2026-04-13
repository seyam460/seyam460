# car class banabo ,setar kichu object banabo
#brand ,model,color

class Car:
    def __init__(self): #self hocche ei car class ar object ke indicate kore 
            self.brand = " " 
            self.model = " "

car1 = Car()
car1.brand = "toyota"
car1.model= "corolla"
print(car1.brand)
print(car1.model)

#init function --> dunder method because of double underscore, constructor --> no return
#constructor -->
#1. default constructor
#2.parameterized constructor
#3. default value constructor 

class Car:
      def __init__(self,model,brand):
            self.model = model
            self.brand = brand
           

car2 = Car("honda", "corolla")
print(car2.brand, car2.model)


class Car:
      def __init__(self, model = "civic", brand = "corolla"):
            self.model = model
            self.brand = brand 
car3 = Car()
print(car3.model, car3.brand)

         def display_info(self):
            print(f"car brand:{self.brand}\n car model: {self.model}")
            car1 = Car
            car2 = Car
            


class school :
      school_name = "ostad high school"  #class variable


      def __init__(self,name):
            self.school.name = name

scl = school("rahim")
print(scl.school_name)

