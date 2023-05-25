# Списки
# list_1 = []
# list_1 = list()
# list_1 = [1,6,8]
# print(list_1)
# print(*list_1)

# for i in list_1:
#     print(i)

# print(len(list_1))

# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# list_1.pop()
# print(list_1)

# list_1.pop(3)
# print(list_1)

# list_1.insert(2,85)
# print(list_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# кортежи

# t = ()

# print(type(t))

# t = (1, )
# print(type(t))

# v=[1,2,5]
# print(v)
# print(type(v))

# v=tuple(v)
# print(v)
# print(type(v))

# a,b,c = v
# print(a,b,c)

# t = (1,2,3,4,)
# print(t[2])

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])


# словари

# d = {}
# print(type(d))

# d['q']='qwerty'
# d['w']='werty'
# print(d['q'])
# print(d['w'])


# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐

# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#   print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →


# множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# a = {1,6,8}
# b = frozenset(a)
# print(b)


# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100 простым способом
list_1 = []
for i in range(1, 101):
  list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так: с помощью генератора списка
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# 2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),..., (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
