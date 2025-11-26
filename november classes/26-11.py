# x = 11

# assert x < 10, 'x is greater than 10'  #AssertionError: x is greater than 10



# ---1 to 10  natural numbers-----

# custom iterators

# class Point():
#     def __add__(self, others):


# p1 = Point()
# p2 = Point()

# print(p1 +p2)

# # 0 to 100

# class NaturalNumbersIter():
#     def __init__(self):
#         self.curr_value = 0
        
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.curr_value > 5:
#             raise StopIteration('100 values are already given')
        
#         temp = self.curr_value # temp = 0 #1 #2
#         self.curr_value += 1 # curr_value = 1 #2#3
#         return temp #0 #1#2
    
    
# n1 =  NaturalNumbersIter() #n1.curr_value = 0

# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))


# # n2 =  NaturalNumbersIter()

# # 0 to 100

# class NaturalNumbersIter():
#     def __init__(self,limit):
#         self.curr_value = 0
#         self.limit = limit
        
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.curr_value > self.limit:
#             raise StopIteration('100 values are already given')
        
#         temp = self.curr_value # temp = 0 #1 #2
#         self.curr_value += 1 # curr_value = 1 #2#3
#         return temp #0 #1#2
    
    
# n1 =  NaturalNumbersIter(5) #n1.curr_value = 0

# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))


# # n2 =  NaturalNumbersIter()

# 27 to 255

# class NaturalNumbersIter():
#     def __init__(self,start_value,end_value):
#         self.curr_value = start_value
#         self.limit = end_value
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.curr_value > self.limit:
#             raise StopIteration('100 values are already given')
        
#         temp = self.curr_value # temp = 0 #1 #2
#         self.curr_value += 1 # curr_value = 1 #2#3
#         return temp #0 #1#2
    
    
# n1 =  NaturalNumbersIter(27,255) #n1.curr_value = 0

# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))


# # n2 =  NaturalNumbersIter()
# 27 to 255

# class NaturalNumbersIter():
#     def __init__(self,start_value,end_value):
#         self.curr_value = start_value
#         self.limit = end_value
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.curr_value > self.limit:
#             raise StopIteration('100 values are already given')
        
#         temp = self.curr_value # temp = 0 #1 #2
#         self.curr_value += 3 # curr_value = 
#         return temp #0 #1#2
    
    
# n1 =  NaturalNumbersIter(27,255) #n1.curr_value = 0

# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))

# ----reverse iteration----


# class NaturalNumbersIter():
#     def __init__(self,start_value,end_value):
#         self.curr_value = start_value
#         self.limit = end_value
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.curr_value < self.limit:
#             raise StopIteration('reverse iteration')
        
#         temp = self.curr_value # temp = 0 #1 #2
#         self.curr_value -= 3 # curr_value = 
#         return temp #0 #1#2
    
    
# n1 =  NaturalNumbersIter(45,27) #n1.curr_value = 0

# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))

# Generator
# yeild 

# def gen1():
#     print('zero line')
#     print('first line')
#     print('second line')
    
#     yield 1
#     print('hi')
#     yield 2
#     yield 3
    
    
# g1 = gen1()
# print(next(g1))
# print('second call')
# print(next(g1))
# print(next(g1))


def gen1():
    curr_num = 0
    
    while curr_num <= 5:
        yield curr_num
        curr_num += 1

g1 = gen1()
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))