#Задание 1

# class Circle:
#     def __init__(self, radius):
#         """Класс окруность"""
#         self.radius = radius
#         self.length = 2*self.radius*3.14
#
#
#     def __eq__(self, other):
#         return self.radius==other.radius
#
#     def __gt__(self, other):
#         return self.length > other.length
#
#     def __ge__(self, other):
#         return self.length >= other.length
#
#     def __lt__(self, other):
#         return self.length < other.length
#
#     def __le__(self, other):
#         return self.length <= other.length
#
#     def __add__(self, other):
#         return print(f'\nПропорциональное именение размеров окружноти 1: R= {self.radius + other} L= {2*(self.radius + other)*3.14}' )
#
#     def __sub__(self, other):
#         return print(f'\nПропорциональное именение размеров окружноти 1: R= {self.radius - other} L= {2*(self.radius - other)*3.14}' )
#
#     def __isub__(self, other):
#         self.radius -= other
#         self.length = 2 * self.radius * 3.14
#         print(f'\nПропорциональное именение размеров окружноти 1: R= {circle_1.radius}, L= {self.length}')
#         return self
#
#     def __iadd__(self, other):
#         self.radius += other
#         self.length = 2 * self.radius * 3.14
#         print(f'\nПропорциональное именение размеров окружноти 1: R= {circle_1.radius}, L= {self.length}')
#         return self
#
#     def print_circle (self):
#         print(f"R= {self.radius} "
#               f"L= {self.length}")
#
#
# circle_1=Circle(15)
# circle_1.print_circle()
#
# circle_2=Circle(15)
# circle_2.print_circle()
#
#
# print(circle_2 == circle_1)
#
# if circle_1>circle_2:
#     print("Окружность 1 > окружности 2")
# elif circle_1<circle_2:
#     print("Окружность 1 < окружности 2")
# elif circle_1==circle_2:
#     print("Окружность 1 = окружности 2")
#
# circle_1 + 4
#
# circle_1 - 4
#
# circle_1 -= 3
#
# circle_1 += 8
#
# Задание 2
#
# class Complex:
#     def __init__(self, re,lm):
#         """Класс комплексные числа"""
#         self.re = re
#         self.lm = lm
#
#     def __add__(self, other):
#         return print(f'\nСумма комплексных чисел: {self.re + other.re} {self.lm + other.lm}i' )
#
#     def __sub__(self, other):
#         return print(f'\nРазность комплексных чисел: {self.re - other.re} {self.lm - other.lm}i' )
#
#     def __mul__(self, other):
#         return print(f'\nПроизведение комплексных чисел: {self.re * other.re - self.lm*other.lm} {self.re*other.lm + other.re*self.lm}i' )
#
#     def __truediv__(self, other):
#         a3 = (self.re * other.re + self.lm * other.lm)/(other.re **2 + other.lm**2)
#         b3 = (other.re*self.lm - self.re*other.lm)/(other.re **2 + other.lm**2)
#         return print(f'\nДеление комплексных чисел: {a3} {b3}i' )
#
#
#     def print_complex (self):
#         print(f"{self.re} {self.lm}i")
#
#
# complex_1=Complex(2,5)
# complex_1.print_complex()
#
# complex_2=Complex(3, -7)
# complex_2.print_complex()
#
# complex_1+complex_2
#
# complex_1-complex_2
#
# complex_1*complex_2
#
# complex_1/complex_2

#Здание 3

# class Airplane:
#     def __init__(self, capacity, range, speed, passenger):
#         """Класс самолет"""
#         self.capacity = capacity
#         self.range = range
#         self.speed = speed
#         self.passenger = passenger
#
#     def __eq__(self, other):
#         return self.capacity == other.capacity and self.range == other.range and self.speed == other.speed
#
#     def __gt__(self, other):
#         return self.capacity > other.capacity
#
#     def __lt__(self, other):
#         return self.capacity < other.capacity
#
#     def print_airplane (self):
#         print(f"Вместимость = {self.capacity}. "
#               f"   Дальность полета= {self.range}."
#               f"   Скорость полета= {self.speed}."
#               f"   Пассажиров на борту= {self.passenger}")
#
#
#     def __add__(self, other):
#         return print(f'\nУвеличение количества пассажиров на борту смолета 1 до: {self.passenger + other}')
#
#     def __sub__(self, other):
#         return print(f'\nУменьшение количества пассажиров на борту смолета 1 до: {self.passenger - other}')
#
#     def __isub__(self, other):
#         self.passenger -= other
#         print(f'\nУменьшение количества пассажиров на борту смолета 1 до: {self.passenger}')
#         return self
#
#     def __iadd__(self, other):
#         self.passenger += other
#         print(f'\nУвеличение количества пассажиров на борту смолета 1 до: {self.passenger}')
#         return self
#
#
# airplane_1=Airplane(100, 4100, 500, 70)
# airplane_1.print_airplane()
#
# airplane_2=Airplane(163, 5100, 870, 80)
# airplane_2.print_airplane()
#
# print("Тип самолета одинаковый - " ,airplane_2 == airplane_1)
#
# if airplane_1 > airplane_2:
#     print("Максимальное количество пасажиров самолета 1 > максимального количества пасажиров самолета 2")
# elif airplane_1 < airplane_2:
#     print("Максимальное количество пасажиров самолета 1 < максимального количества пасажиров самолета 2")
# elif airplane_1 == airplane_2:
#     print("Максимальное количество пасажиров самолета 1 = максимальному количеству пасажиров самолета 2")
#
# airplane_1 + 4
#
# airplane_1 - 6
#
# airplane_1 -= 4
#
# airplane_1 += 8

#Задание 4

class Flat:
    def __init__(self, square, price):
        """Класс квартира"""
        self.square = square
        self.price = price

    def __eq__(self, other):
        return self.square == other.square

    def __ne__(self, other):
        return self.square != other.square

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price


    def print_flat (self):
        print(f"Площадь = {self.square}. "
              f"   Стоимость= {self.price}.")


flat_1=Flat(95, 2800)
flat_1.print_flat()

flat_2=Flat(98, 2500)
flat_2.print_flat()

print("Площади равны:    ", flat_1.square == flat_2.square)
print("Площади не равны: ", flat_1.square != flat_2.square)

print("Стоимоть вариры 1 < стоимости квартиры 2:", flat_1.price<flat_2.price)
print("Стоимоть вариры 1 > стоимости квартиры 2:", flat_1.price>flat_2.price)
print("Стоимоть вариры 1 = стоимости квартиры 2:", flat_1.price==flat_2.price)




