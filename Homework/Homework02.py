'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
'''
# quantityMonets = int(input('Введите количество монет:'))
# orel = 0
# reshka = 0
# for i in range(0, quantityMonets):
#     monet = int(input('Если орел напишите цифру 1, если решка напишите цифру 0: '))
#     if monet == 1:
#         orel += 1
#     elif monet == 0:
#         reshka += 1
#     else:
#         print('Введено некорретное значение. Результат некорретен')
#         break
# if orel > reshka:
#     print(f'Минимальное количество монет, которые нужно перевернуть: {reshka}')
# else:
#     print(f'Минимальное количество монет, которые нужно перевернуть: {orel}')


# с использованием random
# from random import randint
# quantityMonets = int(input('Введите количество монет:'))
# orel = 0
# reshka = 0
# for i in range(0, quantityMonets):
#     monet = randint(0, 1)
#     print(monet)
#     if monet == 1:
#         orel += 1
#     else:
#         reshka += 1
# if orel > reshka:
#     print(f'Минимальное количество монет, которые нужно перевернуть: {reshka}')
# else:
#     print(f'Минимальное количество монет, которые нужно перевернуть: {orel}')


'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
'''

# numbersSum = int(input('Введите сумму натуральных чисел X и Y (и X и Y должны быть не больше 1000): '))
# numbersMult = int(input('Введите произведение этих же чисел: '))
# X = int(((numbersSum) - ((numbersSum)**2 - 4 * numbersMult)**(0.5) )/ 2)
# Y = int(((numbersSum) + ((numbersSum)**2 - 4 * numbersMult)**(0.5) )/ 2)
# if X <= 1000 and Y <= 1000 and X>0 and Y>0:
#     print(f'X = {X}, Y = {Y}')
# else:
#     print('X и Y должны быть не больше 1000 и натуральными числами')
    
# эталонное решение:
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)

'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
'''

# number = int (input('Введите число: '))
# degree = 0
# twoInDegree = 0
# while twoInDegree < number:
#     twoInDegree = 2**degree
#     degree += 1
#     if twoInDegree < number:
#       print(twoInDegree)

# эталонное решение:
# number = int (input('Введите число: '))
# degree = 0
# while 2**degree <= number:
#     print(2**degree)
#     degree += 1    
    