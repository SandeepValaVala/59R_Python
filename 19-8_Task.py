# Python Assignment :
# 1.Write a program to check the three sides will form a valid triangle and 
# also check wheather the triangle is isosceles or equivalent or right angled.

def valid_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print("It is a valid triangle")
        if a == b == c:
            print("It is a Equivalent Triangle")
        elif a == b or b == c or a ==c:
            print("It is a Isosceles Triangle")
        else:
            print('It is a Scalene Triangle')
        if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
            print('It is a Right-angled Triangle')
        else:
            print('It is not a Right-angled Triangle')
    else:
        print('It is not a valid triangle')

valid_triangle(3,4,5)


