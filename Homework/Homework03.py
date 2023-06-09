'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
'''

''' C вводом элементов пользователем'''
# array = []
# for i in range(int(input('Введите количество элементов массива (натуральное число): '))):
#     array.append(int(input('Введите значение элемента массива:')))
#     i += 1
# print(array)
# number = int(input('Задайте число, количество которого нужно определить в данном массиве: '))
# count = 0
# for item in array:
#     if item == number:
#         count += 1
# print(f'Данное число встречается в массиве {count} раз')

''' C использованием генератора случайных чисел'''
# from random import randint
# array = []
# for i in range(int(input('Введите количество элементов массива (натуральное число): '))):
#     array.append(randint(0,10))
#     i += 1
# print(array)
# number = int(input('Задайте число, количество которого нужно определить в данном массиве: '))
# count = 0
# for item in array:
#     if item == number:
#         count += 1
# print(f'Данное число встречается в массиве {count} раз')

'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
'''

# from random import randint
# my_list = []
# for i in range(int(input('Введите количество элементов массива (натуральное число): '))):
#     my_list.append(randint(0,100))
# print(my_list)
# number = int(input('Введите число: '))
# difference = abs(my_list[0] - number)
# close_element = my_list[0]
# for i in range(len(my_list)):
#     if abs(my_list[i] - number) < difference:
#         difference = abs(my_list[i] - number)
#         close_element = my_list[i]
# print(f'Наиболее близкий по величине элемент массива к заданному числу: {close_element}')

'''
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12
'''

'''Для русского алфавита'''
# word = input('Введите слово для определения количества набранных очков: ').upper()
# alphabet = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 'К': 2,
#             'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'Й': 4, 'Ы': 4,
#             'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10, }
# result = 0
# if " " in word:
#   print('Необходимо ввести только одно слово!')
# else:
#   for i in range(len(word)):
#       for k,v in alphabet.items():
#         if word[i] == k:
#               result = result + v
#   print('Количество набранных очков: ', result)

'''Для английского алфавита'''
# word = input('Введите слово для определения количества набранных очков: ').upper()
# alphabet = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,            
#             'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5,
#             'J': 8, 'X': 8, 'Q': 10, 'Z': 10, }
# result = 0
# if " " in word:
#   print('Необходимо ввести только одно слово!')
# else:
#   for i in range(len(word)):
#       for k,v in alphabet.items():
#         if word[i] == k:
#               result = result + v
#   print('Your scores: ', result)


'''Сразу для двух алфавитов'''
word = input('Введите слово для определения количества набранных очков: ').upper()
alphabet = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 'К': 2,
            'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'Й': 4, 'Ы': 4,
            'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10, 
            'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,           
            'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5,
            'J': 8, 'X': 8, 'Q': 10, 'Z': 10, }
result = 0
if " " in word:
  print('Необходимо ввести только одно слово!')
else:
  # for i in range(len(word)):
  #     for k,v in alphabet.items():
  #       if word[i] == k:
  #             result = result + v
  # print('Количество набранных очков: ', result)
  for i in word:
     if i in alphabet.keys():
        result += alphabet[i]
  print('Количество набранных очков: ', result)
  
  '''Решение когда ключ очки'''
  # dictonary = {1:'AEIO', 2:'DG'}
  # world = input('Введите слово: ').upper()
  # sum = 0
  # for i in word:
  #    for key,value in dictonary.items():
  #       if i in value:
  #          sum += key
  # print(f'Стоимость слова: {sum}')

