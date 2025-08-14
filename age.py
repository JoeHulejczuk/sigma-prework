from datetime import date

today = date.today()


def age_calc():
    given_date = input(
        'Enter a date in the following format (DD-MM-YYYY) ').strip()

    given_day = int(given_date[:2])
    given_month = int(given_date[3:5])
    given_year = int(given_date[6:])

    age = int(today.year) - int(given_year)

    if given_month >= int(today.month):
        if given_day > int(today.day):
            age -= 1

    return (f'The age of someone born on {given_date} is {age} ')


print(age_calc())
