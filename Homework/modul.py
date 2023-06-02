def fib_number(number: int) ->int:
    '''Вывод числа number последовательности Фибоначчи'''
    if number == 0 or number == 1:
        return number
    return (fib_number(number-1) + fib_number(number-2))


def reverse_range(num: int) -> int:
    '''вывод последовательности натуральных чисел от 0 до num в обратном порядке'''
    print(num, end=' ')
    if num > 0:
        reverse_range(num-1)


def prime_number(n: int) -> bool:
  '''Проверка на простое число'''
  if n > 2 and n %2 != 0:
      for i in range (3, n//2):
          if n %i == 0:
              return False
      return True
  return False 


def degree_number(number_1: int, number_2: int) -> int:
    ''' Возведение числа number_1 в степень  number_2 с помощью рекурсии'''
    if number_2 == 0:
        return 1
    return number_1 * degree_number(number_1, number_2-1)


def summa_recursion(a: int, b: int) -> int:
    '''Нахождение суммы целых чисел путем рекурсии'''
    if b == 0:
        return a
    return 1+summa_recursion(a, b-1)
