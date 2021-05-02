def deposite(money, years):
    return money + money * 0.1 * years


m = float(input('Введите сумму денег\n'))
y = float(input('Введите количество лет\n'))

print('Итоговая сумма', deposite(m, y))
