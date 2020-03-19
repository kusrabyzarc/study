from math import log as ln
pn = 0

while True:
    try:
        p = int(input('Введите верхнюю границу: '))
    except:
        continue
    break

for i in range(2, p + 1):
    rt = i ** 0.5
    ao = True
    for j in range(2, int(round(rt) + 1)):
        if i % j == 0:
            ao = False
            break
    if ao:
        pn += 1

th = p / ln(p)

print('Найдено ' + str(pn) + ' простых чисел.')
print('Теоретическое значение: ' + str(round(th)) + ' чисел.')
print('Погрешность теоретического значения: ~' + str(round(100 - ((p - th) / p) * 100)) + '%.')
print('Средняя частота: ' + str(p / pn) + '.')
