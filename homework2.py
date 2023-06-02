
# Задание №1

a = hex(int(input('Введите целое число: ')))
print(a)


# Задание №2

from fractions import Fraction

a = Fraction (int(input('Введите первый числитель: ')), int(input('Введите первый знаменатель: ')))
b = Fraction(int(input('Введите второй числитель: ')), int(input('Введите второй знаменатель: ')))

print(a + b)