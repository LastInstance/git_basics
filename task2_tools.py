def adding():
    x = float(input('First number: '))
    y = float(input('Second number: '))
    print(x + y)

def subtraction():
    x = float(input('First number: '))
    y = float(input('Second number: '))
    print(x - y)
def multiplication():
    x = float(input('First number: '))
    y = float(input('Second number: '))
    print(x * y)
def division():
    x = float(input('First number: '))
    y = float(input('Second number: '))
    if y == 0:
        print('Incomplete operation')
    else:
        print(x / y)

def exponention():
    x = float(input('First number: '))
    y = float(input('Second number: '))
    print(x ** y)

operation = (input('Chose operation: '))
if operation == '+':
    adding()
elif operation == '-':
    subtraction()
elif operation == '*':
    multiplication()
elif operation == '/':
    division()
elif operation == '^':
    exponention()


else:
    print('Goodbye')