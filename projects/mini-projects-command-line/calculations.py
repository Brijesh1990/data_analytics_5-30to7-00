# print on command line instructions 
print("""\n
      
      select 1 for add
      select 2 for substract
      select 3 for multiplications
      select 4 for divisions 
      select 5 for modulas 
      select 6 for exit from programmes
      
      """)

# create a function additons 
def add(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a+b 
    print("Additions of numbers is :",c)
def subs(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a-b 
    print("Substractions of numbers is :",c)
def mult(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a*b 
    print("Multiplications of numbers is :",c)
def dv(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a/b 
    print("Divisions of numbers is :",c)
def mod(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a%b 
    print("Modulas  of numbers is :",c)
    
# create loop for executions 

while True:
    choice=int(input("Enter your choices : "))
    if choice==1:
        add("a","b")
    elif choice==2:
        subs("a","b")
    elif choice==3:
        mult("a","b")
    elif choice==4:
        dv("a","b")
    elif choice==5:
        mod("a","b")
    else:
        print("wrong choice selected try again")
        break
        
        