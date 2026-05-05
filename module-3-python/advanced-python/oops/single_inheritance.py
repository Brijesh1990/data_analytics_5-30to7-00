# when we access one parent class properties by its one child class i.e called single inheritance 

class animal:
    def __init__(self, name):
        self.name=name 
        
    def info(self):
        print("Animal name is :",self.name)
        
class Dog(animal):
    def speak(self):
        print(self.name,"dogs is barks") 
        
obj=Dog("Tiger")
# inherited method 
obj.info()
obj.speak()
            
            
            
            
        