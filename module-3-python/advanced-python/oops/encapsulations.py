# what is encapsulation ?

# encapsulation is used to wrap up data into single object i.e called encapsulations 

# data access by access specifier or access modifier or data visibility process

#  types of access specifier 

#   1) private 2) public 3) protected  



# public 

# class employee:
#     def __init__(self,name):
#         self.name=name  #public attributes 
#         # create a public method 
#     def display_emp(self):
#         print(self.name)

# obj=employee("brijesh")
# obj.display_emp() #accessible via public 
# print(obj.name) #accessible anywhere 




# private : access inside of class only 

# class employee:
#     def __init__(self,name):
#         # public attributes
#         self.name=name 
#     # public method 
#     def show_age(self,age):
#         print(age)
        
#     #private method 
#     def show_address(self):
#         print("Address is :",self.__address)
         
        
# obj=employee("brijesh")
# print(obj.name)   #accessible 
# obj.show_age(35); #accessible 
# obj.show_address() #not accessible due to private
# #print address
# print(obj.__address)   

        
        
        
# class employee:
#     def __init__(self,name):
#         # public attributes
#         self.name=name 
#     # public method 
#     def show_age(self,age):
#         print(age)
        
#     #private method 
#     def show_address(self):
#         print("Address is :",self.__address)
         
        
# obj=employee("brijesh")
# print(obj.name)   #accessible 
# obj.show_age(35); #accessible 
# obj.show_address() #not accessible due to private
#print address
# print(obj.__address)          

        
        
#protected 
# access by its one child class 
class employee:
    def __init__(self,name,age):
        # public attributes
        self.name=name 
        self.age=age 
# call a protected method 
class SubEmployeeDetails(employee):
    def show_age(self):
        print("Employee name is :",self.name)
        print("Employee age is :",self.age)


obj=SubEmployeeDetails("Brijesh sekhda",25)

obj.show_age()    
        

 