n = input('Введите n\n')
n = int(n)

i = 1
sum = 0
while i <= n:
    sum += i
    i += 1

print(sum, int(n * (n + 1) / 2))
