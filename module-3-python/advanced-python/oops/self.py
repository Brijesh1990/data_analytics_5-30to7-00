class A:
   # defined an attributes of class
   name="brijesh"
   #create an constructor 
   def __init__(self,fname,age):
     self.fname=fname # instance attributes
     self.age=age   # instance attributes

#creating an object of class 
obj=A("Brijesh",35) # obj=A("Brijesh",35) it is a object of class A
print(obj.name)
print(obj.age)   