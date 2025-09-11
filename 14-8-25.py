# def vote (age):
#     if age >= 18 :
#         print("vote")
#     else:
#         print("not vote")
# vote(19)
# vote(17)

# def sum (a,b,c):   #  wrong
#     if a > b :
#         return True

# sum(2,5,7)

# res =a+b

# if sum == True :
#     print(res)
# else:
#     print(res)


# def sum_big_number(a, b, c):
#     total = 0
#     if a > b and a > c:
#         total += a
#         if b > c:
#             total += b
#         else:
#             total += c
#     elif b > a and b > c:
#         total += b
#         if a > c:
#             total += a
#         else:
#             total += c
#     else:
#         total += c
#         if b > a:
#             total += b
#         else:
#             total += a
#     return total   # return instead of relying on outer variable

# print(sum_big_number(3, 1, 7))
  
  
  
# def sum_big_number(a,b,c):
#     sum = 0
#     if a>b and a>c:
#         sum+= a
#         if b>c:
#             sum += b
#         else:
#             sum += c
#     elif b>a and b>c:
#         sum+=b
#         if a>c:
#             sum+=a
#         else:
#             sum+=c
#     else:
#         sum+=c
#         if b>a:
#             sum+=b
#         else:
#             sum+=a
#     return sum

# print(sum_big_number(7, 1, 3))
# print(sum_big_number(3, 1, 7))


# def is_palindrome(s):
#     s = s.lower()  
#     n = len(s)
#     for i in range(n // 2):  
#         if s[i] != s[n - 1 - i]:
#             return False
#     return True

# print(is_palindrome("madam"))   
# print(is_palindrome("hello"))   


# n = input("enter a name:")
# res = ""
# for i in range(len(n)-1,-1,-1):
#     res += n[i]
# if res == n:
#     print("yes")
# else:
#     print("no")

# amount = int(input("enter a amount:"))
# cost = amount
# wrapper = amount
# while wrapper >= 3:
#     extra = wrapper//3
#     cost += extra
#     wrapper = extra + wrapper%3
# print(cost)
