# a=10
# def test():
#     # local
#     # access as global
#     global b
#     b=20
#     print(b)
# test()     
# # access b globally or as a global variables 
# print("Global values of b is :",b)


def glob():
    # global
    global a 
    global b 
    global c
    a=10;b=20;c=30  #this is a local 
    print(a,b,c)
glob()
print(a,b,c)
