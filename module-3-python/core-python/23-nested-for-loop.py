'''
nested for loop :
  loop within another loop i.e called nested loop
  
  syntax :
  
   for variable in iterable:
     for variable in iterable:
        statements
         
'''
# print star triangle pattern

# for i in range(1,6):
#     for j in range(i):
#         print("*", end="")
#     print()


# for i in range(1,6):
#     for j in range(i):
#         print(j, end="")
#     print()

# print multiplication table
for i in range(1,11):
    for j in range(1,11):
        # print("#########")
        print(i, "*", j, "=", i*j)
    
    print("###########") 