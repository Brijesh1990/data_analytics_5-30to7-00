print("select 1 for additions 2 for substraction")
a=int(input('Enter a numbers :'))
b=int(input('Enter b numbers : '))
res=int(input('select numbers to performed'))
if res==1:
    c=a+b 
    print("additions of numbers is :",c)
    
elif res==2:
    c=a-b 
    print("subtractions of numbers is :",c)

else:
    print('wrong result numbers selected :')         
