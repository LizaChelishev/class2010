def circum_of_a_rectangle(height, width):
    _circum = height * 2 + width * 2
    return _circum


width = float(input('Enter the width: '))
height = float(input('Enter the height: '))
circum = circum_of_a_rectangle(height, width)
print(f'The circum of the rectangle is {circum}')
