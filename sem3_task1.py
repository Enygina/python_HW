# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.
from typing import List, Any

list_with_dubl = [1, 2, 5, 4, 6, 1, 2, 5, 4, 7, 8, 5, 6, 9]
dic = {}
list_only_dubl = []
list_uniqu = list(dict.fromkeys(list_with_dubl))

for item in list_with_dubl:
    value = dic.setdefault(item, 0)
    dic[item] += 1
print(dic)

for key, value in dic.items():
    if value > 1:
        list_only_dubl.append(key)

print(f'Список дублирующихся значений {list_only_dubl}')
print(f'Список без дубликатов {list_uniqu}')
