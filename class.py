#   class Cars:                 #class 
#       name                    #Property
#       price                   #Property
#       colour                  #Property
#               
#       start()                 #Method
#           
#   car1 = "Tata Tiago"         #Object
#   car2 = "Tata Nexon"         #Object



'''class Cars:
    def __init__(self,name,price,colour):
        self.name   = name
        self.price  = price
        self.colour = colour
        
    def start(self):
        print(f"{self.name} Engine Started")
        
        
car1 = Cars("Tiago",600000,"white")
car2 = Cars("Nexon",1200000,"Grey")
print(f"Our Car {car1.name}, which cost {car1.price}, and it's colour is {car1.colour}")
print(f"Our neighbour's car {car2.name}, Which cost {car2.price}, and it's colour is {car2.colour}")

car1.start()'''


class Person:                                           #class 
    def __init__(self, first_name, last_name,age):      #Initialization
        self.first_name = first_name                    #Attribute
        self.last_name = last_name                      #Attribute
        self.age = age                                  #Attribute
        
    def hello(self):                                    #Method
        print(f"Hello my name is {self.first_name} and my last name is {self.last_name} and I'm {self.age} years old")
        
#Creating Objects(Instances)

person1 = Person("Akshay","Babu",21)                    #Instance
person2 = Person("Shonith","Krishna",22)                #Instance
person1.hello()                                         #Calling the method
person2.hello()                                         #Calling the method 
        
print(person1.age)


