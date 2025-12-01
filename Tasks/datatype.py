# # 1.	Add an integer and float. What is the result’s type?

# integr = 10
# float = 2.2
# x = integr + float
# print(type(x))   #<class 'float'>

# # 2.Create a string and access its:
# #    1 .First character
# #    2.Last character
# #    3.A substring from index 2 to 5

# str1 ='sandeep'
# print(str1[0])   #    s
# print(str1[-1])  #    p
# print(str1[2:6])  #   ndee

# # 3.Concatenate two strings and print the result

# s1 = "Hello"
# s2 = "sai"
# a = s1 + s2
# a = s1 +" "+ s2
# print(a) #Hellosai

# # 4.Define list. What are the difference between List and Tuple

# # 1) List is an ordered sequence of items.
# #  2) We can have different data types under a list. E.g we can have integer, float and string items in
# #  a same list.
# # 3) Tuple is similar to List except that the objects in tuple are immutable which means we cannot
# #  change the elements of a tuple once assigned.
# #  4). When we do not want to change the data over time, tuple is a preferred data type.

#  # 5.Write a programme to print a list in reverse order

# s = [1,2,3,4,5,6]
# s.reverse()
# print(s)   #[6, 5, 4, 3, 2, 1]

# s = ['sai','sandeep','naga','siva']
# print(s[::-1])    #['siva', 'naga', 'sandeep', 'sai']

#  # 6.Create a tuple of 4 elements. Print the first and last element

# s1 = ('NAGA','SAI','SANDEEP','siva')
# print(s1[0])  # NAGA
# print(s1[3])  # siva

#   # 7.Try changing a value in a tuple. What happens

# s2 = ('NAGA','SAI','SANDEEP','siva')
# print(type(s2)) #<class 'tuple'>
# s2[1]='sumanth'
# print(s2)  #TypeError: 'tuple' object does not support item assignment

 #8.Create a dictionary of 3 students with their marks. Print the dictionary

# marks ={
#     'A': 98,
#     'B': 88,
#     'C': 76
# }
# print(marks) #{'A': 98, 'B': 88, 'C': 76}
# Python3 Program to find minimum 
# number of operations to make all 
# array Elements equal

# Function to find minimum number 
# of operations to make all array
# Elements equal


