from datetime import date
today = date.today()

birth_day = int(input('Enter your birth day: '))
birth_month = int(input('Enter your birth month: '))
birth_year = int(input('Enter your birth year: '))
age = today.year - birth_year

if birth_month > today.month: # age logic
    age -= 1
elif birth_month == today.month:
    if birth_day > today.day:
        age -= 1
print(f'Your age is {age}')

birthdate = date(today.year, birth_month, birth_day) # next birthday logic

if birthdate <= today:
    print(f'Your next birthday is: {birth_day}/{birth_month}/{today.year + 1}')
    next_birthday = date(today.year + 1, birth_month, birth_day)
else:
    print(f'Your next birthday is: {birth_day}/{birth_month}/{today.year}')
    next_birthday = date(today.year, birth_month, birth_day)

days_to_birthdate = (next_birthday - today).days
print(f'{days_to_birthdate} days until your next birthday')
