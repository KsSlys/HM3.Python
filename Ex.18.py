'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в
первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны 
N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
    '''

N = int(input('Введите количество элементов: '))
x = int(input("Введите число    "))
from random import randint
list_1 = [randint(0,10) for i in range(N)]
print(list_1)

itog_min = []
for i in range(N):
    if list_1[i] <= x:
        itog_min.append(list_1[i])
print(itog_min)

itog_max = []
for i in range(N):
    if list_1[i] >= x:
        itog_max.append(list_1[i])
print(itog_max)

if (x - max(itog_min)) > (min(itog_max) - x):
    print(min(itog_max))
else:
    print(max(itog_min))
