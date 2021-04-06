#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ind_2 import Fraction

# Варивнт 12 Создать класс Fraction для работы с дробными числами. Число должно быть представлено
# двумя целочисленными полями: целая часть и дробная часть. Реализовать арифметические
# операции сложения, вычитания, умножения и операции сравнения.

# Выполнить индивидуальное задание 1 лабораторной работы 12, максимально задействовав
# имеющиеся в Python средства перегрузки операторов.


if __name__ == '__main__':
    r1 = Fraction(whole=5, fractional=6)
    print(f"r1={r1}")
    r2 = Fraction(whole=3, fractional=4)
    print(f"r2={r2}")

    print(f"r1 < r2: {r1 < r2}")
    print(f"r1 > r2: {r1 > r2}")
    print(f"r1 == r2: {r1 == r2}")
    print(f"r1 >= r2: {r1 >= r2}")
    print(f"r1 <= r2: {r1 <= r2}")

    print(f"Subtraction: {r1 - r2}")
    print(f"Addition: {r1 + r2}")
    print(f"Multiplication: {r1 * r2}")
