# def hello(name, word):
#     print('Hello, ' + name + '. Say ' + word)
#
# hello('John', 'hi')
# hello('Katy', 'hello')


# def get_sum(a, b):
#     print(a + b)


# x = 2
# y = 5
# get_sum(1, 3)
# get_sum(x, y)

# print(len('Hello'))

# def get_sum(a, b):
#     return a + b
#
# print(get_sum(1, 2))

# def hi():
#     print('Hi')
#
# hi()

def h1():
    time1 = 3 # litres = 1
    time2 = 6.7 # litres = 3
    time3 = 11.8 # litres = 5
    print(int(time1 // 2))
    print(int(time2 // 2))
    print(int(time3 // 2))

h1()

def register(s):
    if ' ' in s:
        return s.upper()
    else:
        return s.lower()
print(set_register('Hello world'))
print(set_register('Hello,world'))
