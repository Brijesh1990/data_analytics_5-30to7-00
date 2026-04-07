# defining a list of integers
my_list = [1, 2, 3, 4, 5]
print(my_list)
# defining a list of strings
my_list = ["apple", "banana", "cherry"]
print(my_list)
# defining a list of mixed data types
my_list = [1, "hello", 3.14, True]
print(my_list)
# defining a list of lists
my_list = [[1, 2, 3], ["a", "b", "c"]]
print(my_list)

# defined list as constructor as list() function
my_list = list((1, 2, 3, 4, 5))
print(my_list)
my_list = list(("apple", "banana", "cherry"))
print(my_list)
my_list = list((1, "hello", 3.14, True))
print(my_list)
my_list = list(([1, 2, 3], ["a", "b", "c"]))
print(type(my_list))


# duplicate values in list
my_list = [1, 2, 2, 3, 4, 4, 5]
print(my_list)

# repeat 
my_list=[2]*20
print(my_list)


# iterable to list
# employee=["Alice", "Bob", "Charlie","het","brijesh"]
# for i in employee:
#     print(i)

#for i in employee:
    #print(i)
    #print(i[0]) # first character of each name
    #print(i[0:3]) # first three characters of each name
    #print(i[-3:]) # last three characters of each name
    #print(i[1:4]) # characters from index 1 to 3 (excluding index 4)    
    
    
# employee=["Alice", "Bob", "Charlie","het","brijesh"]
# print(list(employee))
# print(employee[::-1]) # reverse the list

# append in list : add a single element to the end of the list   
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)


#extend in list : add elements of another list to the end of the current list

# my_list = [1, 2, 3]
# my_list.extend([4,5,8])
# print(my_list)


# my_list = [1, 2, 3]
# my_list.append([4,5,8])
# print(my_list)


#insert in list : insert an element at a specific position in the list

#my_list = [1, 2, 3]
# my_list.insert(0,5) # insert 5 at index 0
# print(my_list)

#my_list.insert(2,10) # insert 10 at index 2
#print(my_list)


#employee=["krish", "devyang", "jinali","het","brijesh"]

# employee.insert(2,"pratik") # insert "pratik" at index 2
# print(employee)

# employee.insert(0,"pratik") # insert "pratik" at index 0
# print(employee)

# employee.insert(-1,"pratik") # insert "pratik" at index -1 (before the last element)
# print(employee)

#employee.insert(5,"pratik") # insert "pratik" at index 100 (which is out of range, so it will be added at the end)
#print(employee)


# how to remove an element from a list

# remove() method: removes the first occurrence of a specified value
# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3) # remove the first occurrence of 3
# print(my_list)


# removed all data from list    
# my_list = [1, 2, 3, 4, 5]
# my_list.clear() # remove all elements from the list
# print(my_list)
# res=[]
# res.append(10)
# print(res)


# remove all data using remove() method

# my_list = [1, 2, 3, 4, 5,6,7,8,9,10]
# for i in my_list:
#     print(i)
#     my_list.remove(i) # remove the first occurrence of i
# print(my_list)

# my_list = [1, 2, 3, 4, 5,6,7,8,9,10]
# my_list.remove(1) # remove the first occurrence of 1
# print(my_list)


#my_list=[10,20,30,40,50]
# update a list element by index
# my_list[0]=100
# print(my_list)

# my_list[2]=70
# print(my_list)


#pop() method: removes and returns the element at a specified index (default is the last element)

# my_list = [1, 2, 3, 4, 5]
# popped_element = my_list.pop() # remove and return the last element
# print(popped_element) # output: 5
# print(my_list) # output: [1, 2, 3, 4]



# my_list = [1, 2, 3, 4, 5]
# popped_element = my_list.pop(2) # remove and return the element at index 2
# print(popped_element) # output: 3
# print(my_list) # output: [1, 2, 4, 5]


# sorting a list : sort() method: sorts the list in ascending order (by default) or in descending order if specified
# my_list = [5, 2, 9, 1, 5, 6]
# my_list.sort() # sort the list in ascending order
# print(my_list) # output: [1, 2, 5, 5, 6, 9]

my_list = [5, 2, 9, 1, 5, 6]
# descendning order
my_list.sort(reverse=True) # sort the list in descending order
print(my_list) # output: [9, 6, 5, 5, 2, 1]


# slice any list : slicing allows you to extract a portion of a list by specifying a range of indices
my_list = [1, 2, 3, 4, 5]
# slicing from index 1 to 3 (excluding index 4)
sliced_list = my_list[1:4]
print(sliced_list) # output: [2, 3, 4]
# slicing from the beginning to index 3 (excluding index 4)
sliced_list = my_list[:4]
print(sliced_list) # output: [1, 2, 3, 4]
# slicing from index 2 to the end of the list
sliced_list = my_list[2:5]
print(sliced_list) # output: [3, 4, 5]
# slicing with a step of 2
sliced_list = my_list[::2]
print(sliced_list) # output: [1, 3, 5]

# sum of all list data
my_list = [1, 2, 3, 4, 5]
total_sum = sum(my_list)
print(total_sum) # output: 15

# average of all list data
average = total_sum / len(my_list)
print(average) # output: 3.0