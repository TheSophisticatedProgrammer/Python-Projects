contacts = {}

def add():
    add_input = input('Enter name: ')
    number = input('Enter number: ')
    contacts[add_input] = number
    print('Contact saved!')

def lookup():
    try:
        lookup_input = input('Enter name:')
        print(f'{lookup_input}\'s number is {contacts[lookup_input]}')
    except KeyError:
        print('That contact does not exist.')

def delete():
    try:
        delete_input = input('Enter name:')
        del contacts[delete_input]
        print(f'{delete_input}\'s contact has been deleted.')
    except KeyError:
        print('That contact does not exist.')

def view():
    if not contacts:
        print('No contacts')
    else:
        for name, number in contacts.items():
            print(f'{name}: {number} ')

while True:
    action = input('What do you want to do? (add/lookup/delete/view/quit): ')

    if action == 'add':
       add()
    elif action == 'lookup':
        lookup()
    elif action == 'delete':
        delete()
    elif action == 'view':
        view()
    elif action == 'quit':
        break
    else:
        print('Unknown command, try again.')