def area_of_a_rectangle(width, height):
     _area = width * height
     return _area

width = float(int('Enter the width: '))
height = float(int('Enter the height: '))

area = area_of_a_rectangle(width, height)
print(f'The area of the rectangle is {area}')