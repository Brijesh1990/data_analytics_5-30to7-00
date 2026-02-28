# if : if is executed when condition is true 
'''

syntax 
if condition:
  statements

'''

# a=10
# b=20
# if a>b:
#     print("a is greater than b")

# check true

# a=40
# b=20
# if a>b:
#     print("a is greater than b")



# if - else: if is executed when condition is true if condition false else is executed

'''
syntax :

if condition:
 statements
 
else:
   statements
     
''' 

# age=10
# if age>=18:
#     print('i am adults')
# else:
#     print("i am child")

# short way to check if else (ternary operator)

# age=10
# result="adults" if age>=18 else "child"
# print(result) 


# mistakes in indent

# age=10
# if age>=18:
#     print('i am adults')
# else:
#     print("i am child")


# nested if : if within another if i.e called nested if 
'''
syntax :
if condition:
  if condition:
     statements
  else:
    statements
else:
  statements       
'''

# a=50
# b=20

# a,b=10,20
# if a>b:
#     if a!=0 and b!=0:
#         print('a is greater than b and both are positive numbers')
# else:
#     print('a is smaller than b')        


# num=-13
# if num>0:
#     if num%2==0:
#         print('positive even numbers')
#     else:
#         print('positive odd numbers')
    
# else:
#     print('negative numbers')    



# w.a.p to check odd or even numbers take input from users

# num=int(input('Enter a Numbers :'));
# if num>0:
#     if num%2==0:
#         print('positive even numbers')
#     else:
#         print('positive odd numbers')
    
# else:
#     print('negative numbers')    


# if elif : if executed when condition is true elif check multiple true condition if elif is false else is executed 

'''
syntax :
if condition:
   elif condition:
      statements;
   elif condition:
       statements;
   
else:
  statements;    
 
   
'''
# w.a.p to check both numbers are equals take input from users

# a=int(input('Enter a values :'))
# b=int(input('Enter b values :'))
  
# if a>b:
#     print('a is greater than b')
# elif b>a:
#     print('b is greater than a')
# else:
#     print('both are equal')
    
    
    
# w.a.p to check  max numbers amongs  three numbers input from users


# n1=int(input('Enter n1 values :'))
# n2=int(input('Enter n2 values :'))
# n3=int(input('Enter n3 values :'))
  
# if n1>n2 and n1>n3:
#     print('n1 is max numbers')
# elif n2>n3 and n2>n1:
#     print('n2 is max numbers')               
# elif n3>n2 and n3>n1:
#     print('n3 is max numbers')

# else:
#     print('something went wrong while checking max numbers among three numbers')
 


# w.a.p to check a years is leap years take input from users 

year=int(input("Enter a Year :"))

if year%4==0:
    print('this is a leap year')
else:
    print('this is not a leap year')    