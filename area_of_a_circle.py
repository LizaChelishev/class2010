import math

def area_of_a_circle(radius):
    _area = math.pi * (radius**2)
    return _area


radius = float(input('What is the circles radius? '))
area = area_of_a_circle(radius)
print(f'The area of the circle is {area}')