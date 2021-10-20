def get_full_name(fname = 'john', lname = 'doe'):
    return f'{fname} {lname}'
fname = input('Enter your first name: ')
lname = input('Enter your last name: ')
print('Hello, ' + get_full_name(fname, lname))