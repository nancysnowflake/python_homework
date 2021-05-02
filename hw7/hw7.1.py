season_dict = {
    '1': 'Зима',
    '2': 'Зима',
    '12': 'Зима',
    '3': 'Весна',
    '4': 'Весна',
    '5': 'Весна',
    '6': 'Лето',
    '7': 'Лето',
    '8': 'Лето',
    '9': 'Осень',
    '10': 'Осень',
    '11': 'Осень'
}


def season(month_number):
    if month_number in season_dict:
        return season_dict[month_number]
    else:
        return 'Такого месяца не существует'


month = input('Введите номер месяца\n')

print(season(month))
