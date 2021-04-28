numbers = input('Введите список чисел через пробел\n')
k = input('Введите индекс k\n')
k = int(k)

numbers = numbers.split()

i = 0
while i < len(numbers):
    if i > k:
        numbers[i-1] = numbers[i]
    i += 1

numbers.pop()

print(' '.join(numbers))
