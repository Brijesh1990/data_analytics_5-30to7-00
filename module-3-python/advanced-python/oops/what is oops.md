# what is oops in python ? 
  1. oops stands for object oriented programming structured language
  2. oops used in advanced python 
  3. oops basically used inn web developement using python with django oops
  4. oops provides some features in python
  
     types of oops features 

     1. class 
     2. object 
     3. inheritance 
     4. polymorphism 
     5. encapsulations 
     6. abstractions 


 **architectures of oops features**

 https://miro.medium.com/0*kPat5mwo2lVx7sqR

  

# what is class in oops ? 

  1. A class is an collection of an object 
  2. A class is an blue print of an object in oops i.e called class 
  3. class is always defined in python with class keyword

  **syntax of class**
  ```
  class A:
   # defined an attributes of class
   name="brijesh"
   #create an constructor 
   def __init__(self,fname,age):
     self.fname=fname # instance attributes
     self.age=age   # instance attributes

  #creating an object of class 
  obj=A("Brijesh",35)
  print(obj.name)
  print(obj.age)   

   ```  
     

# what is object in python in oops ?
 
  1. An object is an instances of class
  2. An object is an examples of class 

  **syntax**

  ```
  class Pet 
    def __init__(result,name,age):
      result.name=name
      result.age=age
  
  obj=Pet("puppy",5)
  print(obj.name)
  print(obj,age)

  ```

# what is constructor in python ?
 
  1. A constructor is same name of the class 
  2. A constructor called inside of python __init__
  3. A constructor automatically called when we create an object of class 
  4. __init__ is an method of constructor
  5. its calls when object is created of class 

     **examples of constructor**

     ```
     class Pet: 
      def __init__(self,name,age):
        self.name=name
        self.age=age

    obj=Pet("puppy",5) # obj=Pet("puppy",5)
    print(obj.name)
    print(obj.age)
    
    ``` 

# what is self in oops ?

  1. self is used to stored a current object 
  2. self is used to called the method of class 
  3. self is not reserved keyword it will be changed name self=result just like parameter or arguments of function

  **examples of self**

  ```
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

  ```

# what is inheritance in python ?

  1. inheritance is used to inherit one class properties by another class i.e called inheritance 

  2. inheritance is used to access parent class properties by its child class i.e called inheritance 

   A => B 

   parent => child 

 **types of inheritance**

 1. single inheritance 

   ![alt text](image.png)


 2. multilevel inheritance 

 ![alt text](image-1.png)

 3. multiple inheritance (support in python)

 ![alt text](image-2.png)

