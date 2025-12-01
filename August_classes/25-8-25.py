# num1 = 1476

# flag = True
# if num1 < 0:
#     flag = False
#     num1 = num1 * -1

# rev_num = 0
# while num1 > 0:
#     digit = num1 % 10
#     print(digit)
#     rev_num = rev_num * 10 + digit
#     num1 = num1 // 10

# if flag:
#     print(rev_num)
# else:
#     print(rev_num * -1)





#Prime number

#17
#32 => 1 to 32


# num1 = 35
# count = 0

# for i in range(1, num1 + 1): #35
#     if num1 % i == 0:
#         count += 1


# print('Prime') if count == 2 else print('Not prime')


# -----------------method - 2-----------------------------

# num1 = 45
# flag = True

# for i in range(2,num1):
#     if num1 % i == 0:
#         flag = False
#         print('not prime')
#         break
# if flag == True:
#     print('prime')
    

# num1 = 45

# if num1 <= 1:
#     print('not a prime')
# else:
    
#     flag = True

#     for i in range(2,num1):
#         if num1 % i == 0:
#             flag = False
#             print('not prime')
#             break
#     if flag == True:
#         print('prime')



# ---------------functions-----------------

# def check_prime(num1):
#     if num1 <= 1:
#         return 'Not a prime'
#     for i in range(2, num1):
#         if num1 % i == 0:
#             return 'Not a prime'
    
#     return 'prime'

# print(check_prime(17))
# --------------------method--- 2-------------------------------
# def check_prime(num1):  # 17 => 7 iterations  
#     if num1 <= 1:
#         return 'Not a prime'
#     for i in range(2, num1//2+1):
#         if num1 % i == 0:
#             return 'Not a prime'
    
#     return 'prime'

# print(check_prime(17))

# ------------------final method------------------------------------
# def check_prime(num1):  #17 => 3 iterations
#     if num1 <= 1:
#         return 'Not a prime'
#     for i in range(2, int(num1 ** 0.5)+1):
#         if num1 % i == 0:
#             return 'Not a prime'
    
#     return 'prime'

# print(check_prime(17))


# ------------today task--------------------------------------

# num1 = 400

# for i in range(300,num1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i,"is a prime number")
        
# num1 = 400

# for i in range(300, num1 + 1):
#     if num1 % i == 0:
#         break
#     else:
#         print(i,"is a prime number")
        




# --------------count------------------------


# def check_prime(num1):
#     if num1 <= 1:
#         return 'Not a prime'
#     count = 0
#     for i in range(2, num1):
#         if num1 % i == 0:
#             count += 1
            
#     if count == 0:
#         return 'prime'
#     else:
#         return f'Not a prime (found {count} divisors)'
#         # return f' {count} not prime'

# print(check_prime(35))







