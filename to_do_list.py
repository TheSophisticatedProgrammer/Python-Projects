import os
lists = []

def load_tasks():
    global lists

    if os.path.exists('tasks.txt'):
        
        with open('tasks.txt', 'r') as file:
            lists = [line.strip() for line in file] 

def save_tasks():

    with open('tasks.txt', 'w') as file:
        for task in lists:
            file.writelines(task +  '\n')

def add_task():
    add_input = input('Enter task: ')
    lists.append(add_input)
    save_tasks()

def view_tasks():

    if not lists:
        print('Nothing here yet...')
    else:
        for task in lists:
            print(task)

def delete_tasks():
    delete_input = input('Enter task: ')

    if delete_input in lists:
        lists.remove(delete_input)

    save_tasks()

load_tasks()

actions = {
    'add': add_task,
    'view': view_tasks,
    'delete': delete_tasks
}

while True:

    options = '/'.join(actions)
    action = input(f'What do you want to do ({options}/quit): ').lower()

    if action == 'quit':
        break

    elif action in actions:
        actions[action]()

    else:
        print('Unknown command, please try again.')