# Задание 3

class Maxi:  # Максимум из четырех элеметов
    def __init__(self, a, b, c, d):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
        list = [self.a, self.b, self.c, self.d]
        maxi = max(list)
        print("     Максимальное значение:  ", maxi )


class Mini:  # Минимум из четырех элеметов
    def __init__(self, a, b, c, d):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
        list = [self.a, self.b, self.c, self.d]
        mini = min(list)
        print("     Минимальое зачение: ", mini )


class Arithmetic:  # Среднее арифмеическое из четырех элементов
    def __init__(self, a, b, c, d):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
        print("     Среднее арифмеическое: ", (a+b+c+d)/4 )


class Factorial:  # Факториал из четырех элементов
    def __init__(self, a, b, c, d):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
        print("     Факториал: ", a*b*c*d )


count=0
ma=input ("\nНайти максимальное значение \"+\" или \"-\" ")
if ma=="+":
    maxi = Maxi(5, 6, 7, 8)
    count += 1

mi=input ("\nНайти минмльное значение \"+\" или \"-\" ")
if mi=="+":
    mini = Mini(5, 6, 7, 8)
    count += 1

ar=input ("\nНайти среднее арифмеическое \"+\" или \"-\" ")
if ar=="+":
    arithmetic = Arithmetic(5, 6, 7, 8)
    count += 1

fa=input("\nНайти факториал \"+\" или \"-\" ")
if fa=="+":
    factorial = Factorial(5, 6, 7, 8)
    count += 1

print("\nКоличество расчетов:  ",count)