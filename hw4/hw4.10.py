type = input('Какой из методов сжатия применить? 1 или 2?\n')

if type == '1':
    text = input('Введите текст\n')
    text = text.split()
    result = []
    for word in text:
        newWord = ''
        i = 1
        c = 1
        while i < len(word):
            if word[i] == word[i-1]:
                c += 1
            elif c > 1:
                newWord += word[i-1] + str(c)
                c = 1
            else:
                newWord += word[i-1]
            i += 1
        if c > 1:
            newWord += word[i-1] + str(c)
        else:
            newWord += word[i - 1]
        result.append(newWord)
    print(' '.join(result))
elif type == '2':
    numbers = input('Введите числа через пробел\n')
    numbers = numbers.split()
    i = 0
    zeroPosition = -1
    while i < len(numbers):
        if numbers[i] == '0':
            if zeroPosition == -1:
                zeroPosition = i
        elif zeroPosition != -1:
            numbers[zeroPosition] = numbers[i]
            numbers[i] = '0'
            zeroPosition += 1
        i += 1
    print(' '.join(numbers))
else:
    print('Некоректный метод')
