from random import randint
n = int(input('введите число'))
numbers = []
for i in range(n):
    numbers.append(randint(-n, n))
print(numbers)

x = int(input('введите номер первого элемента: '))
y = int(input('введите номер второго элемента: '))
if x > n or y > n:
    print('такого элемента нет')
else:
    for i in range(len(numbers)):
        multiplication = numbers[x - 1]*numbers[y - 1]
    print(
        f'произведение элементов: {numbers[x -1]} * {numbers[y -1]} =', multiplication)
