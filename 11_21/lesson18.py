"""
1. Дан список. Получите новый список, в котором каждое значение будет удвоено:
[1, 2, 3] --> [2, 4, 6]
"""
a = [1, 2, 3]
a2 = [i * 2 for i in a]
print(a2)
"""
2. Дан список. Возведите в квадрат каждый из его элементов и получит сумму всех полученных квадратов:
[1, 2, 3] --> 14 --> 1^2 + 2^2 + 3^2 = 14
"""
s = [1, 2, 3]
s2 = [i ** 2 for i in s]
print(sum(s2))
"""
3. Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвоживания и пьет 0,5 литра воды в час. Вам дается время в часах, и вам нужно вернуть количество литров, которые Игорь выпьет, с округлением до наименьшего значения.
time1 = 3 --> litres = 1
time2 = 6.7 --> litres = 3
time3 = 11.8 --> litres = 5
"""
time1 = 3
time2 = 6.7
time3 = 11.8
print(int(time1 // 2), end=' ')
print(int(time2 // 2), end=' ')
print(int(time3 // 2))
"""
4. Дана строка 'Hello world'. Проверьте, если в этой строке есть символ пробела - " ", тогда преобразуйте строку к верхнему регистру, если же нет, тогда к нижнему.
***************
s = 'Hello world'
if stm:
	pass
else:
	pass
"""

g = 'Hello world'
if ' ' in g:
    g = g.upper()
else:
    g = g.lower()

print(g)