# n = 5

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*",end =" ")
#     print()

# n = 5
# for i in range (1, n+1):
#     for j in range(1, n-i+2):
#         print("*",end =" ")
#     print()



# ---------single for loop-----------
# n = 5
# for i in range(1,n+1):
#     print("*"*i)

# n = 5
# for i in range(n,0,-1):
#     print("*"*i)



# ------- square pattern---------------
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end="  ")
#     print()

n = 5
for i in range(1,n+1):
    if i == 1 or i == n:
        print("*"*n)
    else:
        print("* "+"   "*(n-2)+"*")