'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
'''

# quantity_1 = int(input('Введите количeсто элементов первого множества: '))
# quantity_2 = int(input('Введите количество элементов второго множества: '))
# numbers_1 = input('Введите элементы первого множества (целые числа) через пробел: ').split()
# numbers_2 = input('Введите элементы второго множества (целые числа) через пробел: ').split()
# if len(numbers_1) == quantity_1 and len(numbers_2) == quantity_2:
#     numbers_1 = [int(item) for item in numbers_1]
#     numbers_2 = [int(item) for item in numbers_2]
#     print(*numbers_1)
#     print(*numbers_2)
#     result = list(set(numbers_1).intersection(set(numbers_2)))
#     result.sort()
#     print(*result)
# else:
#     print('Введенное количество элементов не соответствует заданному значению!')

'''Эталонное решение'''
# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()

# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')

'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
4 -> 1 2 3 4
9
'''


'''Для закрепления понимания словаря'''
# from random import randint
# bushes = int(input('Введите количество кустов черники на грядке: '))
# bushes_with_berries = {}
# bush = 1
# while bush <= bushes:
#     bushes_with_berries[bush] = randint(0, 10)
#     bush += 1
# print(f'Урожайность кустов (куст: количество ягод): {bushes_with_berries}')
# bush = 2
# berries_max = 0
# while bush < bushes:
#     berries_summ = bushes_with_berries[bush] + bushes_with_berries[bush-1]+ bushes_with_berries[bush+1] 
#     if berries_summ > berries_max:
#         berries_max = berries_summ
#     bush += 1
# print(f'За один заход масимально можно собрать следующее количество ягод: {berries_max}')

'''Эталонное решение'''
n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)

arr_count = list()
for i in range(len(arr)-1):
    arr_count.append(arr[i-1]+arr[i]+arr[i+1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))
