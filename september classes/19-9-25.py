
# Wap  to find  repeated values in a list:---
# I/P : [1,2,3,4,3,6,7,2]
# num = list(map(int,input().split())) #1 2 3 4 3 6 7 2
# o/p: [2,3]

# num = [1,2,3,4,3,6,7,2]
# d = []
# for i in num:
#     if num.count(i)>1:
#         if i not in d:
#             d.append(i)
# print(d)   #[2, 3]
# print(*d)   #2 3

# -------------list convert to  int using dict-----------

# num = [1,2,2,3,3,4]
# dict = {} # {1:1, 2: 2, 3: 3 ,4: 1}
# for i in num:
#     if i in dict:
#         dict[i]+= 1
#     else:
#         dict[i] = 1
# # print(dict)  # using for frequency/count---{1: 1, 2: 2, 3: 2, 4: 1}

# for i in dict:
#     if dict[i]>1:
#         print(i,end=" ")  #  2 3 
        

#Wap to sum of digits of list elements-----
# I/p :[12,3,202,399]
# o/p :[3,3,4,21]



# num = [12,3,202,399]
# d = []

# for i in num:
#     s = 0
#     while i > 0:
#         rem = i % 10
#         s += rem
#         i = i // 10
#     d.append(s)
# print(d)  # [3, 3, 4, 21]


# --------list  convert to string-------

# l = [12,3,202,399]

# for i in l:
#     res = 0  # 1 + 2
#     s = str(i)  # "12"
#     for j in s:
#         res += int(j)
#     print(res,end= " ")       #3 3 4 21    





# WAP function to check  a num is prime or not....
# i/ : 7        4     10           11
# o/p: True     False  False       True


# def isprime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True
# # n = 11
# n = 10
# print(isprime(n))


# ------ print  nearest prime---------

def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
# n = 11
n = 65
# n = 10
if isprime(n) == True:
    print(n)
else:
    left = n - 1  #9
    right = n + 1 #11
    while True:
        if isprime(left) == True:
            print(left)
            break
        if isprime(right) == True:
            print(right)
            break
        left -= 1
        right += 1
