'''
Треугольник существует только тогда, когда сумма любых двух его сторон
больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует. Отдельно сообщить
является ли треугольник разносторонним, равнобедренным или равносторонним.
'''
a = float(input('Введите стоорону a: '))
b = float(input('Введите стоорону b: '))
c = float(input('Введите стоорону c: '))

if a < b + c and b < a + c and c < b + a:
    if a == b == c:
        print('Треугольник равносторонним')
    elif a == b or b == c or c == a:
        print('Треугольник равнобедренным')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольника с такими сторонами не существует')