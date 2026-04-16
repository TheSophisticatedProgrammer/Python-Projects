def add_item():
    add_input = input('Item: ')
    shopping_list.append(add_input)
    print('Added!')

def remove_item():
    try:
        remove_input = input('Item: ')
        shopping_list.remove(remove_input)
    except ValueError:
        print('Does not exist.')

def view_items():
    if not shopping_list:
        print('Nothing here yet.')
    else:
        for item in shopping_list:
            print(f'- {item}')

shopping_list = []

actions = {
    'add': add_item,
    'remove': remove_item,
    'view': view_items
}

while True:
    options = '/'.join(actions)
    action = input(f'What do you wanna do {options}/quit: ').lower()

    if action == 'quit':
        break

    if action in actions:
        actions[action]()

    else:
        print('Unknown command, please try again.')