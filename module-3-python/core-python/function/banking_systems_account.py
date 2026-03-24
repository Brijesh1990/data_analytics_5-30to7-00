def bank():
    pin=int(input("Enter your account pincode :"))
    if pin==3202:
        global ammount
        ammount=60000
        print("Welcome to : Brijesh Kumar Pandey" + "\n" + "Account numbers is :45681546541541" + "\n" + "Branch name is : SBI 150 feet ring road:" + "\n" + "Total balance is : 60000")
        print("Enter 1 for balance" + "\n" + "Enter 2 for withdraw")    
        num=int(input("Enter your choice for banking :"))
        
        if num==1:
            print(ammount)
     
        elif num==2:
            withammount=int(input("Enter your withdral ammount :"))
            finalbalance=ammount-withammount
            print("Your remaning ammount after withdrwal :",finalbalance)
               
        
    else:
        print("Your account pin code is wrong try again")
    
bank()
    
    