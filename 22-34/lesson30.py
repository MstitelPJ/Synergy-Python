# https://docs.python.org/3/library/

# import os
# import random as r
# import random
# from random import randint, shuffle
# from random import *

# print(os.getcwd())
# # print(random.randint(1, 100))
#
# print(randint(1, 100))
# l = [1, 2, 3, 4, 5]
# shuffle(l)
# print(l)


import libs
# print(__name__)
# print(libs.get_count('hello', 'l'))
# print(libs.get_len('hello'))

# f = libs.get_count
# print(f('hello', 'l'))
#
#
# def get_sum(a, b):
#     return a + b
#
#
# func = get_sum
# print(func(1, 2))



import random

x = random.randint(0, 100)
user_num = 0
cnt = 0

while True:
    user_num = int(input('Я загадал число от 1 до 100 - угадай его: '))
    cnt += 1
    if user_num == x:
        print(f'Ты угадал число за {cnt} попыток')
        print('Спасибо за игру')
        break
    elif user_num > x:
        print('Мое число меньше')
    else:
        print('Мое число больше')