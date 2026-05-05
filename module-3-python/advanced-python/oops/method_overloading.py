# method overloading 
# method overload is performed any operation using same function pass with different arguments there we used method overload. 
class Display1:
    def info(self, a=None, b=None, c=None):
        if a is not None:
            print(a)
        if b is not None:
            print(b)
        if c is not None:
            print(c)

class Display2(Display1):
    pass

obj = Display2()
obj.info(10, 20, 30)
        
        
   
