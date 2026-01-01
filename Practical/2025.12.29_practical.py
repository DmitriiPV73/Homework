# Задание 1

# class BankAccount:
#     def __init__(self, balance, owner):
#         self.__balance = balance
#         self.__owner = owner
#
#     def withdraw(self, amount):
#         if amount < 0:
#             print("Сумма снятия не может быть отрицательной.")
#         elif amount > self.__balance:
#             print("Недостаточно средств на счете.")
#         else:
#             self.__balance -= amount
#
#     def deposit(self, amount):
#         if amount < 0:
#             print("Пополнение баланса не может быть отрицательным.")
#         else:
#             self.__balance += amount
#
#     def get_owner(self):
#         print(f"Владелец счёта: {self.__owner}")
#
#     def get_balance(self):
#         return self.__balance
#
#
# # Пример использования:
# bank_account_1 = BankAccount(10000, 'Петров Петр Петрович')
# bank_account_1.get_owner()        # Владелец счёта: Петров Петр Петрович
# print(bank_account_1.get_balance())  # 10000
#
# bank_account_1.withdraw(300)
# print(bank_account_1.get_balance())  # 9700
#
# bank_account_1.deposit(-500)      # Пополнение баланса не может быть отрицательным.
# print(bank_account_1.get_balance())  # всё ещё 9700
#
# bank_account_1.deposit(1000)
# print(bank_account_1.get_balance())  # 10700

# Задание 2

class UserProfile:
    def __init__(self, email: str, age: int, username: str):
        # Инициализация через сеттеры (они вызовут валидацию)
        self.email = email
        self.age = age
        self.username = username

    # Геттеры
    @property
    def email(self):
        return self.__email

    @property
    def age(self):
        return self.__age

    @property
    def username(self):
        return self.__username

    # Сеттеры с try-except
    @email.setter
    def email(self, value: str):
        try:
            # Проверяем тип
            if not isinstance(value, str):
                raise TypeError("Email должен быть строкой.")
            # Простая проверка на наличие '@' и '.'
            if "@" not in value or "." not in value:
                raise ValueError("Email должен содержать '@' и '.'.")
            self.__email = value
        except (TypeError, ValueError) as e:
            # Перехватываем и повторно выбрасываем исключение
            raise e  # или просто: raise

    @age.setter
    def age(self, value: int):
        try:
            if not isinstance(value, int):
                raise TypeError("Возраст должен быть целым числом.")
            if value < 13 or value > 120:
                raise ValueError("Возраст должен быть от 13 до 120.")
            self.__age = value
        except (TypeError, ValueError) as e:
            raise e

    @username.setter
    def username(self, value: str):
        try:
            if not isinstance(value, str):
                raise TypeError("Имя пользователя должно быть строкой.")
            if len(value) < 3 or len(value) > 20:
                raise ValueError("Имя пользователя должно содержать от 3 до 20 символов.")
            self.__username = value
        except (TypeError, ValueError) as e:
            raise e

    def __str__(self):
        return (f"\nПользователь: {self.__username}, "
                f"\nEmail: {self.__email}, "
                f"\nВозраст: {self.__age}")

# Верный ввод
user=UserProfile('123@mail.ru', 15, 'Den')
print(user)

# Ввод с ошибкой
user2=UserProfile('123-email.ru', 25, 'Anna')
print(user2)