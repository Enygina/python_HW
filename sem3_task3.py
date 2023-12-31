"""
Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.

"""
import random

a = {"рюкзак": 2, "палатка": 3, "спальный мешок": 2, "одежда": 4, "вода": 5, "аптечка": 2, "фонарик": 0.5, "кателок": 2,
     "спрей от комаров": 0.3}

max_load = 10
count = 0
List_item = []
while count < max_load:
    key, value = random.choice(list(a.items()))
    if key in List_item:
        continue
    if count + value > max_load:
        break
    count += value
    List_item += (str(key), str(value))

print(List_item, "=", count)
