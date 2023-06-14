# def f(x):
#     return x*x
# a = f
# print(type(f))
# print((f(5)))
# print(type(a))
# print((a(5)))


# def calk1(a, b):
#     return a + b


# def calk2(a, b):
#     return a * b


# def math(op, x, y):
#     print(op(x, y))


# math(calk1, 5, 45)
# math(calk2, 5, 45)

# calk1 = lambda a,b: a+b
# calk2 = lambda a,b: a*b


# print(calk1(5,10))
# print(calk2(5,10))


# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a+ b, 5, 45)

'''
В списке хранятся числа. Нужно выбрать только четные числа и составить список пар (число, квадрат числа).
'''
# my_list = [1,2,3,5,8,15,23,38]
# new_list = []
# for i in my_list:
#   if i % 2 == 0:
#       new_list.append((i, i**2))      
# print(new_list)


# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# my_list = [1,2,3,5,8,15,23,38]
# res = select(int, my_list)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)
'''
Сокращенный вариант 1
'''

# def where(f, col):
#     return [x for x in col if f(x)]

# my_list = [1,2,3,5,8,15,23,38]
# res = list(map(int, my_list))
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)




# list_1 = [x for x in range(1,10)]
# print(list_1)

# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

'''
С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. Этот набор чисел будет считан в качестве строки. как превратить list строк в list чисел
'''

# input_str=(input('Введите набор чисел через пробел: '))
# list_int = list(map(int, input_str.split()))
# print(list_int)




# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)


'''
Сокращенный вариант 2
'''
# my_list = [1,2,3,5,8,15,23,38]
# res = (map(int, my_list))
# res = (filter(lambda x: x % 2 == 0, res))
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# my_list = list(zip([1,2,3], ['ф','о','в'], ['a', 'f', 'g']))
# print(my_list)

# print(list(enumerate(['Казань', 'Москва', 'Смоленск', 'Уфа'])))

'''
Работа с файлами
'''
colors = ['red', 'green', 'blue']
data = open('file.txt','a')
data.writelines(colors)
data.close()

with open('file.txt','w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
print(56)


data = open('file.txt','r')
for line in data:
    print(line)
data.close()