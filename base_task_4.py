# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()


first_num = input('Введите первое число: ')
second_num = input('Введите второе число : ')
third_num = input('Введите третье число: ')
def func_sort_sum(arg1, arg2, arg3):
    ad_to_list = [arg1, arg2, arg3]
    for j in range(len(ad_to_list)):
        for i in range(len(ad_to_list) - 1):
            if ad_to_list[i + 1] > ad_to_list[i]:
                ad_to_list[i + 1], ad_to_list[i] = ad_to_list[i], ad_to_list[i + 1]
    print(ad_to_list)
    print(int(ad_to_list[0]) + int(ad_to_list[1]))
func_sort_sum(first_num, second_num, third_num)
