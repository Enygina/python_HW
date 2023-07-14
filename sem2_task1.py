"""
    Напишите программу, которая получает целое число и возвращает
    его шестнадцатеричное строковое представление. Функцию hex
    используйте для проверки своего результата.
"""

hexadec_digits = "0123456789abcdef"


def converter(number):
    hexadec_number = ""

    while number > 0:
        hex_dec_index = number % 16
        hexadec_digit = hexadec_digits[hex_dec_index]
        hexadec_number = hexadec_digit + hexadec_number
        number //= 16

    return hexadec_number


check_num = int(input('Введите число: '))
print("Число в шестнадцатеричной системе счисления:", converter(check_num))
print("Проверка:", hex(check_num)[2:])
