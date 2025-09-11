# name = input('Enter your name: ')
# hindi_marks = input('Enter hindi marks: ')
# maths_marks = input('Enter maths marks: ')
# science_marks = input('Enter science marks: ')
# percentage = ((int(hindi_marks)+int(maths_marks)+int(science_marks))/300)*100
# print(f"{name},have{percentage}% well done & keepworking hard !!")

# str_num = "26"
# int_num = int(str_num)
# print(int_num)
# print(type(int_num))

#Numeric 

# val1 = 10  # Integer data type
# print(val1)
# print(type(val1))
# print(val1, "is integer?", isinstance(val1,int))

# val2 = 92.78 # Float data type
# print(val2)
# print(type(val2))
# print(val2, "is float ?", isinstance(val2,float))

# val3 = 25 + 10j  #complex data type
# print(val3)
# print(type(val3))
# print(val3,"is complex?", isinstance(val3,complex))


#boolean:----

# bool1 = True
# bool2 = False
# print(type(bool1))
# print(type(bool2))
# print(isinstance(bool1,bool))


# print(bool(0))
# print(bool(1))
# print(bool(None))
# print(bool(False))

#string----

# str1 = "HELLO PYTHON"
# print(str1)

# mystr = 'Hello world'
# print(mystr)


# mystr = 'Hello world '
# mystr1 = mystr*5
# print(mystr1)

# mystr = "sandeep"
# print(len(mystr))

# -------string indexing:----

# str = "hello python"
# print(str)
# print(str[0])
# print(str[len(str)-1])
# print(str[-1])
# print(str[7])


# ----- string slicing------


# str = "hello python"
# print(str[0:5])
# print(str[6:12])
# print(str[-4:])
# print(str[:6])

#------update & delete string-------

# str = "HELLO PYTHON"
# print(str)
# str[0:5] = 'HOLAA'  #TypeError: 'str' object does not support item assignment

# del str
# print(str)  # NameError: name 'str' is not defined

# ------ string concatenation-----

# s1 = "hello"
# s2 = "ravi"
# s3 = s1 + s2
# print(s3)   #helloravi


# s1 = "hello"
# s2 = "ravi"
# s3 = s1 + " " + s2
# print(s3)    #hello ravi

#----- Iterating  through a string-----

# mystr1 = "HELLO EVERYONE"
# #Iteration
# for i in mystr1:
#     print(i)

# mystr1 = "HELLO EVERYONE"
# for i in enumerate(mystr1):
#     print(i)

# mystr1 = "HELLO EVERYONE"
# i = list(enumerate(mystr1))
# print(i) 

#---- string membership---

# mystr1 = "hello everyone"
# print('hello' in mystr1)    #True
# print('everyone' in mystr1) #True
# print('hi' in mystr1)  #False


#---- string partitioning----

# str = "natural language processing with python and R and Java "
# L = str.partition("and")
# print(L)  #('natural language processing with python ', 'and', ' R and Java')

# str = "natural language processing with python and R and Java "
# L = str.rpartition("and")
# print(L)  #('natural language processing with python and R ', 'and', ' Java ')


# -----string functions-------

# mystr1 = "  Hello Everyone  "
# print(mystr1)    #  Hello Everyone  
# print(mystr1.strip())  #Hello Everyone
# print(mystr1.rstrip())  #  Hello Everyone
# print(mystr1.lstrip())   #Hello Everyone   


# mystr1 = "*****Hello Everyone*****All the Best*****"
# print(mystr1)  #*****Hello Everyone*****All the Best*****
# print(mystr1.strip('*'))  # Hello Everyone*****All the Best
# print(mystr1.rstrip('*')) # *****Hello Everyone*****All the Best
# print(mystr1.lstrip('*')) # Hello Everyone*****All the Best*****



# mylist = ['one','two','three','four','five','six','seven','eight']
# print(mylist)
# mylist.append('nine')
# print(mylist)
# mylist.insert(9,'ten')
# print(mylist)
# mylist.insert(1,'one')
# print(mylist)



# mystring = "welcome"
# mylist =  [i for i in mystring]
# print(mylist)


# for i in range(40):
#     if i%2 == 0:
#         print(i)

# myset = ('one','two','three','four','five','six','seven','eight')
# print(myset)
# myset = {'one','two','three','four','five','six','seven','eight'}
# print('one' in myset)


# A ={1,2,3,4,5}
# B={4,5,6,7,8}
# C={8,9,10}
# print(A|B)
# print(A.union(B))
# print(A.union(B))
# print(B.union(C))
# print(A.union(B,C))


num = "sandeep"

num1 =" "
for i in num:
    num1 = i + num1
    
if num == num1:
    print("palindrome")
else:
    print("not a palindrome")

