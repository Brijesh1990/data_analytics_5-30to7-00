# when we access two or more than two parent class properties by its one child class i. e called multiple inheritance 

# note : python  support multiple  inheritance 

'''

A      B      C 


      D
                 
'''
# base class 1
class Mother:
    mothername=""
    def motherInfo(self):
        print(self.mothername)
# base class 2        
class Father:
    fathername=""
    def fatherInfo(self):
        print(self.fathername)        
  
#derived class  
class Son(Mother,Father):
    def Parent(self):
        print("Father name is  :",self.fathername)
        print("Mother name is :",self.mothername)
        
        
# create an object       
  
obj=Son()
obj.fathername="Dr Ravindra nath Pandey"
obj.mothername="Mrs Shashikala Pandey"
obj.Parent()        

            
            
            
            
        