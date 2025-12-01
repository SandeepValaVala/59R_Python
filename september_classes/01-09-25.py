# Lambda Function: lambda functions are one line anonymous(nameless)functiom
# defination?
# A lambda function in Python is a small, anonymous (nameless) function that is defined using the keyword lambda.

# def add (a,b):
#     return a+b
# print(add(2,5))

# ex:--- lambda a ,b : a + b

# example_function = lambda a , b : a + b
# res = example_function(2,3)
# # example_function = 50
# print(res)

# def square(n):
#     n = n*n
#     return n
# print(square(10))

# ex:---

# example = lambda a : a ** 2
# print(example(5))
# # lambda : 10


# higher order functions:--
# those functions which takes one more function as there function argument.

# example of higher order function

# def first_function(a , b):
#     pass

# def second_function():
#     pass

# first_function(second_function , 5)

# # print(first_function(second_function , 5))


# map , filter  and reduce  are higher order functions

# map :----syntax

# map(func , iterable)

# ex:--

# def square (x):
#     return x ** 2

# # print(map(square , [1,2,3,4,5,6]))   #<map object at 0x000002AB24CDB550>
# print(list(map(square , [1,2,3,4,5,6])))   #[1, 4, 9, 16, 25, 36]

# def square (x):
#     return x + 2

# print(list(map(square , [1,2,3,4,5,6])))  #[3, 4, 5, 6, 7, 8]



# def square (x):
#     return x ** 2

# print(list(map( lambda  a :a ** 4 , [1,2,3,4,5,6])))  #


# # balayya's code
# print(list(map(square , [1, 4 ,9 , -4 ,11 , 23])))



# filter :----


#  x % 2 == 0 ----> True value can print

# print(list(filter(lambda x : x % 2 == 0, [ 1,4,9,-4,11,23])))  #[4, -4]

# print(list(filter(lambda x : x > 0, [ 1,4,9,-4,11,23])))  #[1, 4, 9, 11, 23]

# print(list(filter(lambda x : x-5> 0, [ 1,4,9,-4,11,23])))  #[9, 11, 23]



# reduce :---
# compress  the list values to print one single value

# syntax ------ reduce(func , iterable )

# ex:- 

# reduce( lambda a , b : a + b,[ 1,4,9,-4,11,23])  #NameError: name 'reduce' is not defined

# ex:--- use import

# from functools import reduce  # top of the page
# # print(reduce( lambda a , b : a + b,[ 1,4,9,-4,11,23])) #44
# print(reduce( lambda a , b : a * b,[ 1,4,9,-4,11,23]))  #-36432


# list1
# list1 = [1,2,3,4,5,6,7]
# # using slicing
# print(list1[0:3]) #[1, 2, 3]
# print(list1[3:]) #[4, 5, 6, 7]

# k = 2
# list1 = [1,2,3,4,5,6,7]
# list1 = list1[k:] + list1[0:k]
# print(list1)

k = 70002
list1 = [1,2,3,4,5,6,7]
k = k % len(list1)

list1 = list1[k:] + list1[0:k]
print(list1)