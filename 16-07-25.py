#  ordered

dict1 ={
    
    1:'pawn kalyan',
    2:'mahesh babu',
    3:'AA',
    4:'Dhanush',
    5:'mohan babu',
    6:'surya',
    '7':'surya',
    3:'prabhas'
}

print(dict1)
print(dict1[5])
#print(dict1['mohan babu]) 

dict1['7'] = 'Allu Arjun'
print(dict1)

# dict1 ={
    
#     1:['pawn kalyan', 'AA'],
#     2:'MAHESH'
# }
# dict1[1][1] = 'pspk'
# print(dict1)

#set is a collection of unorderd,unique,finite elements
# set is mutable but set will take only immutable elements as its members
#set is not indexable 


# set1 = {1, 2, 1.5, 'string1', 1, 1, 1, 'string2'}
# print(set1)     #{1, 2, 1.5, 'string2', 'string1'} key value doesn't take any duplicate values in unordered

# # set1=set()
# # dict1={}

# # Frozenset => immutable

# # F1 = frozenset([1, 2, 3, 1, 'str1', 'str2'])
# # print(F1)

# s2 = {1, 2, 3,{ 8, 9}}
# print(s2)