# Задание 1

class Human:
    def __init__(self, nsp, date, country, city):
        self.__nsp = nsp
        self.__date = date
        self.__country = country
        self.__city = city

    def print_human(self):
        print(f"\nФИО: {self.__nsp}, дата рождения: {self.__date}, "
              f"\nстрана: {self.__country}, город: {self.__city}, ")


class My_human(Human):
    count = 0  # Нулевое значение счетчика

    def __init__(self, nsp, date, country, city, phone, address):
        super().__init__(nsp, date, country, city)
        self.phone = phone
        self.address = address
        type(self).count += 1  # Увеличение счетчика на количество обращений к классу

    def print_my_human(self):
        print(f"номер телефона: {self.phone}, адрес: {self.address} ")
        print(f'Количество объектов: {self.count}')  # Вывод значение счетчика


man_1 = My_human('Петров Петр Петрович', '13.06.1982', 'Россия', 'Пермь', 2637233, 'Краснова 7-125')
man_1.print_human()
man_1.print_my_human()

man_2 = My_human('Васильев Василий Васильевич', '01.05.2000', 'Россия', 'Москва', 89652637233, 'Щепкина 44-2')
man_2.print_human()
man_2.print_my_human()
