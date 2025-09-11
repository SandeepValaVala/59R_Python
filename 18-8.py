# def student_marks(num1):
#     return "pass" if num1 >= 40 else ("subpass" if num1 >= 30 else "fail")
# print(student_marks(50))
# print(student_marks(35))
# print(student_marks(20))

# num1 = int(input("enter a numbber:"))
# if num1 == 1:
#     print("Monday")
# elif num1 == 2 :
#     print("Tuesday")
# elif num1 == 3:
#     print("Wednesday")
# elif num1 == 4:
#     print("Thursday")
# elif num1 == 5 :
#     print("Friday")
# elif num1 == 6:
#     print("Saturday")
# elif num1 == 7:
#     print("sunday")
# else:
#     print("Invalid")

#  ---------simple calculator----------

# def simple_calc(op,num1,num2):
#     # if op == '+':
#     # if op == '+' or op == 'add' or op == 'ADD':
#     # if op in ['+','add','Add','ADD']:
#     if op in ['+','add']:
#         return num1 + num2
#     elif op == '-':
#         return num1 - num2
#     elif op == '*':
#         return num1 * num2
#     elif op == '/':
#         return num1 / num2 if num2 != 0 else 'Invalid denominator'
#     else:
#         return 'Invalid operator'
    
# op = input("enter an operator:").lower()
# num1 = float(input("enter a number1:"))
# num2 = float(input("enter a number2:"))

# res = simple_calc(op,num1,num2)
# print(res)
# print(simple_calc(op,num1,num2))

# a = 10
# b = 10
# dict = {"+" : a + b}
# print(dict)


# ---------- write a program to find the greatest of three numbers --------

# num1,num2,num3 = 5, 7, 9

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# # elif num2 >= num1 and num2 >= num3:
# elif  num2 >= num3:
#     print(num2)
# else:
#     print(num3)



# num1 = int(input('Enter a num1:'))
# num2 = int(input('Enter a num2:'))
# num3 = int(input('Enter a num3:'))

# if num1 >= num2 and num1 >= num3:
#     greatest = num1
# elif num2 >= num1 and num2 >= num3:
#     greatest = num2
# else:
#     greatest = num3

# print('The greatest of three numbers is:',greatest)

# def greatest_three_numbers(num1,num2,num3):
#      if num1 >= num2 and num1 >= num3:
#          greatest = num1
#      elif num2 >= num1 and num2 >= num3:
#          greatest = num2
#      else:
#          greatest = num3
#      return greatest
# result = greatest_three_numbers(num1 = 10,num2 = 20 , num3 = 15)
# print(result)

# ------------------- ternary conditional expression --------

# def greatest_three_numbers(num1,num2,num3):
#     # return  num1 if num1 >= num2 and num1 >= num3 elif (num2  num2 >= num1 and num2 >= num3 else
#     return num1 if (num1 >= num2 and num1 >= num3) else (num2 if (num2 >= num1 and num2 >= num3) else num3)
# print(greatest_three_numbers(10,20,30))
# print(greatest_three_numbers(20,30,40))
# print(greatest_three_numbers(30,40,50))


# ------ check if a year is a leap year-------

# year = int(input('Enter a year:'))

# if year % 400 == 0 or year % 4 == 0 and  year % 100 != 0:
#     print( year,'is a leap year')
# else:
#     print(year,'is not a leap year')


# for year in range(2000,2026):
#     if year % 400 == 0 or year % 4 == 0 and  year % 100 != 0:
#         print( year,'is a leap year')
#     else:
#         print(year,'is not a leap year')


# ------------------- ternary  operator conditional expression --------

# year = 2024

# print(year,"is a leap year") if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) else (year,"is not a leap year")



    

# year = int(input('Enter a year:'))

# def leap_year(year):
#     return (year,'is a leap year') if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else (year,'iis not a leap year')
# print(leap_year(year))



# ---calculate the grade of a student based on the marks they score: 
# 1.  90-100  : Grade A 
# 2.  80-89  : Grade B 
# 3.  70-79  : Grade C 
# 4.  <70  : Fail. ------------------------------

# num1 = int(input('Enter a marks:'))

# if 90 <= num1 <= 100 :
#     print('Grade A')
# elif 80 <= num1 <= 89 :
#     print('Grade B')
# elif 70 <= num1 <= 79 :
#     print('Grade C')
# elif num1 < 70 :
#     print('Fail')
# else:
#     print('Invalid')


# -------function -------


# def student_marks(num1):
#     if 90 <= num1 <= 100 :
#         print('Grade A')
#     elif 80 <= num1 <= 89 :
#         print('Grade B')
#     elif 70 <= num1 <= 79 :
#         print('Grade C')
#     elif num1 < 70 :
#         print('Fail')
#     else:
#         print('Invalid')

# student_marks(num1 = 95)





#  ------------------- ternary conditional expression --------

# def student_marks(num1):
#     return ( 'Grade A 'if 90 <= num1 <= 100  else 'Grade B'  if 80 <= num1 <= 89  else 'Grade C' if 70 <= num1 <= 79  else 'Fail' if num1 < 70 else 'Invalid' )
# print(student_marks(num1 = 95))

# ----write a program to check if three sides length form a valid triangle------

# s1, s2, s3 = 2, 3, 5

# if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2) :
#     print('Triangle can be formed')
# else:
    # pass




# ------ write a program to classify a character entered by the user as a vowel, consonant, or neither.-------

# input_char = input('Enter a character : ')
# def check_char(in_ch):
#     if in_ch in 'aeiou':
#         print('vowel')
#     else:
#         print('consonant')
# elif in_ch in 'bcdfgh':
    



# -----------