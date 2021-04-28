numbers = []

while True:
    num = input()
    if num == '0':
        break
    numbers.append(int(num))

s = sum(numbers)
print('sum =', s)

