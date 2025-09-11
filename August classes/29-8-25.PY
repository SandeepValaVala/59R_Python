# functions
# --------scope---------------

# num1 = 10
# def test_function():
#     num1 = 20
#     def inner_function():
#         num1 =45
#         print(num1)
#     inner_function()
#     print(num1)
    
# test_function()
# print(num1)


# in the same time work on local and global-------------

# num1 = 10
# def test_function():
#     num1 = 0
#     globals()['num1']=20
#     print(num1)
    
# test_function()
# print(num1)

# ----work on only global|\/| /\ |\| |---------->
# num1 = 10
# def test_function():
#     global num1
#     num1 = 0
#     globals()['num1']=20
#     print(num1)
    
# test_function()
# print(num1)

# def outer function

# num2= 35
# def printer():
#     num2 =35
# def test_function():
#     num2 = 35
#     def inner_function():
#         nonlocal num2
#         num2 =45
#         print(num2)
#         print('inner function')
#     inner_function()
#     print(num2)
    
# test_function()
# print(num2)
# print(num1)




# 