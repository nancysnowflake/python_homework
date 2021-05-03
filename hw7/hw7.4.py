# Написать функцию принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


y = int(input('Введите год\n'))
if y < 1:
    print('Год должен быть больше 0')
else:
    if leap(y) == True:
        print('Год високосный')
    else:
        print('Год не високосный')