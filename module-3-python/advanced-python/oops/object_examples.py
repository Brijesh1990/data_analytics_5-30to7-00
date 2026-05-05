class  Dog:
    # object is an instances of class 
    # object is an examples of class 
     name="Tiger"  # instance of attributes 
     
     def __init__(self,fname,age,owner): # constructor method 
         self.fname=fname
         self.age=age 
         self.owner=owner 
         
# create an object of class 

obj=Dog("puppy",5,"Brijesh")

# obj=Dog("puppy",5,"Brijesh") this is an object of class Dog
# print(obj.fname)
# print(obj.age)
# print(obj.owner)
          
print(obj.name)
print(obj.age)
print(obj.owner)
                    