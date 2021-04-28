z_list = ['*', '/', '+', '-', '0']

while True:
    x = float(input('Введите первое число\n'))
    y = float(input('Введите второе число\n'))
    while True:
        z = input('Введите знак\n')
        if z in z_list:
            if z == '/':
                if y == 0:
                    print('На 0 делить нельзя')
                else:
                    print(x/y)
            elif z == '*':
                print(x*y)
            elif z == '+':
                print(x+y)
            elif z == '-':
                print(x-y)
            break
        else:
            print('Вы ввели некорректный знак')
    if z == '0':
        break
