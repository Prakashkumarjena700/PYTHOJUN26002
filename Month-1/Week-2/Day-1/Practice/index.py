# Make an object class/

class Car:
    cat = "SUV"
    color = "red"
    wheel = 4
    
car1 = Car()
car2 = Car()
car3 = Car()
car4 = Car()

print(car1.cat)     
print(car1.color)     

# Methods

class Student():
    name = "Rahul"
    age = 14
    
    def studentDetails(self):
        print("Student name is", self.name , "Age is ", self.age )
        
    def viewInput(self, address, roll):
        print("This is the address",address, "This is the roll", roll )
            
        
s1=Student()
s1.studentDetails()
s1.viewInput("Bhubaneswar", 40)

print(s1.age)
        
        
# constructor

class Citizen:
    country = "India"
    def __init__(self, aadhar, phone, name):
        self.aadhar = aadhar
        self.phone = phone
        self.name = name
        
    def printCitizen(self):
        print("Aadhar -" , self.aadhar)    
        print("Phone -" , self.phone)    
        print("Name -" , self.name)    
        print("Country -" , self.country)    
        
c1 = Citizen("12123222", "91182912829", "Prakash") 
c2 = Citizen("2346234823", "7817287287", "Rohan") 
c3 = Citizen("1823471892791", "5616271726", "XYZ") 

c2.printCitizen()  
 
 
class Building:
    country = "India"
    
    def __init__(self):
        self.location = input("Enter Location : ") 
        self.pin = input("Enter pincode : ")
        self.floor = input("Enter floor count : ")
        self.roomsInFloor = input("Enter room in each floor : ")
       
    def DisplyBuild(self):
        print("The building has ", self.floor, "floor")    
        
                

building1 = Building()

building1.DisplyBuild() 