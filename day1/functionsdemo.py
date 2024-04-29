def say_hi():
    print('Hi')

say_hi()


def say_hi(firstname,lastname):
    print('Hi ',firstname+' '+lastname)

say_hi('Boris','Becker')


def say_hi(firstname,lastname='Wilander'):
    print('Hi ',firstname+' '+lastname)

say_hi('Matts')

# Arbitrary argument * args
def say_hi(*names):
    print(type(names))
    for name in names:
        print(name)

say_hi('Carl lewis','Ben Johnson','Desmond Haynes')


# Keyword arguments ** args
def say_hi(firstname, lastname):
    print(firstname+' '+lastname)

say_hi(firstname = 'Gordon', lastname='Greenidge')

def say_hi(**name):
    print(name['firstname']+' '+name['lastname'])
    return name['firstname']+' '+name['lastname']

new_data = say_hi(firstname = 'Pete', lastname='Sampras')
print(new_data)


def calc(*marks):
    pass

calc([90,100,80])


result = lambda num1,num2: num1 + num2
print(result(10,20))

next_year  = lambda year: year + 1
print(next_year(2024))