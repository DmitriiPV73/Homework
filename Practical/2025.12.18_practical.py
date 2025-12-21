# Задание 1

# class Human:
#     def __init__(self, nsp, date):
#         self.__nsp = nsp
#         self.__date = date
#
#     def print_human(self):
#         print(f"\nФИО: {self.__nsp}, дата рождения: {self.__date}, ")
#
#
# class Builder(Human):
#
#     def __init__(self, nsp, date, profession, object, firm):
#         super().__init__(nsp, date)
#         self.profession = profession
#         self.object = object
#         self.firm = firm
#
#     def print_builder(self):
#         print(f"профессия: {self.profession}, объект: {self.object}, организация: {self.firm} ")
#
# class Sailor(Human):
#
#     def __init__(self, nsp, date, profession, ship, company):
#         super().__init__(nsp, date)
#         self.profession = profession
#         self.ship = ship
#         self.company = company
#
#     def print_sailor(self):
#         print(f"профессия: {self.profession}, судно: {self.ship}, компания: {self.company} ")
#
# class Pilot(Human):
#
#     def __init__(self, nsp, date, profession, plane, company):
#         super().__init__(nsp, date)
#         self.profession = profession
#         self.plane = plane
#         self.company = company
#
#     def print_pilot(self):
#         print(f"профессия: {self.profession}, самолет: {self.plane}, компания: {self.company} ")
#
# man_1 = Builder('Петров Петр Петрович', '13.06.1982', 'каменьщик', 'Солнечный город', 'ПЗСП')
# man_1.print_human()
# man_1.print_builder()
#
# man_2 = Sailor('Васильев Василий Васильевич', '01.05.2000', 'боцман', 'Русь великая',  'Камское речное пароходство')
# man_2.print_human()
# man_2.print_sailor()
#
# man_3 = Pilot('Иванов Иван Иванович', '15.06.1990', 'штурман', 'Airbus A320',  'Аэрофлот')
# man_3.print_human()
# man_3.print_pilot()

# Задание 2

# from datetime import date
#
# class Passport():
#     def __init__(self, series, number, nsp, birth_date, birth_place, issue_authority, issue_date):
#         self.series = series
#         self.number = number
#         self.nsp = nsp
#         self.birth_date = birth_date
#         self.birth_place = birth_place
#         self.issue_authority = issue_authority
#         self.issue_date = issue_date
#
#
#     def basic_info(self):
#         return (f"Паспорт: {self.series} {self.number}\n"
#                 f"ФИО: {self.nsp}\n"
#                 f"Дата рождения: {self.birth_date}\n"
#                 f"Место рождения: {self.birth_place}\n"
#                 f"Выдан: {self.issue_authority}\n"
#                 f"Дата выдачи: {self.issue_date}"
#                 )
#
# class ForeignPassport(Passport):
#     def __init__(self, series, number, nsp, birth_date, birth_place, issue_authority, issue_date, foreign_passport_number,
#                  foreign_passport_issue_date):
#         super().__init__(series, number, nsp, birth_date, birth_place, issue_authority, issue_date)
#         self.foreign_passport_number = foreign_passport_number
#         self.foreign_passport_issue_date = foreign_passport_issue_date
#         self.visas = []  # Список для хранения информации о визах
#
#     def visa_info(self, country, expiry_date_visa, visa_type):
#         self.visas.append({
#             "country": country,
#             "expiry_date": expiry_date_visa,
#             "type": visa_type
#         })
#
#     def foreign_passport_info(self):
#         print ("\n--- Заграничный паспорт ---")
#         print (f"ФИО: {self.nsp}")
#         print (f"Дата рождения: {self.birth_date}")
#         print (f"Номер заграничного паспорта: {self.foreign_passport_number}")
#         print (f"Дата выдачи: {self.foreign_passport_issue_date}")
#
#         if self.visas:
#             print("\n--- Визы ---")
#             for visa in self.visas:
#                 print(f"  Страна: {visa['country']}, Срок действия: {visa['expiry_date']}, Тип: {visa['type']}")
#         else:
#             print("\nВизы отсутствуют.")
#
#
#
# passport_1 = Passport(
#     series='4506',
#     number='123456',
#     nsp='Петров Петр Петрович',
#     birth_date=date(1982,6,13),
#     birth_place='Москва',
#     issue_authority='УФМС России',
#     issue_date=date(2022,12,12)
# )
# print(passport_1.basic_info())
#
# foreign_passport = ForeignPassport(
#     series='4506',
#     number='123456',
#     nsp='Петров Петр Петрович',
#     birth_date=date(1982, 6, 13),
#     birth_place='Москва',
#     issue_authority='УФМС России',
#     issue_date=date(2022, 12, 12),
#     foreign_passport_number='456987',
#     foreign_passport_issue_date=date(2024,10,12)
#     )
#
# foreign_passport.visa_info("Германия", "2025-12-31", "Шенген")
# foreign_passport.visa_info("США", "2026-06-01", "Туристическая")
#
#
# print(foreign_passport.foreign_passport_info())

# Задание 3

class Animal:
    def __init__(self, name, age):
        """Класс Животные"""
        self.name = name          # Имя(Кличка) животного
        self.age = age            # Возраст животного

    def __str__(self):
        """Отображение информации о животном"""
        return f" Имя: {self.name}, Возраст: {self.age} лет"


class Tiger(Animal):
    """Метод, который возвращает инфрмацию о тигре"""
    def __init__(self, name, age, klass, detachment):
        super().__init__(name, age)
        self.klass=klass
        self.detachment=detachment

    def tiger_info (self):
        return ("Тигр\n"
                f"Имя/кличка: {self.name}\n"
                f"Возраст: {self.age}\n"
                f"Класс: {self.klass}\n"
                f"Отряд: {self.detachment}\n")

class Crocodile(Animal):
    """Метод, который возвращает инфрмацию о крокодиле"""
    def __init__(self, name, age, klass, detachment):
        super().__init__(name, age)
        self.klass=klass
        self.detachment=detachment

    def crocodile_info(self):
        return ("Крокодил\n"
               f"Имя/кличка: {self.name}\n"
               f"Возраст: {self.age}\n"
               f"Класс: {self.klass}\n"
               f"Отряд: {self.detachment}\n"
               )

class Kangaroo(Animal):
    """Метод, который возвращает инфрмацию о кенгуру"""
    def __init__(self, name, age, klass, detachment):
        super().__init__(name, age)
        self.klass=klass
        self.detachment=detachment

    def kangaroo_info(self):
        return ("Кенгуру\n"
               f"Имя/кличка: {self.name}\n"
               f"Возраст: {self.age}\n"
               f"Класс: {self.klass}\n"
               f"Отряд: {self.detachment}\n"
               )


tiger = Tiger("Тигр Тоша", 5, 'Mлекопитающие', 'Хищные')
print(tiger.tiger_info())
crocodile = Crocodile("Гена", 10, "Пресмыкающиеся", "Крокодилы")
print(crocodile.crocodile_info())
kangaroo = Kangaroo("Боб", 3, 'Mлекопитающие', 'Сумчатые')
print(kangaroo.kangaroo_info())
