# for class_no in range(1,11):
#     print(class_no,'class')
#     for roll_no in range(1,31):
#         print('class', class_no,'roll_no',roll_no)

# even roll numbers---

# for class_no in range(1,11):
#     print(class_no,'class')
#     for roll_no in range(1,31):
#         if roll_no %2==0:
#             print('class', class_no,'roll_no',roll_no)

# for class_no in range(1,11):
#     if class_no % 2 ==1:
#         print(class_no,'class')
#         for roll_no in range(1,31):
#             print('class', class_no,'roll_no',roll_no)
        
        
# for class_no in range(1,11):
#     print(class_no,'class')
#     if class_no % 2 ==1:
#         for roll_no in range(1,31):
#             print('class', class_no,'roll_no',roll_no)   # skip the even class rooms  #not efficient


# for class_no in range(1,11):
#     print(class_no,'class')
#     for roll_no in range(1,31):
#             if class_no % 2 ==1:
#                 print('class', class_no,'roll_no',roll_no)  #more efficient


# for class_no in range(1,11):
#     if class_no % 3 == 0:
#         print(class_no,'class')
#         for roll_no in range(1,31):
#             if roll_no > 15:
#                 print('class', class_no,'roll_no',roll_no)



# for class_no in range(1,11):
#     print(class_no,'class')
#     for roll_no in range(1,31):
#         if roll_no > 15 and class_no % 3 == 0:
#             print('class', class_no,'roll_no',roll_no)

# class_no = 1
# while  class_no < 11:
#     print(class_no,'class')
#     roll_no = 1  # once iteration is complete  roll no is reset to 1
#     while roll_no < 31:
#         print('class', class_no,'roll_no',roll_no)
#         roll_no+=1
#     class_no+=1



# class_no = 1
# roll_no = 1
# while  class_no < 11:
#     # print(class_no,'class')
#     while roll_no < 31:
#         print('class', class_no,'roll_no',roll_no)    # only print class- 1 but   roll no are print(1-30) not reclll the remaining  loop
#         roll_no+=1
#     class_no+=1



# Jump statements:--->  break , continue , pass


class_no = 1
while  class_no < 11:
    print(class_no,'class')
    continue
    roll_no = 1  # once iteration is complete  roll no is reset to 1
    while roll_no < 31:
        print('class', class_no,'roll_no',roll_no)
        roll_no+=1
    class_no+=1
    break



