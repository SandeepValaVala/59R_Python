# r = 3
# c = 3
# l = [[1,2,3],[4,5,6],[7,8,9]]
# print(l)
# for i in range(0,r):
#     for j in range(0,c):
#         l[i][j] = 0
# print(l)   #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# num = [12,3,202,399]
# d = []

# for i in num:
#     s = 0
#     while i > 0:
#         rem = i % 10
#         s += rem
#         i = i // 10
#     d.append(s)
# print(d) 

# r = 3
# c = 3
# l = [[1,2,3],[4,5,6],[7,8,9]]   # o/p :- [6,15,24]  
# for i in range(r):
#     sum = 0
#     for j in range(c):
#         sum += l[i][j]
#     print(sum,end=" ")  #6 15 24



# r = 3
# c = 3
# l = [[1,2,3],[4,5,6],[7,8,9]]   # o/p :- [6,15,24]  
# d = []
# for i in range(r):
#     res = 0
#     for j in range(c):
#         res += l[i][j]
#     d.append(res)
# print(d)  #[6, 15, 24]




r = 3
c = 3
l = [[1,2,3],[4,5,6],[7,8,9]]   # o/p :- [12,15,18]  
d = []
for i in range(r):
    res = 0
    for j in range(c):
        res += l[j][i]
    d.append(res)
print(d)