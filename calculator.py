def int_possible(num): # functions
    if num.is_integer():
        return int(num)
    return num

def calculate(operation):
    
    try:
        x = float(input('Enter first number: '))
        y = float(input('Enter second number: '))
        return int_possible(operation(x, y))
    except ValueError:
        print('ValueError: please enter a number.')
    except ZeroDivisionError:
        print('ZeroDivisionError: cannot divide by zero.')

def add():
    return calculate(lambda x, y: x + y)

def subtract():
    return calculate(lambda x, y: x - y)

def multiply():
    return calculate(lambda x, y: x * y)

def divide():  
    return calculate(lambda x, y: x / y)

def power():    
    return calculate(lambda x, y: x ** y)

actions = { # map out functions
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'power': power
}

while True:
    action = input(f'What do you wanna do: ({'/'.join(actions)}/quit:) ').lower()

    if action == 'quit':
        break

    if action in actions:
        result = actions[action]()
        if result != None:
            print(result)
    
    else:
        print('Unknown command: please try again')
