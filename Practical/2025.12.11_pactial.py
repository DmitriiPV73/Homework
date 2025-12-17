# Задание 1

# class Human:
#     def __init__(self, nsp, date, country, city):
#         self.__nsp = nsp
#         self.__date = date
#         self.__country = country
#         self.__city = city
#
#     def print_human(self):
#         print(f"\nФИО: {self.__nsp}, дата рождения: {self.__date}, "
#               f"\nстрана: {self.__country}, город: {self.__city}, ")
#
#
# class My_human(Human):
#     def __init__(self, nsp, date, country, city, phone, address):
#         super().__init__(nsp, date, country, city)
#         self.phone = phone
#         self.address = address
#
#     def print_my_human(self):
#         print(f"номер телефона: {self.phone}, адрес: {self.address} ")
#
#
# man_1 = My_human('Петров Петр Петрович', '13.06.1982', 'Россия', 'Пермь', 2637233, 'Краснова 7-125')
# man_1.print_human()
# man_1.print_my_human()
#
# man_2 = My_human('Васильев Василий Васильевич', '01.05.2000', 'Россия', 'Москва', 89652637233, 'Щепкина 44-2')
# man_2.print_human()
# man_2.print_my_human()

# Задание 2

# class City:
#     def __init__(self, name, region, country, residents, index, phone_code):
#         self.name = name
#         self.region = region
#         self.country = country
#         self.index = index
#         self.residents = residents
#         self.phone_code = phone_code
#
#     def  print_city(self):
#         print(f"\n\"{self.name}\", регион: {self.region}, страна: \"{self.country}\","
#               f"\nколичество жителей: {self.residents} человек, почтовый индекс: {self.index}, телефонный код: {self.phone_code} ")
#
#
# city_1 = City('Пермь', 'Пермкий край', 'Россия', '1 592 493 ', 614, '+7 342')
# city_1.print_city()
#
# city_2 = City('Екатеринбург', 'Свердловская область', 'Россия', '1 332 866 ', 620, '+7 343')
# city_2.print_city()


# Задание 3

# class Country:
#     def __init__(self, name, continent, size, phone_code, capital, city):
#         self.__name = name
#         self.__continent = continent
#         self.__size = size
#         self.__phone_code = phone_code
#         self.__capital = capital
#         self.city = city
#
#     def city_country(self, city):
#         self.city = city
#
#     def print_country(self):
#         print(f"\nСтрана: \"{self.__name}\", континент: {self.__continent}, численность населения: {self.__size},"
#               f"\nтелефонный код страны: {self.__phone_code}, столица: {self.__capital} ")
#
#     def print_city(self):
#         print(f"Города страны: {self.city}")
#
#
# country_1 = Country('Куба', 'Латинская Америка', '11 061 886', '+53', 'Гавана', 'Баямо')
# country_1.print_country()
#
# country_2.city_country('Камагуэй, Ольгин, Сьенфуэгос, Баямо')
# country_2.print_city()

# Задание 4

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


""" Сложение двух обыкновенных дробей """
class   Summ_fraction (Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
        numerator_fraction= numerator * denominator_1 + numerator_1 * denominator
        denominator_fraction=denominator * denominator_1

        for i in range(8):
            x=int(denominator_fraction%(i+1))
            y=int(numerator_fraction%(i+1))
            if x==0 and y==0:
                numerator_fraction=int(numerator_fraction/(i+1))
                denominator_fraction=int(denominator_fraction/(i+1))
            else:
                continue

        if denominator_fraction < numerator_fraction:
            volume=int(numerator_fraction//denominator_fraction)
            numerator_fraction=int(numerator_fraction%denominator_fraction)
            print(f'{numerator}/{denominator}+{numerator_1}/{denominator_1}={volume} {numerator_fraction}/{denominator_fraction}')
        else:
            print(f'{numerator}/{denominator}+{numerator_1}/{denominator_1}={numerator_fraction}/{denominator_fraction}')

""" Разность двух обыкновенных дробей """
class   Difference_fraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
        numerator_fraction = numerator * denominator_1 - numerator_1 * denominator
        denominator_fraction = denominator * denominator_1

        for i in range(8):
            x=int(denominator_fraction%(i+1))
            y=int(numerator_fraction%(i+1))
            if x==0 and y==0:
                numerator_fraction=int(numerator_fraction/(i+1))
                denominator_fraction=int(denominator_fraction/(i+1))
            else:
                continue

        if denominator_fraction < numerator_fraction:
            volume=int(numerator_fraction//denominator_fraction)
            numerator_fraction=int(numerator_fraction%denominator_fraction)
            print(f'{numerator}/{denominator}-{numerator_1}/{denominator_1}={volume} {numerator_fraction}/{denominator_fraction}')
        else:
            print(f'{numerator}/{denominator}-{numerator_1}/{denominator_1}={numerator_fraction}/{denominator_fraction}')

""" Умножение двух обыкновенных дробей """
class   Multiplication_fraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
        numerator_fraction=numerator * numerator_1
        denominator_fraction=denominator*denominator_1

        for i in range(8):
            x=int(denominator_fraction%(i+1))
            y=int(numerator_fraction%(i+1))
            if x==0 and y==0:
                numerator_fraction=int(numerator_fraction/(i+1))
                denominator_fraction=int(denominator_fraction/(i+1))
            else:
                continue

        if denominator_fraction < numerator_fraction:
            volume=int(numerator_fraction//denominator_fraction)
            numerator_fraction=int(numerator_fraction%denominator_fraction)
            print(f'{numerator}/{denominator}*{numerator_1}/{denominator_1}={volume} {numerator_fraction}/{denominator_fraction}')
        else:
            print(f'{numerator}/{denominator}*{numerator_1}/{denominator_1}={numerator_fraction}/{denominator_fraction}')

""" Деление двух обыкновенных дробей """
class   Division_fraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
        numerator_fraction=numerator * denominator_1
        denominator_fraction=denominator * numerator_1

        for i in range(8):
            x=int(denominator_fraction%(i+1))
            y=int(numerator_fraction%(i+1))
            if x==0 and y==0:
                numerator_fraction=int(numerator_fraction/(i+1))
                denominator_fraction=int(denominator_fraction/(i+1))
            else:
                continue

        if denominator_fraction < numerator_fraction:
            volume=int(numerator_fraction//denominator_fraction)
            numerator_fraction=int(numerator_fraction%denominator_fraction)
            print(f'{numerator}/{denominator} / {numerator_1}/{denominator_1}={volume} {numerator_fraction}/{denominator_fraction}')
        else:
            print(f'{numerator}/{denominator} / {numerator_1}/{denominator_1}={numerator_fraction}/{denominator_fraction}')



numerate=1
denominator=4
numerator_1 = int(input("Введи числитель второй дроби: "))
denominator_1 = int(input("Введи знаменатель второй дроби: "))
summa_fr=Summ_fraction(numerate,denominator)
difference_fr=Difference_fraction(numerate,denominator)
multiplication_fr=Multiplication_fraction(numerate,denominator)
division_fr=Division_fraction(numerate,denominator)



