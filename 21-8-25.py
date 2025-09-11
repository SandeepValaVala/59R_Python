# Implement a basic login system where the user has three attempts to enter the correct password using a loop.


# db_username = 'sandeepvalavala'
# db_password = 'sai@123'
# remaining_chances = 3

# while remaining_chances > 0:
#     input_username = input('Enter username: ')
#     input_password = input('Enter password: ')
    
#     if db_username == input_username and db_password == input_password:
#         print('Login successful')
#         break
#     else:
#         remaining_chances -= 1
#         print('Login failed')
#         if remaining_chances == 0:
#             print('Try again after 24 hrs')

# Reverse a number using a  while  loop. 
# 1.  Also can we get the sum of all the digits.
# Write a program to count the number of digits in a given number using a  while  loop.

# -------------------------Reverse a num value and also sum of all digits--------------------------------------------

# num = 12456
# sum = 0
# v = 0
# while num > 0:
#     rem = num % 10
#     sum += rem
#     v = v * 10 + rem 
#     num = num // 10
# print(v)
# print(sum)



# --------------------------method 2---------------------------------

# num = 1476
# sum = 0
# while num > 0 :
#     rem = num % 10
#     sum += rem
#     num = num // 10
# print(sum)


# num = 1476
# while num > 0 :
#     rem = num % 10
#     print(rem)
#     num = num // 10

# num = 1476
# count = 0
# sum = 0

# #  <------1476 => rem = 6, floor_division = 147 ------->
# # <-------147 => rem =  7, floor_division = 14 ------->
# # <-------14 => rem =  4, floor_division = 1 ------->
# # <-------1 => rem =  1, floor_division = 0 ------->

# while num > 0 :
#     digit = num % 10
#     # print(digit)
#     sum += digit
#     num = num // 10
#     count += 1

# print(count)
# print(sum)



# ----------------------- method - 1{reverse}---------------------------------

# n = 1470
# rev_num = 0
# while n > 0:
#     digit = n % 10
#     rev_num = rev_num * 10 + digit
#     n = n // 10
# print(rev_num)




# n = 1476
# rev_num = 0
# sum = 0
# count = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     rev_num = rev_num * 10 + digit
#     n = n // 10
#     count += 1
# print(rev_num)
# print(sum)
# print(count)

# while True:
#     num1 = int(input('Enter a positive number:'))
#     print(num1)
#     if num1 <= 0:
#         print('Non positive number entered')
#         break

# ----------------small change chayillali-----------

# while True:
#     num = -1476
#     rev = 0
#     if num >= 0:
#         digit = num % -10
#         print(digit)
#         rev = rev * 10 + digit
#         num = num // 10
#     print(rev)
    
# n = 1470
# flag = True
# rev_num = 0
# while n > 0:
#     flag = False 
#     digit = n % 10
#     rev_num = rev_num * 10 + digit
#     n = n // 10

# if flag:
#     print(rev_num)
# else:
#     print(rev_num * -1)