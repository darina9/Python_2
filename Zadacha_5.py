import random

list = ['мышка', 'сосиска', 'собачка', 'жвачка']
print('изначальный список :' + str(list))
for i in range(len(list)-1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
print('измененный список : ' + str(list))
