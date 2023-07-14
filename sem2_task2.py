"""Напишите программу, которая принимает две строки вида “a/b” - дробь 
с числителем и знаменателем. Программа должна возвращать сумму и 
произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

import fractions

fst_fract = input("Введите 1-ю дробь через '/': ")
sec_fract = input("Введите 2-ю дробь через '/': ")


def fract_sum(fst_fract: str, sec_fract: str) -> str:
    # получение числителей и знаменателей из дробей
    fst_fract_part = split_fraction(fst_fract)
    sec_fract_part = split_fraction(sec_fract)
    # ищем НОК, приводим к общему знаменателю
    fract_lcm = my_lcm(fst_fract_part[1], sec_fract_part[1])
    # добавочные множители для приведения к единому знаменателю
    mult_1 = int(fract_lcm / fst_fract_part[1])
    mult_2 = int(fract_lcm / sec_fract_part[1])
    fst_fract_part = [i * mult_1 for i in fst_fract_part]
    sec_fract_part = [i * mult_2 for i in sec_fract_part]
    # сложение дроби
    fst_fract_part[0] += sec_fract_part[0]

    return str(fst_fract_part[0]) + "/" + str(fst_fract_part[1])


def split_fraction(fract: str) -> list:
    fraction_parts = fract.split("/")
    fraction_parts = [int(s) for s in fraction_parts]
    return fraction_parts


# произведение дробей
def fract_milt(fst_fract: str, sec_fract: str) -> str:
    # получение числителей и знаменателей из дробей
    fst_fract_part = split_fraction(fst_fract)
    sec_fract_part = split_fraction(sec_fract)
    # умножение дробей
    fst_fract_part[0] *= sec_fract_part[0]
    fst_fract_part[1] *= sec_fract_part[1]

    return str(fst_fract_part[0]) + "/" + str(fst_fract_part[1])


# НОД
def my_gcd(num_1: int, num_2: int) -> int:
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    while num_2:
        num_1 %= num_2
        num_1, num_2 = num_2, num_1

    return int(num_1)


# Поиск НОК
def my_lcm(num_1: int, num_2: int) -> int:
    return int(num_1 / my_gcd(num_1, num_2) * num_2)


print("Мои методы:")
print(f"{fst_fract} + {sec_fract} = {fract_sum(fst_fract, sec_fract)}")
print(f"{fst_fract} * {sec_fract} = {fract_milt(fst_fract, sec_fract)}")

print("Проверочные методы:")
print(f"{fst_fract} + {sec_fract} = {fractions.Fraction(fst_fract) + fractions.Fraction(sec_fract)}")
print(f"{fst_fract} * {sec_fract} = {fractions.Fraction(fst_fract) * fractions.Fraction(sec_fract)}")
