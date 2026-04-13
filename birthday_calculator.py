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

birthdate = date(today.year, birth_month, birth_day) # next birthday

if birthdate <= today:
    print(f'Your next birthday is: {birth_day}/{birth_month}/{today.year + 1}')
else:
    print(f'Your next birthday is: {birth_day}/{birth_month}/{today.year}')

days_to_birthdate = (birthdate - today).days
if days_to_birthdate != 0:
    print(f'{days_to_birthdate} days until next birthday')
else:
    print(f'365 days until next birthday')
