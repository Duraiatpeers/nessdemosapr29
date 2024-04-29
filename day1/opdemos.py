'''
Operators
    Arithmetic -> +,-,*,/,%,**
    Assignment -> =, +=, -=,
    Comparison -> >, <, <=, >=, ==, !=
    Logical -> and, or, not
    Identity -> is, is not
    Membership -> in, not in
    Bitwise -> |, &
'''

x = 100
x += 10  # x = x + 10
print(x)

x *= 4
print( 3 * 4)
print( 2 ** 3)
print(x)

a = 100
b = 200

if(a > b):
    print('a is bigger')
else:
    print('b is bigger')

age = 19
gender = 'female'

if(age < 23 and age > 18 and gender == 'female'):
    print('Eligible for scholarship')

old_city = 'madrid'
new_city = old_city

print(new_city is old_city)

old_city = 'madrid'
new_city = 'madrid'

print(new_city is old_city)

old_city = 'madrid'
new_city = 'chester'

print(new_city is old_city)

city_list = ['chester','manchester','liverpool']
print('manchester' not in city_list)

x = (20 + 2) * 3
print(x)

x = 10 + 10 * 3 ** 2
print(x)

x = (10 + 10) * 3 ** 2
print(x)

