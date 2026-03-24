def clc():
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    print('select 1,2,3,4 for performed actions')
    num=int(input("Select numbers :"))
    if num==1:
        c=a+b 
        print("Additions of numbers is :",c)
    elif num==2:
        c=a-b 
        print("Substractions of numbers is :",c)
    elif num==3:
        c=a*b 
        print("Multiplications of numbers is :",c)
    elif num==4:
        c=a/b 
        print("Divisions of numbers is :",c)
    else:
        print('you are provides invalid numbers please check again')
clc()
        
    