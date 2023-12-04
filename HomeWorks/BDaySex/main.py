from datetime import date, timedelta


users = [{'name': 'Sanya', 'birthday': date(year=1989, month=12, day=11)},
         {'name': 'Irina', 'birthday': date(year=1998, month=12, day=10)},
         {'name': 'Jerry', 'birthday': date(year=1995, month=12, day=6)},
         {'name': 'Toma', 'birthday': date(year=1983, month=12, day=6)},
         {'name': 'Andrii', 'birthday': date(year=1974, month=12, day=12)},
         {'name': 'Serg', 'birthday': date(year=1972, month=12, day=5)},
         {'name': 'Niko', 'birthday': date(year=1964, month=12, day=10)},
         {'name': 'Tolik', 'birthday': date(year=1993, month=12, day=9)},
         {'name': 'Pasha', 'birthday': date(year=1986, month=12, day=8)}
         ]


def get_birthdays_per_week(users_list: list) -> None:

    result = {}
    count = start_index()

    for _ in range(7):
        interval = timedelta(days=count)
        week_day = date.today() + interval
        day = week_day.strftime('%A')
        for user in users_list:
            name = user['name']
            birthday = user['birthday'].replace(year=date.today().year)
            if birthday == week_day:
                if day in ('Saturday', 'Sunday'):
                    next_monday = week_day + timedelta(days=6)
                    next_monday_day = next_monday.strftime('%A')
                    result.setdefault(next_monday_day, [])
                    result[next_monday_day].append(name)
                else:
                    result.setdefault(day, [])
                    result[day].append(name)
        count += 1

    print_birthday(result)


def start_index() -> int:
    week_day = date.today()
    day = week_day.strftime('%A')

    if day == 'Sunday':
        count = -1
    elif day == 'Monday':
        count = -2
    else:
        count = 0

    return count


def print_birthday(birth_dict: dict) -> None:

    for day_of_week in birth_dict.keys():
        print_result = f'{day_of_week}: '
        for name in birth_dict[day_of_week]:
            print_result += f'{name} / '
        print(f'{print_result}\b\b')

get_birthdays_per_week(users)

