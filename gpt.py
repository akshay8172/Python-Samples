"""#Creating the class
class Book:
    def __init__(self,title,author,published_year):
        self.title = title
        self.author = author
        self.published_year = published_year
        
#Creating the method
    def display_info(self):
        printing = f'''
        Title  : {self.title}
        Author : {self.author}
        Published Year :{self.published_year}
        '''
        print(printing)
        
# Creating Instances of the class Book

Book1 = Book("Atomic Habits","James",2008)
Book2 = Book("Cracking the coding interview","Coders",2010)

#Calling the method.

Book1.display_info()            
    
    
#Creating the class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        perimeter = (self.length + self.width) * 2
        return perimeter

    def display_info(self):
        area = self.calculate_area()  # Call the method to get the area
        perimeter = self.calculate_perimeter()  # Call the method to get the perimeter

        printing = f'''
        Information about the rectangle:
        LENGTH:     {self.length}
        WIDTH:      {self.width}
        AREA:       {area}
        PERIMETER:  {perimeter}
        '''
        print(printing)

# Create an instance of the Rectangle class and accepting the values form the user.
length = int(input("Enter the length :"))
width = int(input("Enter the width :"))
rectangle = Rectangle(length, width)


# Call the methods and display information
rectangle.display_info()



#Creating class Car
class Car:
    def __init__(self,make,model,year,mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        
    def display_info(self):
        printing = f'''
        Details of the car :
        Car maker : {self.make}
        Car model : {self.model}
        Year      : {self.year}
        Mileage   : {self.mileage}
        '''
        print(printing)
        
    def update_mileage(self):
        newMileage = int(input("Enter the new mileage..."))
        self.mileage = newMileage
        print("Mileage updated")
               
       
#Creating instances....

car1 = Car("Toyota","Camry",2022,15000)

car1.display_info()         #Display information about the car
car1.update_mileage()       #Update the mileage
car1.display_info()         #Display the updated information
 
   
            
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def display_info(self):
        information = f'''
        Information about the bank account.
        Account holder's name: {self.account_holder}
        Balance: {self.balance}'''
        print(information)
        
    def deposit(self):
        print("Deposit Money")
        deposit_amount = float(input('How much do you want to deposit? '))
        self.balance += deposit_amount
        print(f'New balance is {self.balance}')
    
    def withdraw(self):
        print("Withdraw money")
        withdraw_amount = float(input('How much do you want to withdraw? '))
        if withdraw_amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= withdraw_amount
            print("Please collect the cash.")
            print(f'New balance is {self.balance}')
            
# Creating an instance
customer1 = BankAccount("John Doe", 1000)

# Display information about the account
customer1.display_info()

# Deposit and display updated information
customer1.deposit()

# Withdraw and display updated information
customer1.withdraw()

customer1.display_info()

#Creating the class
class Student:
    def __init__(self,name,age,grade):
        self.name  = name
        self.age   = age
        self.grade = grade
        
    def display_info(self):
        printing = f'''
        Information about the student
        NAME    :{self.name}
        AGE     :{self.age}
        GRADE   :{self.grade}
        '''
        print(printing)
        
    def promote(self):
        self.grade += 1

#Creating the object
student1 = Student("Alice",15,9)

#Calling the method

#Method to display the information about the students.
student1.display_info()
#Method to promote the student from the initial classs to next class
student1.promote()
#Method to view the updated student information
student1.display_info()
        

#Creating the class
class Library:
    def __init__(self , name , books):
        self.name = name
        self.books = books
        
#Creating the methods      
    def display_info(self):
        print(f"Library information of {self.name}")
        print("Available books")
        for books in self.books:
            print(f" * {books}")

#Method for creating new book.     
    def add_book(self):
        new_book = input("\nEnter the new book's name.")
        self.books.append(new_book)
        print(f"The book {new_book} is added.")
        
    def borrow_book(self):
        borrowing_book = input("\nEnter the book's name to borrow.")
        #Checking whether there are any copies left or not.
        if borrowing_book in self.books:
            self.books.remove(borrowing_book)
            print(f"You have selected the book {borrowing_book}.")
        else:
            print(f"Sorry the book {borrowing_book} is not available.")
       
#Creating the instance of Library class.     
city_library = Library("City Library",["Atomic habits","Cracking the coding interview","DSA with Java","python programming","C programming"])
  
#Initial list 
city_library.display_info()

#Add new book to the library
city_library.add_book()

#Check the new book is added or not.So call again display_info()
city_library.display_info()

#Borow a book form the library
city_library.borrow_book()
        
#Update the new list.
city_library.display_info()"""

class ShoppingCart:
    def __init__(self,items,total):
        self.items = items
        self.total = total
        
    def display_cart(self):
        printing = f'''
        Shopping cart 
        -------------------
        ITEMS       : {self.items}
        TOTAL       : {self.total}
        '''
        print(printing)
        
    def add_item(self):
        item_name = input("Please enter item name :")
        price = int(input("Enter the price :"))
        self.items.append(item_name)
        self.total += price
        print("Item added")
        
    def remove_item(self):
        remove_item_name = input("Enter the item name to remove :")
        if remove_item_name in self.items:
            self.items.remove(remove_item_name)
            print("Item deleted...")
        else:
            print('This item does not exist !!!')
            
cart1 = ShoppingCart(["Rice","Soap","Laptop","Mobile"],150000)

cart1.display_cart()

cart1.add_item()  

cart1.display_cart() 

cart1.remove_item()     

cart1.display_cart()        
        
        
        
        
    
    
    

        
        
        
        
        
        
        
        
        
        
