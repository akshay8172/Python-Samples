"""#parent class vehicle
class Vehicle:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        self.fuel = 0
    
    def start(self):
        print(f"\nThe {self.brand} {self.model} is started")
        
    def refuel(self):
        print(f"\nRefuel the vehicle {self.model}")
        petrol = int(input("\nHow much Ltr ? : "))
        self.fuel += petrol
        print(f"\n{self.model} is refuled with {petrol} ltr. Total fuel available is {self.fuel} ltr")
        
#Derived class 1 - CAR

class Car(Vehicle):
    def __init__(self,brand,model,tyres):
        # Call the constructor of vehicle class
        super().__init__(brand,model)
        self.tyres = tyres
    
    def horn(self):
        print(f"\nHorn Blowed by {self.model}")
        
#Derived class 2 - Bike

class Bike(Vehicle):
    def __init__(self,brand,model,power):
        #Call the constructor of the vehicle class
        super().__init__(brand,model)
        self.power = power
        
    def wheelie(self):
        print("\nHe can do wheelie")
        
#Creating instances.
car = Car("Tata","Tiago",4)
bike = Bike("Tvs","Raider",11)

car.start()
car.horn()
car.refuel()

bike.start()
bike.wheelie()
bike.refuel()

#Creating parent class Employee
class Employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
    def display_info(self):
        printing = f'''
        NAME : {self.name}
        EMPLOYEE_ID : {self.employee_id}
        '''
        print(printing)
        
# Derieved class 1 : MANAGER

class Manager(Employee):
    def __init__(self,name,employee_id,department):
        super().__init__(name,employee_id)
        self.department = department
        
    def manage_team(self):
        print(f"{self.name} is managing the {self.department} team.")
        
# Derieved class 2 : Developer

class Developer(Employee):
    def __init__(self,name,employee_id,domain):
        super().__init__(name,employee_id)
        self.domain = domain
        
    def working_domain(self):
        print(f"{self.name} is working in {self.domain}") 
        
#Creating instances.

manager = Manager("Ajith","M1","Sales")
developer = Developer("Akshay","D1","Back_end")


manager.display_info()
developer.display_info()

manager.manage_team()
developer.working_domain()

#create two derived classes, "Car" and "Bicycle", which inherit from the "Vehicle" class.
# Each derived class should have specific attributes and methods, such as "num_doors" and "trunk_capacity" for a car,
# "num_gears" and "ride" for a bicycle. 
# Illustrate how inheritance can be used to model different types of vehicles in a transportation system efficiently.

class Vehicle:
    def __init__(self,brand,model,color,fuel_type,fuel_level,year,mileage):
        self.brand = brand
        self.model = model
        self.color= color
        self.fuel_type = fuel_type
        self.fuel_level = fuel_level
        self.year = year
        self.mileage = mileage
    def display_info(self):
        info = f'''
    About Vehicle
    BRAND       : {self.brand}
    MODEL       : {self.model}
    COLOR       : {self.color}
    FUEL TYPE   : {self.fuel_type}
    FUEL LEVEL  : {self.fuel_level}
    YEAR        : {self.year}
    MILEAGE     : {self.mileage}
    '''
        print(info)
    
#Derived class 1 - CAR
class Car(Vehicle):
    def __init__(self,brand,model,color,fuel_type,fuel_level,year,mileage,num_doors,trunk_capacity):
        super().__init__(brand,model,color,fuel_type,fuel_level,year,mileage)
        self.num_doors = num_doors
        self.trunk_capacity = trunk_capacity
    def start(self):
        print(f"{self.model}'s engine is started\n Available Fuel : {self.fuel_level}")
    def open_trunk(self):
        print(f"The Trunk capacity is {self.trunk_capacity} and is opened.")
    def close_trunk(self):
        print(f"The Trunk is closed")
        
#Derived class 2 - 
class Bike(Vehicle):
    def __init__(self,brand,model,color,fuel_type,fuel_level,year,mileage,num_gears,ride):
        super().__init__(brand,model,color,fuel_type,fuel_level,year,mileage)
        self.num_gear = num_gears
        self.ride = ride
    def ring_bell(self):
        print("Ringing the bike's bell...")
    def adjust_gears(self,new_gear):
        gear = 1
        self.num_gear = new_gear
        if new_gear < gear:
            print("Up the gear please")
        else:
            gear += new_gear
            print(f"Gear changed to {gear}")
    def apply_brakes(self):
        print("Brake applied")
 
# Creating instances       
car = Car("Tata","Tiago","White","Petrol",10,2021,15,4,240)
bike = Bike("TVS","Raider","Black","petrol",2,2022,60,5,120)

car.display_info()
car.start()
car.open_trunk()
car.close_trunk()

bike.display_info()
bike.ring_bell()
bike.adjust_gears(3)
bike.apply_brakes()



#Imagine a scenario where you have a base class 'Person' representing individuals with common attributes like 'name' and 'age'. 
# Create two derived classes, 'Student' and 'Teacher', which inherit from the 'Person' class. Each derived class should have specific attributes and methods:
#For the Student class, include attributes like 'student_id' and 'grade'. Implement a method called 'study' that simulates the student studying.
#For the Teacher class, include attributes like 'employee_id' and 'subject'. Implement a method called 'teach' that simulates the teacher giving a lecture.
#Create instances of both Student and Teacher and demonstrate how inheritance allows you to model different roles in an educational setting efficiently.

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"\nName: {self.name}\nAge: {self.age}")

# Derived class - Student
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        print(f"\nStudent Info:\nName: {self.name}\nAge: {self.age}\nStudent ID: {self.student_id}\nGrade: {self.grade}")

    def study(self):
        print(f"Student {self.name} has passed the exam with a grade of {self.grade}")

# Derived class - Teacher
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def display_info(self):
        print(f"\nTeacher Info:\nName: {self.name}\nAge: {self.age}\nEmployee ID: {self.employee_id}\nSubject: {self.subject}")

    def teach(self):
        print(f"Teacher {self.name} is teaching {self.subject}")

# Creating instances for student class
student1 = Student("Akshay", 21, 40, "B")

# Creating instances for teacher class
teacher1 = Teacher("Rasheed", 36, 1, "Python")

# Calling the overridden display_info method for student1
student1.display_info()  # This will only execute the version in the Student class

# Calling the overridden display_info method for teacher1
teacher1.display_info()  # This will only execute the version in the Teacher class 

#Parent class 
class Product:
    def __init__(self , name , price , quantity_in_stock):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        
    def display_info(self):
        info = f'''
Product Details.
NAME                : {self.name}
PRICE               : {self.price}
quantity_in_stock   : {self.quantity_in_stock}   
'''
        print(info)

#Derived class 1 :Electronics
class Electronics(Product):
    def __init__(self , name , price , brand , warranty_period , quantity_in_stock):
        super().__init__(name , price , quantity_in_stock)
        self.brand = brand
        self.warranty_period = warranty_period
    #Override the display_info method
    def display_info(self):
        info = f'''
Product Details.
--------------------
NAME                : {self.name}
PRICE               : {self.price}
BRAND               : {self.brand}
WARRANTY PERIOD     : {self.warranty_period}
'''
        print(info)
        
#Derived class 2 :
class Clothing(Product):
    def __init__(self , name , price , size , material  , quantity_in_stock):
        super().__init__(name , price , quantity_in_stock)
        self.size = size
        self.material = material
        
    #Override the display_info method
    def display_info(self):
        info = f'''
Product Details 
---------------------
NAME           : {self.name}
PRICE          : {self.price}
SIZE           : {self.size}
MATERIAL       : {self.material}
'''
        print(info)
        
# Creating Instance for Product class    
laptop = Electronics("HP Elitebook",130000,"HP",1,True)
smartwatch = Electronics("Noise Colourfit pro",1199,"Noise",6,True)
shirt = Clothing("Allen Solly",1300,"Medium","cotton",True)
jeans = Clothing("killer",2000,"M","Hard",True)

#Calling The method
laptop.display_info()
smartwatch.display_info()

shirt.display_info()
jeans.display_info()
"""