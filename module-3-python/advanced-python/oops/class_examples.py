class  Dog:
     name="Tiger"  # instance of attributes 
     
     def __init__(self,fname,age,owner): # constructor method 
         self.fname=fname
         self.age=age 
         self.owner=owner 
         
# create an object of class 

obj=Dog("puppy",5,"Brijesh")
# print(obj.fname)
# print(obj.age)
# print(obj.owner)
          
print(obj.name)
print(obj.age)
print(obj.owner)
                    