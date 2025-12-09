# Задание 1

class Car:
    def __init__(self, model, manufacturer, volume_engine, colour):
        self.__model = model
        self.__manufacturer = manufacturer
        self.__volume_engine = volume_engine
        self.__colour = colour

    def print_car(self):
        print(f"\nМодель {self.__model}, производитель {self.__manufacturer}, "
              f"\nобъем двигателя {self.__volume_engine}, цвет {self.__colour}, ")


class My_car(Car):
    def __init__(self, model, manufacturer, volume_engine, colour, year, price):
        super().__init__(model, manufacturer, volume_engine, colour)
        self.year = year
        self.price = price

    def print_my_car(self):
        print(f"год {self.year}, цена {self.price} $")


car_1 = My_car('Ford', 'Ford Motor Company', 1.4, 'white', 2023, 1500)
car_1.print_car()
car_1.print_my_car()

car_2 = My_car('Volvo', 'Volvo Cars', 2.4, 'black', 2008, 1300)
car_2.print_car()
car_2.print_my_car()

car_3 = My_car('Toyta', 'Toyota Motor Corporation', 1.8, 'blue', 2010, 800)
car_3.print_car()
car_3.print_my_car()

# Задание 2

# class Book:
#     def __init__(self, name, year, manufacturer, genre, author, price):
#         self.name = name
#         self.year = year
#         self.manufacturer = manufacturer
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def  print_book(self):
#         print(f"\n\"{self.name}\", год {self.year}, издательство \"{self.manufacturer}\","
#               f"\nжанр {self.genre}, автор {self.author}, цена {self.price} руб.")
#
#
# book_1 = Book('Как закалялась сталь', 1934, 'Молодая гвардия', 'Повести', 'Н.А. Островсий', 259)
# book_1.print_book()
# book_2 = Book('Война и мир', 1869, 'МИФ', 'Исторический роман', 'Л.Н.Толстой', 437)
# book_2.print_book()
# book_3 = Book('Мишкино детство', 1973, 'Малыш', 'Детская проза', 'М.Н. Алексеев', 437)
# book_3.print_book()

# Задание 3

# class Stadium:
#     def __init__(self, name, date, country, city, volume):
#         self.__name = name
#         self.__date = date
#         self.__country = country
#         self.__city = city
#         self.volume = volume
#
#     def volume_stadium(self, volume):
#         self.volume = volume
#
#     def print_stadium(self):
#         print(f"\nСтадион \"{self.__name}\", дата открытия {self.__date}, страна {self.__country},"
#               f"\nгород {self.__city}, вместимость {self.volume} человек")
#
#
# stadium_1 = Stadium('Лужники', '31 июля 1956', 'СССР', 'Москва', 81000)
# stadium_1.print_stadium()
#
# stadium_2 = Stadium('Камп Ноу', '24 сентября 1957', 'Испания', 'Барселона', 99354)
# stadium_2.print_stadium()
#
# stadium_3 = Stadium('Мичиган Стэдиум', '1927', 'США', 'Мичиган', 81000)
# stadium_3.volume_stadium(107601) #Числеость после рекострукции
# stadium_3.print_stadium()
