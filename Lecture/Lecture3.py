# def summ_numbers (n):
#     summ = 0
#     for i in range(1, n+1):
#         summ += i
#     print(summ)

# summ_numbers(5)

# def sum_numbers (n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# print(sum_numbers(5))

# def summ_numbers2 (n, y ='Hello'):
#     print(y)
#     summ = 0
#     for i in range(1, n+1):
#         summ += i
#     return summ
# print(summ_numbers2(5, 'lkj'))

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'f', 'f'))

# def sum_str(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res

# print(sum_str(1, 2, 3))

# import module
# print(module.maxi(5,9))

# import module as m1
# print(m1.maxi(5,6))

# from module import maxi
# print(maxi(10,9))

# from module import *
# print(maxi(15,9))

'''Последовательность Фибоначчи циклом'''

# def fibonachi (n):
#     fib1 = 0
#     fib2 = 1
#     print (fib1, fib2, end=" ")
#     i = 0
#     while i < n:
#       fibi = fib1+fib2
#       fib1 = fib2
#       fib2 = fibi
#       i += 1
#       print (fibi, end=" ")
      

# fibonachi(10)


# '''Последовательность Фибоначчи рекурсией'''
# def fib(n):
#    if n in [1,2]:
#       return 1
#    return fib(n-1) + fib (n-2)

# list_1 = []
# for i in range(1,10):
#    list_1.append(fib(i))
# print(list_1)


def quick_sort(array):
    if len(array) <= 1:
        return(array)
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14,5,9,6,3,58,7,5,2,7]))

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len (left) and j < len (right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len (right):
            nums[k] = right[j]
            j += 1
            k += 1


list_1 = [14,5,9,6,3,58,7,5,2,7]
merge_sort(list_1)
print(list_1)