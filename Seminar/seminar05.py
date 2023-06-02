'''
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0 , a1 , ..., an , ...,
где a0  = 0, a1  = 1, ak  = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
'''

# import module_function
# number = int(input('Введите число: '))
# print(module_function.fib_number(number))



'''
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

# from random import randint
# quantity = int(input('Введите количество отметок: '))
# grades =[int(randint(1,5)) for i in range(quantity)]
# print(grades)
# a = max(grades)
# b = min(grades)
# for i in range(quantity):
#     if grades[i] == a:
#         grades[i] = b
# print(grades)

# from random import randint
# quantity = int(input('Введите количество отметок: '))
# grades =[int(randint(1,5)) for i in range(quantity)]
# grades_new = []
# a = max(grades)
# b = min(grades)
# print(grades)
# for item in grades:
#     if item == a:
#           grades_new.append(b)
#     else:
#          grades_new.append(item)
# print(grades_new)

'''
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
'''
# from module_function import prime_number
# number = int(input('Введите число: '))
# if prime_number(number) == True:
#     print('Это простое число')
# else:
#    print('Это не простое число')


'''
Задача №37. Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''
# from module_function import reverse_range
# number = int(input('Введите число: '))
# reverse_range(number)


