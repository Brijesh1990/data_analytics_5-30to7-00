# abstract class 
# abstract class not accessible directly 
# abstract class never create its object 
# abstraction will access by another class object
from abc import ABC,abstractmethod
class Greet:
    @abstractmethod
    def say_hello(self):
        pass #abstract method
 
class English(Greet):
    def say_hello(self):
        return "Hello"
    
obj=English()
print(obj.say_hello()) 
