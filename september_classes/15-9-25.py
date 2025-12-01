# single  Inheritance =>  
# multilevel Inheritance =>  
# multiple Inheritance =>  
# Hier...  Inheritance
# Hybrid Inheritance

# class A

# ----------------

# class Clac:  #parent class ,super class , base class
#     company = 'CASIO'
#     def add(self , a, b):
#         return a + b
    
#     def mul(self , a, b):
#         return a * b
    
    
    
# class AdvCalc(Clac):  # child class , sub class ,Derived
#     def find_log(self , num):
#         return num / 5
    
    
#     def add (self ,a , b):
#         print('Add from adv calc')
#         return a + b
    
# adv1 = AdvCalc()
# adv1.add(2,3)
# print(adv1.company)


# ----constructor ------- in classes (parent ,child)---------

# class Clac:  #parent class ,super class , base class
#     company = 'CASIO'
#     def __init__(self):
#         print('Parent class constructor called')
    
#     def add(self , a, b):
#         return a + b
    
#     def mul(self , a, b):
#         return a * b
    
    
    
# class AdvCalc(Clac):  # child class , sub class ,Derived
#     def __init__(self):
#         print('child class constructor called')   # method overridding 
    
#     def find_log(self , num):
#         return num / 5
    
    
#     def add (self ,a , b):
#         print('Add from adv calc')
#         return a + b
    
# adv1 = AdvCalc()    
# adv1.add(2,3)
# print(adv1.company)




# -----  self ,id ,manf_date , cmp_power ---
# class Clac:  #parent class ,super class , base class
#     company = 'CASIO'
#     def __init__(self ,id ,manf_date):
#         self.id = id
#         self.manf_date = manf_date
#         print('Parent class constructor called')
    
    # def add(self , a, b):
    #     return a + b
    
#     def mul(self , a, b):
#         return a * b
    
    
    
# class AdvCalc(Clac):  # child class , sub class ,Derived
#     def __init__(self ,id ,manf_date , cmp_power):
#         # self.id = id
#         # self.manf_date = manf_date
#         super().__init__(id,manf_date)
#         self.cmp_power = cmp_power
#         print('child class constructor called')   # method overridding 
    
#     def find_log(self , num):
#         return num / 5
    
    
#     def add (self ,a , b):
#         super().add(a , b)
#         print('Add from adv calc')
#         return a + b
    
# adv1 = AdvCalc( 2, '15-sep',55)    
# adv1.add(2,3)
# print(adv1.company)
# print(adv1.id)
# print(adv1.manf_date)
# print(adv1.cmp_power)

# --------add super class-----------------

class Clac:  #parent class ,super class , base class
    company = 'CASIO'
    def __init__(self ,id ,manf_date):
        self.id = id
        self.manf_date = manf_date
        print('Parent class constructor called')
    
    def add(self , a, b):
        return a + b
    
    def mul(self , a, b):
        return a * b
    
    
    
class AdvCalc(Clac):  # child class , sub class ,Derived
    def __init__(self ,id ,manf_date , cmp_power):
        # self.id = id
        # self.manf_date = manf_date
        super().__init__(id,manf_date)
        self.cmp_power = cmp_power
        print('child class constructor called')   # method overridding 
    
    def find_log(self , num):
        return num / 5
    
    
    def add (self ,a , b):
        super().add(a , b)
        print('Add from adv calc')
        return a + b
    
class SuperClac(AdvCalc):
    pass
    
adv1 = AdvCalc( 2, '15-sep',55)    
adv1.add(2,3)
print(adv1.company)
print(adv1.id)
print(adv1.manf_date)
print(adv1.cmp_power)
# print(AdvCalc.mro())

s1 = SuperClac( 2, '15-sep',55)
s1.add(5,5)
print(s1.id)