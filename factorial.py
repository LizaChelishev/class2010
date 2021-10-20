
def get_factorial(x):
    atz = 1
    for x in range (1, x+1):
        atz *= x
    return atz
x = int(input('Enter a positive integer number: '))
atz = get_factorial(x)
print(f'The factorial of {x} is {atz}')
