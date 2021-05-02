def prime(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return True


num = int(input('Введите число от 0 до 1000\n'))
if num < 0 or num > 1000:
    print('Число должно быть в диапазоне от 0 до 1000')
else:
    if prime(num) == True:
        print('Число простое')
    else:
        print('Число не является простым')