# inheritance is used to access parent class properties by its child class i.e called inheritance 

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
            
        