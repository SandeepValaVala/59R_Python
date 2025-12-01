# num = [1,2,1,3,4,5,5,1]
 
# output -- duplicate: [1, 5]
#           unique: [2, 3, 4]


# --------using count bulit in function-----
# num = [1,2,1,3,4,5,5,1]
# d = []
# u = []
# for i in num:
#      if num.count(i)>1:
#          if i not in d:
#              d .append(i)
#      else:
#          u.append(i)
# # print("duplicate:", d)
# # print("unique:", u)
# print("duplicate:", *d)
# print("unique:", *u)


# -----using dictionaries----------

# num = [1,2,1,3,4,5,5,1]
# d = []
# u = []
# dict = {}
# for i in num:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
# # print(dict)
# for i in dict:
#     if dict[i]> 1:
#         d.append(i)
#     else:
#         u.append(i)

# print("duplicate:", *d)
# print("unique:", *u)


# -------without using slicing and  reverse function can print it reverse a list-----

# num = [1,1,1,2,3,4,5,5]
# output: 5 5 4 3 2 1 1 1

# ------------- 1- apporach----------


# num = [1,1,1,2,3,4,5,5]
# rev = num[::-1]  # slice to reverse
# print(*rev)
# ------------- 2- apporach----------

# num = [1,1,1,2,3,4,5,5]
# rev = []
# for i in range(len(num)-1,-1,-1):
#     rev.append(num[i])
# print(*rev)

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



# ------------- 2 -pointer - apporach---------- find  using this palindrome ,cube root ,bubble sort
# num = [1,1,1,2,3,4,5,5]
# i = 0
# j = len(num) - 1
# while i < j:
#     num[i],num[j] = num[j],num[i]
#     j -= 1
#     i += 1
# print(*num)


# ---smallest and largest elements in a list----------
l = [100, 1000 , 999 , 99 ,9 ,10]  #output : 9 , 1000

# max = l[0] #1000
# min = l[0] #100
max = float("-inf") #1000
min = float("inf") #100
for i in l:
    if i >max :
        max = i
    elif i < min:
        min = i
print(min,max)


