# Задание 2

class Square:  # Расчет площади квадрата
    def __init__(self, l):
        self.l = int(l)
        print("     Площадь квадрата:  ", self.l ** 2)


class Rectangle:  # Расчет площади прямоугольника
    def __init__(self, l_1, l_2):
        self.l_1 = int(l_1)
        self.l_2 = int(l_2)
        print("     Площадь прямоугольника: ", self.l_1 * self.l_2)


class Rhomb_diagonal:  # Расчет площади ромба через диагонали
    def __init__(self, d_1, d_2):
        self.d_1 = int(d_1)
        self.d_2 = int(d_2)
        print("     Площадь ромба через диагонали: ", (self.d_1 * self.d_2) / 2)


class Rhomb_height:  # Расчет площади ромба через длину стороны и высоту
    def __init__(self, l, h):
        self.l = int(l)
        self.h = int(h)
        print("     Площадь ромба через длину стороны и высоту: ", self.l * self.h)


class Rhomb_corner:  # Расчет площади ромба через длину стороны и угол
    def __init__(self, l, a):
        self.l = int(l)
        import math
        self.a = math.radians(a)
        print("     Площадь ромба через длину стороны и угол: ", (self.l ** 2) * math.sin(self.a))


class Triangle_height:  # Расчет площади ромба через длину стороны и высоту
    def __init__(self, l, h):
        self.l = int(l)
        self.h = int(h)
        print("     Площадь треугольника через длину стороны и высоту: ", self.l * self.h * 0.5)


class Triangle_corner:  # Расчет площади треульника через две стороны и угол между ними
    def __init__(self, a, b, a_b):
        self.a = int(a)
        self.b = int(b)
        import math
        self.a_b = math.radians(a_b)
        print("     Площадь треугольника через две стороны и угол между ними: ",
              (self.a * self.b) * math.sin(self.a_b) * 0.5)

class Triangle_sides:  # Расчет площади треугольника через три стороны
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        p=(a+b+c)/2
        import math
        print("     Площадь треугольника через три стороны: ", math.sqrt(p*(p-a)*(p-b)*(p-c)))


count=0
sq=input ("\nРасчитать площадь квадрата со стороной 5 \"+\" или \"-\"")
if sq=="+":
    square = Square(5)
    count = count + 1

rec=input ("\nРасчитать площадь прямоугольника со стоонами 5 и 6 \"+\" или \"-\" ")
if rec=="+":
    rectangle = Rectangle(5,6)
    count = count + 1

rh_d=input ("\nРасчитать площадь ромба через диагонали 5 и 6 \"+\" или \"-\" ")
if rh_d=="+":
    rhomb_diagonal = Rhomb_diagonal(5, 6)
    count += 1

rh_h=input("\nРасчитать площадь ромба через длину стороны 6 и высоту 5 \"+\" или \"-\" ")
if rh_h=="+":
    rhomb_height = Rhomb_height(6, 5)
    count += 1

rh_c=input("\nРасчитать площадь ромба через длину стороны 5 и угол 45 град. \"+\" или \"-\" ")
if rh_c=="+":
    rhomb_corner = Rhomb_corner(5, 45)
    count += 1

tr_h=input("\nРасчитать площадь треугольника через длину стороны 5 и высоту 6 \"+\" или \"-\" ")
if tr_h=="+":
    triangle_height = Triangle_height(5, 6)
    count += 1

tr_c=input("\nРасчитать площадь треугольника через две стороны 5 и 5  и угол между ними 30 град. \"+\" или \"-\" ")
if tr_c=="+":
    triangle_corner = Triangle_corner(5, 5,30)
    count += 1

tr_s=input("\nРасчитать площадь треугольника через три стороны 2, 5 и 6 \"+\" или \"-\" ")
if tr_s=="+":
    triangle_sides = Triangle_sides(2, 5, 4)
    count += 1

print("\nКоличество расчетов:  ",count)




