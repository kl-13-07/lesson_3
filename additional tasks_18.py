# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5


vol_size = int(input('Введите колличества элементов в массиве'))

vol_array = list(range(1, vol_size + 1))

print(vol_array)
vol_number = int(input('введите число к которому самый близкий по величине элементcj,rjcj  '))
vol_index = 0
vol_min = vol_number - vol_array[0]
n = len(vol_array)
for i in range(1, n):
    count = abs(vol_number - vol_array[i])
    if count < vol_min:
        vol_min = count
        vol_index = i
print(vol_array[vol_index])
