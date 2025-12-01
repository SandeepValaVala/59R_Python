# pass by value ; pass by reference
# pass by object reference

#  example of pass by value using c++ code
# include <studio.h>
# void change(int x){
#     x = 10; //only local copy changes
# }
# int  main(){
#     int a = 5:
#     change(a):
#     printf("%d", a); // print 5 , not 10
# }
# ----------------------------------------------------------

# def add (a , b):
#     return a + b
# c , d = 10 , 20
# print(add(c,d))



# pass by reference ; pass by object reference

# pass by value --> only value can send

# ex:---

# def check_function(num1):
#     num1 = [40,50]
#     print(num1) #[40, 50]
    
# a = [10,20,30]
# check_function(a)
# print(a)   # [10, 20, 30]

# pass by value --> not in python

# def check_function(num1):
#     print(id(num1))  #10
    
# a = 10
# print(id(a))  # 10
# check_function(a)  

# pass by reference ---> not in python

# def check_function(num1):
#     num1 = 20
#     print(num1) #20
    
# a = 10
# check_function(a)
# print(a)   #10 

# --------pass by object reference --> is possible in python---

# def check_function(num1):
#     num1.append(40) 
#     print(num1) #[10, 20, 30, 40]
    
# a = [10,20,30]
# check_function(a)
# print(a)   # [10, 20, 30, 40]
# ---------


# ------using dictionaries-----

# def check_function(num1):
#     num1 ['1'] = 5 
#     print(num1)  #{'1': 5, '2': 'b'}
    
# a = {'1': 'a', '2': 'b'}
# check_function(a)
# print(a)  #{'1': 5, '2': 'b'}



# def check_function(num1):
#     print(type(num1))
#     num1 ['1'] = 5 
#     print(num1)  #
    
# a = {'1': 'a', '2': 'b'}
# check_function(a)
# print(a)  #

# res = check_function(10)
# print(check_function(10))


# compresions nothing but shortcut

# list1 = [10,20,30]
# print([x ** 2 for x in list1])

# for  else ---> else is optional
# num1 = 7
# for i in range(2, num1 // 2 + 1):
#     if num1 % i == 0:
#         print('not a prime number')
#         break
# else:
#     print('prime')

#------------ using while---------- 
# num1 = 7
# i = 2

# while i < (num1 // 2 + 1):
#     if num1 % i == 0:
#         print('not a prime number')
#         break
#     i += 1
# else:
#     print('prime')



