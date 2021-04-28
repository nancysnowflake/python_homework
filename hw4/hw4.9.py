import random

secret = random.randint(1, 100)
prev = 0

while True:
    num = input('Введите число\n')
    num = int(num)
    if num == secret:
        print('Вы угадали')
        break
    elif prev == 0:
        if abs(num - secret) > 10:
            print('Холодно')
        else:
            print('Тепло')
    else:
        if abs(num - secret) > prev:
            print('Холоднее')
        elif abs(num - secret) < 5:
            print('Жарко')
        else:
            print('Теплее')
    prev = abs(num - secret)
