# class_no = 1
# while class_no < 11:
#     roll_no =1
#     while roll_no <31:
#         print( 'class',class_no ,'roll_no' ,roll_no)
#         roll_no +=1
#     class_no +=1


# first problem----- using for loop


# for class_no in range(1,11):
#     for roll_no in range(1,31):
#         if roll_no > 5:
#             break
#         print('class',class_no,'roll_no',roll_no)

#  first problem----- using while loop

# class_no = 1
# while class_no < 11:
#     roll_no =1
#     while roll_no <= 5:
#         print( 'class',class_no ,'roll_no' ,roll_no)
#         roll_no +=1
#     class_no +=1



# second problemm------ using for loop

# for class_no in range(1,11):
#     for roll_no in range(1,5):
#         if class_no == 5:
#             continue
#         print('class',class_no,'roll_no',roll_no)

# second problemm------ using   while loop

# class_no = 1
# while class_no <= 10:
#     if class_no == 5:
#         class_no += 1
#         continue
#     roll_no = 1
#     while roll_no <= 5:
#         if roll_no == 5:
#             roll_no+=1
#             continue
#         print('class',class_no,'roll_no', roll_no)
#         roll_no += 1
#     class_no += 1



# class_no = 1
# while class_no <= 10:
#     if class_no == 5:
#         class_no += 1
#         continue
#     roll_no = 1
#     while roll_no <= 4:
#         print('class', class_no, 'roll_no', roll_no)
#         roll_no += 1
#     class_no += 1




# third  problemm------ using for loop

# for class_no in range(1,11):
#     for roll_no in range(1,5):
#         if class_no == 5:
#             print('class',class_no,'roll_no',roll_no)

# third  problemm------ using   while loop

# class_no = 1
# while class_no <= 10:
#     if class_no == 5:
#         roll_no = 1
#         while roll_no < 5:
#             print('class',class_no,'roll_no',roll_no)
#             roll_no += 1
#     class_no += 1

# fourth problem ---- using  -- for loop

# for class_no in range(1,11):
#     if class_no == 5:
#         continue
#     for roll_no in range(1,31):
#         print('class',class_no,'roll_no',roll_no)

# fourth problem ---- using  -- while loop

# class_no = 1
# while class_no < 11:
#     if class_no == 5:
#         class_no += 1
#         continue
#     roll_no = 1
#     while roll_no < 31:
#         print('class',class_no,'roll_no',roll_no)
#         roll_no += 1
#     class_no += 1


# roll_no = 1
# while roll_no < 31:
#     print('roll_no',roll_no)
#     roll_no += 1

# fivth problem ---- using  -- for loop

for class_no in range(1,11):
    for roll_no in range(1,31):
        if class_no % 3== 0 or roll_no < 15:
            break
        print('class',class_no,'roll_no',roll_no)   # empty output becuase inner loop was break

# fivth problem ---- using  -- while loop

# class_no = 1
# while class_no < 11:
#     roll_no = 1
#     while roll_no < 31:
#         if class_no % 3 == 0 or roll_no < 15:
#             break
#         print('class',class_no,'roll_no',roll_no)
#         roll_no += 1
#     class_no += 1

# sixth problem ---- using  for loop 

# for class_no in range(1,11):
#     for roll_no in range(1,31):
#         if class_no % 3== 0 and roll_no < 15:
#             break
#         print('class',class_no,'roll_no',roll_no) 

# sixth problem ---- using  while loop 

# class_no = 1
# while class_no < 11:
#     roll_no = 1
#     while roll_no < 31:
#         if class_no % 3 == 0 and roll_no <15 :
#             break
#         print('class',class_no,'roll_no',roll_no)
#         roll_no += 1
#     class_no += 1
    
# seventh problem ---- using  for loop 
    
# for class_no in range(1,11):
#     for roll_no in range(1,31):
#         if class_no % 3== 0 and roll_no > 15:
#             break
#         print('class',class_no,'roll_no',roll_no)

# seventh problem ---- using  while loop

# class_no = 1
# while class_no < 11:
#     roll_no = 1
#     while roll_no < 31:
#         if class_no % 3 == 0 and roll_no > 15 :
#             break
#         print('class',class_no,'roll_no',roll_no)
#         roll_no += 1
#     class_no += 1

# eight problem ---- using for loop (even)

# for class_no in range(1,11):
#     if class_no & 1 ==0 :
#         continue
#     for roll_no in range(1,31):
#         if class_no % 3== 0 and roll_no < 15:
#             continue
#         print('class',class_no,'roll_no',roll_no)

# eight problem ---- using while loop

# class_no = 1
# while class_no < 11 :
#     if class_no & 1 == 0 :
#         class_no += 1
#         continue
#     roll_no = 1
#     while roll_no < 31:
#         if class_no % 3 == 0 and roll_no < 15:
#             roll_no += 1
#             continue
#         print('class',class_no,'roll_no',roll_no)
#         roll_no += 1
#     class_no += 1




# positive = True
# while positive:
#     n = int(input('enter a number'))
#     if n <= 0:
#         print('positive')

# while 3 > 2:
#     ip_num = int(input('Enter a  positive number'))
#     if ip_num <=0:
#         print('non positive number entered')
#         break


# while True:
#     ip_num = int(input('Enter a  positive number'))
#     if ip_num <=0:
#         print('non positive number entered')
#         break