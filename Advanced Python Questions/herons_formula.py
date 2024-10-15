import math
def calculate_triangle_area(a, b, c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

area = calculate_triangle_area(5,6,8)
print("The area is:", area)