class Display1:
    def info(self, a, b):
        print(a)
        print(b)

class Display2(Display1):
    def info(self, a, b, c,d):   # overriding parent method
    
        print(a)
        print(b)
        print(c)
        print(d)
        # betwise operator
        a+=b 
        print(a)
        a*=b 
        print(a)
        

obj = Display2()
obj.info(10, 20, 30,40)
