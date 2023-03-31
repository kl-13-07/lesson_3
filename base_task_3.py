# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#
# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456


vol_name = input('Введите имя: ')
vol_surname = input('Введите фамилию : ')
vol_year_burn = input('Введите год рождения: ')
vol_city = input('Введите город проживания : ')
vol_email = input('Введите e-mail: ')
vol_phone = input('Введите телефонный номер: ')


def func_input_data(arg1, arg2, arg3, arg4, arg5, arg6):
    result = (f'{arg1} {arg3} {arg5} года рождения, проживает в городе {arg2}, email: {arg4}, телефон:{arg6}')
    print(result)

func_input_data(arg1=vol_name, arg2=vol_city, arg3=vol_surname, arg4=vol_email, arg5=vol_year_burn, arg6=vol_phone)
