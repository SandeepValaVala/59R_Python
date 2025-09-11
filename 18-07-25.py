# Arthematic operators => -,+,*,/,//,%,**

# num1 = 10
# num2 = 0
# print(num1/num2)  #ZeroDivisionError: division by zero  --  cannot divide with zero

# BODMAS RULE:--

# print(2 - 2 * 4)  # bodmas take preference the *  , / , values only # -6

# print((2-2)* 4)  #0

#  Relational operators or conditional operators :--  > ,< ,>=, <=, ==, != 

# print(2 >3) #false
# print(2<3)  #true

# print(5==4) #false
# print(5==5)  #true

# print(5!=5) #false
# print(5!='5')#TRUE

# print('abc' < 'abd')  #true
# print('abc' =='abc') #true

#Assignment operators :--  = , 
# 

# num1 = 10

# print(num1 + 10) #read only given num1 value only 
# print(num1)

# num1 += 10 #num1 = num1 + 10 
# print(num1)

# Eg:--
# users_fathers_age_at_birth = 25
# users_fathers_age_at_birth += 25
# print(users_fathers_age_at_birth)  #50

# num3 = 50 
# num3 = num3 * 3 #num3 *= 3
# print(num3)   #150
 
# num3 = num3 * 3 #num3 *= 3
# print(num3)  # NameError: name 'num3' is not defined

# short term methods
# num = 20
# num -= 10
# print(num) #10

# num += 10
# print(num) #30

# num *= 10
# print(num) #200

# num /= 2
# print(num) #10

# num //= 10
# print(num) #2

# num %= 10
# print(num)  #0 take remainder only

# num **= 10
# print(num) #10240000000000

# Membership operators  :--

# print(3 in [1,2,4,7,9,11,[2,3]])  # false

# print( 'kk' in {'k', 1,2,3}) #false

# dict1 =  {
#     1:'1',
#     2:'2',
#     3:'3',
#     4:'4'
# }
# print(3 in dict1)  #true

# dict1 =  {
#     1:'1',
#     2:'2',
#     4:'4'
# }
# print(3 not in dict1) #true


# Identity operators:--

# num1 = 10
# num2 = 10
# num3 = 20

# print(id(num1))
# print(id(num2))
# print(id(num3))

# print(num1 is num2)  #true
# print(num2 is not num3) #true

# str1 = 'good'
# str2 = 'good'

# print(str1 is str2) #true


# list1 = [1,2,3]
# list2 = [1,2,3]
# print(id(list1))


# num = 5
# n = bin(num)
# print(n)   #0b101


# num = 20

# num+= 10
# print(num)

# num-= 10
# print(num)

# num *=10
# num /=10
# num //=10
# num %=10
# num **=10
# print(num)

# num = 50
# s=0
# while num>0:
#     v=num%2
#     s=v+s*10
#     num//=2
# print(str(s)[::-1])

# num = 110010
# count=0
# sum=0
# while num>0:
#     temp=num%10
#     if temp==1:
#         sum+=2**count
#     elif temp==0:
#         pass
#     num=num//10
#     count+=1
# print(sum)






year=int(input('enter a number :'))
if (year%4==0) and (year%100!=0) or (year%400==0):
    print('its a leap year')
else:
    print('its not a leap year')   
    
    
    
    
    
    
     
# def is_leap(year):
#       leap = False
#     # Check if the year is a leap year
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
    
# year = int(input( ))
# print(is_leap(year))
    