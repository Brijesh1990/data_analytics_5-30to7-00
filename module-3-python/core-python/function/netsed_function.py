# function within another function 
# def add():
#     def subs(a,b):
#         print("Output of numbers is :",a-b)
#     subs(20,10)
# add()

# nested function 

def parent():
    def child(fnm):
        return fnm 
    res=child("The name of my child is :"+"shivansh")
    print(res)
parent()