# t1 = (1, 2, 3,)
# l1 = [1, 2, 3]
# t1 = 1, 2, 3
# t1 = tuple((1, 2, 3))
# t1 = ()
# t1 = (1,)
# t1 = (1, 2, 3)

# print(t1.__sizeof__())
# print(l1.__sizeof__())

# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
#
# print(t3)
# print(t3.count('l'))
#
# if 'l' in t3:
#     print(t3.index('l'))
# else:
#     print('No')
#
# for i in t3:
#     if i == ' ':
#         continue
#     print(f'"{i}"', end=' ')


# t1 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t1, id(t1))
# t1[4][0] = 'new'
# t1[4].append('hello')
# print(t1, id(t1))

# t1 = (1, 2, 3,)
# x, y, z = t1
#
# print(x, y, z)

# x = 1
# y = 2
#
# print(x, y)
# x, y = y, x
# print(x, y)

"""
Дан список words. Составьте из него список слов-палиндромов. Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
"""

words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']


#1
pal = []

for word in words:
    if word == word[::-1]:
        pal.append(word)
print(pal)

ppal = [word for word in words if word == word [::-1]]
print(ppal)

#2
pppal = []

for word in my_str:
    worda = word.replace(' ', '').lower()
    if worda == worda[::-1]:
        pppal.append(word)

print(pppal)


