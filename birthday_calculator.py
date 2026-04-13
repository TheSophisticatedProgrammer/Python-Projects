from datetime import date
today = date.today()

birth_year = int(input('Enter your birth year: '))
birth_month = int(input('Enter your birth month: '))
birth_day = int(input('Enter your birth day: '))
age = today.year - birth_year

if birth_month > today.month:
    age -= 1
elif birth_month == today.month:
    if birth_day > today.day:
        age -= 1

print(f'your age is {age}')