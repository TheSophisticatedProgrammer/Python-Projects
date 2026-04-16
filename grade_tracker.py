def add_student():
    try:
        name = input('Name: ')
        grade = int(input('Grade: '))
        students[name] = grade
    except ValueError:
        print('Grade must be a whole number.')

def view_students():
    if not students:
        print('Nothing here yet.')

    for name, grade in students.items():
        print(f'-{name}: {grade}')

def get_highest():
    highest_grade = max(students.values())
    highest_name = [name for name, grade in students.items() if grade == highest_grade]
    return highest_name, highest_grade

def get_lowest():
    lowest_grade = min(students.values())
    lowest_name = [name for name, grade in students.items() if grade == lowest_grade]
    return lowest_name, lowest_grade

def stats_students():
    try:
        average = sum(students.values()) / len(students)

        highest_name, highest_grade = get_highest()
        lowest_name, lowest_grade = get_lowest()

        print(f'Average: {average}')

        print(f'Highest: {','.join(highest_name)} ({highest_grade})')
        print(f'Lowest: {','.join(lowest_name)} ({lowest_grade})')

    except (ZeroDivisionError, ValueError):
        print('Nothing here yet.')

students = {}
actions = {
    'add': add_student,
    'view': view_students,
    'stats': stats_students
}

while True:
    options = '/'.join(actions)
    action = input(f'What do you want to do? ({options}/quit): ')

    if action == 'quit':
        break

    if action in actions:
        actions[action]()
    else:
        print('Unknown command, please try again.')