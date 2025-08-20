#  Print all numbers from 1 to 100 using a  for  loop?

# n = 100      
# for i in range(1, n+1):
#     print(i)

# Write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2) 
# --------- sum of first n natural numbers------

# n = 25
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(sum)



#---3-- print all even numbers between 1 and 50 using a  while loop. 

# num1 = 1
# while num1 <= 51:
#     if num1 % 2 == 0:
#         print(num1)
#     num1 += 1   


# ----function---

# def even_numbers(num1):
#     while num1 < 51:
#         if num1 % 2 == 0:
#             print(num1)
#         num1 += 1
# even_numbers(1)

# --4-- write a program to display the multiplication table of a given number. First 20

# n = 20
# for i in range(1, n + 1) :
#     print(f'{n} x {i} = {n * i}')

# n = 20
# i = 1
# while i <= 20:
#     print(f'{n} x {i} = {n * i}')
#     i += 1

# def multiplication_table(n):
#     for i in range(1, n + 1):
#         print(f'{n} x {i} = {n * i}')

# multiplication_table(20)
        

# Reverse a number using a  while  loop. 
# 1.  Also can we get the sum of all the digits.






 
# Write a program to count the number of digits in a given number using a  while  loop.




   

# ---7-- write a program that keeps asking the user to enter numbers until they enter a negative number. Use a  while  loop.

# while True:
#     num1 = int(input('Enter a positive number:'))
#     print(num1)
#     if num1 <= 0:
#         print('Non positive number entered')
#         break

# ---implement a menu-driven program where the user can choose to: 
# 1.  Find the square of a number. 
# 2.  Find the cube of a number. 
# 3.  Exit. -----------

# while True:
#     print('1. square 2. cube .Another option will exit the code')
#     choice = input('Enter your choice:').lower()
    
#     if choice == '1' or choice == 'square' :
#         input_num = float(input('Enter the number to square'))
#         print(input_num ** 2)
    
#     elif choice == '2' or choice == 'cube' :
#         input_num = float(input('Enter the number to cube'))
#         print(input_num ** 3)
    
#     else:
#         print('No valid option picked')
#         print('----Exiting----')
#         break


# ------Arithmetic operators -------

# while True:
#     print('1. addition 2. subtraction 3. multiplication 4. division 5. floor division 6. modulus')
#     choice = input('Enter your choice:')
    
#     if choice == '1' or choice == 'addition' :
#         input_num1 = float(input('Enter the number to addition : '))
#         input_num2 = float(input('Enter the number to addition : '))
#         print(input_num1 + input_num2)
    
#     elif choice == '2' or choice == 'subtraction' :
#         input_num1 = float(input('Enter the number to subtraction : '))
#         input_num2 = float(input('Enter the number to subtraction : '))
#         print(input_num1 - input_num2)
    
#     elif choice == '3' or choice == 'multiplication' :
#         input_num1 = float(input('Enter the number to multiplication : '))
#         input_num2 = float(input('Enter the number to multiplication : '))
#         print(input_num1 * input_num2)
        
#     elif  choice == '4' or choice == 'division':
#         input_num1 = float(input('Enter the number to division : '))
#         input_num2 = float(input('Enter the number to division : '))
#         if input_num2 != 0:
#             print(input_num1 / input_num2)
#         else:
#             print('Division by zero is not possible')
        
#     elif choice == '5' or choice == 'floor division':
#         input_num1 = float(input('Enter the number to  floor division : '))
#         input_num2 = float(input('Enter the number to  floor division : '))
#         if input_num2 != 0:
#             print(input_num1 // input_num2)
#         else:
#             print('Division by zero is not possible')
        
#     elif choice == '6' or choice == 'modulus':
#         input_num1 = float(input('Enter the number to modulus : '))
#         input_num2 = float(input('Enter the number to modulus : '))
#         if input_num2 != 0:
#             print(input_num1 % input_num2)
#         else:
#             print('Division by zero is not possible')
    
#     else:
#         print('No valid option picked')
#         print('----Exit----')
#         break

# ----print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop.----

# n = 100
# for i in range(1, n + 1) :
#     if (i % 3 == 0) and (i % 5 == 0) :
#         print(i)

# ----write a program to calculate the factorial of a number using a  while  loop.----


# num = int(input('Enter a number:'))
# factorial = 1
# sum = 1

# while sum <= num:
#     factorial *= sum
#     sum += 1
    
# print(factorial)    


# ---
    
    








