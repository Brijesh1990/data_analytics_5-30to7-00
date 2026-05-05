# when we access multilevel inheritance like A=> B => C => D 

class animal:
    def __init__(self, name):
        self.name=name 
        
    def info(self):
        print("Animal name is :",self.name)
        
class Dog(animal):
    def speak(self):
        print(self.name,"dogs is barks") 
       
       
class Owner(Dog):
    def ownerName(self):
        print(self.name,"Owner Name is :Brijesh") 
               
obj=Owner("Tiger")
# inherited method 
obj.info()
obj.speak()
obj.ownerName()
            
            
            
            
        