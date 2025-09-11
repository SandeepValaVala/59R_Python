# Logical operators ---- and, or , not 

# {and} examples :----

# if first operand itself is false ,then i don't have to check 2nd operand
       #  output is  depend on first operand 
# if first operand is true ,overall output is depends on second operand   

# n1 =35
# print((n1>25) and (n1<50)) #true

# examples:---

# print(True and True)  #true
# print(False and false) #false
# # print(false and False)  #Error
# print(True and False) #False
# print(False and True) #false

# print(True and True and (True and (True and False and (True and True and (True and True)))))  #false

# list eg:--
# print(range(0,10)) #range(0,10)
# print(list(range(0,10)))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# boolean eg:---

# num1 = 10
# print(bool(num1)) #true

# num1 = 0
# print(bool(num1)) #false (0 is falsy value)

# num1 = -1
# print(bool(num1)) #true

# any number except 0 gives to true value
# any string except ' ' is a truthy value
# general empty data type examples are falsy value

# examples:---

# 'sandeep' ,[] ,{1,2},False,5.5,-25,0,'',{},(),[55]


# num1 = 'sandeep'
# print(bool(num1)) #True

# num1 = []
# print(bool(num1)) #false

# num1 = {1,2}
# print(bool(num1)) #true

# num1 = False
# print(bool(num1)) #false

# num1 = 5.5
# print(bool(num1)) #true

# num1 = -25
# print(bool(num1)) #true

# num1 = 0
# print(bool(num1)) #false

# num1 = 1
# print(bool(num1)) #true

# num1 = ''
# print(bool(num1)) #false
 
# num1 = ' '
# print(bool(num1)) #true

# num1 = {}
# print(bool(num1)) #false

# num1 = ()
# print(bool(num1)) #false

# num1 = [55]
# print(bool(num1)) #true


# print( 2 and 0 )  # 0
# print('' and 'temp') # empty
# print(0 and [1, 2, 3]) #0
# print(1 and True) #True
# print(True and []) #[]

# print('' and 'temp') # empty string is false 
# print(' ' and 'temp') #temp

      
 # { or }  examples:---

# if first operand is true ,overall output is depends on first operand
# if first operand is fale ,then have to check the  second operand 

# print(True or False) #true
# print(False or True) #true
# print(True or True) #true
# print(False or False) #false


# print( 2 or 0 )  # 2
# print( 0 or 2 )  # 2
# print('' or 'temp') # temp
# print(0 or [1, 2, 3]) #[1,2,3]
# print(5 or [1, 2, 3]) #5
# print(1 or True) #1
# print(True or []) #true
# print(False or []) #[]

# {not} example:----

# True --------->False   NOT Is replace the values
# False---------> True

# print(not(True and True and False and True and True)) #true
# print(not(False or False or True or False or False))  #false



# Bitwise operators:---- & , | , ^ , << ,>> , ~ 

# print(7&11)  #3
# print(7 and 11)  #11

# print(13 & 9)  #9
# print(13 | 9)  #13

# print(9 and 11) #11
# print(9 & 11) #9
# print(9 | 11) #11
# # print(9 ^ 11) #2


# print(12 and 23) #23
# print(12 & 23) #4
# print(12 | 23) #31
# print(12 ^ 23) #27


# print(12 and 6) #6 
# print(12 & 6) #4
# print(12 | 6) #14
# print(12 ^ 6) #10
