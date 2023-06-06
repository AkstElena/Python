'''
Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an  = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''
# first_element = int(input('Введите первый элемент прогрессии: '))
# step = int(input('Введите шаг прогрессии: '))
# quality = int(input('Введите количество элементов прогрессии: '))
# my_list = []
# for i in range(quality):
#     my_list.append(first_element+i*step)
# print(*my_list)

'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''
from random import randint
quality = int (input('Введите количество элементов массива: '))
my_list = [int(randint(-100, 100)) for i in range(quality)]
print(my_list)
index_list = []
number_min = int (input('Введите минимум: '))
number_max = int (input('Введите максимум: '))
for i in range(len(my_list)):
    if my_list[i] <= number_max and my_list[i] >= number_min:
        index_list.append(i)
print(index_list)