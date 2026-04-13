class employee:
    company_name = "ostad company"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_info(self):  #instance method
        print(f"EMP name : {self.name}\nsalary : {self.salary}")
    
    @classmethod
    def change_company_name(cls,name):
        cls.company_name = name   

ob1 = employee("rakib", 20000)
ob1.display_info()
ob1.change_company_name("zuma store house")
print(ob1.company_name)


#satic method :  

class school :
    school_name = "abc model high school"

    @staticmethod
    def claculate_grade(marks):
        if marks>=90:
            return 'A+'
        else:
            return 'F'
print(school.claculate_grade(45))
#access control method:
class employee:
    company_name = "ostad"
    def __init__(self,name,salary):
        self.name = name 
        self._salary = salary #private access korar underscore use kore 
    def get_salary(self,password):
        if password == "admin":
            print(self._salary)
        else:
            print("Invalid choice")
    def get_salary(self,password,salary):
        if password == "admin":
            self._salary = salary
            print(f"new salary: {self._salary}")
        else:
            print("invalid access")


ob1 = employee("rahim", 20000)
ob2 = employee("karim",10000)
ob1.get_salary("admin")
print(ob1._salary)










