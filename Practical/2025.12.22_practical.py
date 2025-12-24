#Задание 1

# import math
#
# class SquareSide:
#     def __init__(self):
#         self.side = ""
#     def square_side(self, side):
#         self.side = side
#         print(f"Радиус вписанной окружности при стороне квадрата {self.side}:", int(self.side)/2)
#
# class SquarePerimeter:
#     def __init__(self, perimeter):
#         self.perimeter = ""
#     def square_perimeter(self, perimeter):
#         self.perimeter = perimeter
#         print(f"Радиус вписанной окружности при периметре квадрата {self.perimeter}:", int(self.perimeter) / 8)
#
# class SquareDiagonal:
#     def __init__(self, diagonal):
#         self.diagonal = ""
#     def square_diagonal(self, diagonal):
#         self.diagonal = diagonal
#         print(f"Радиус вписанной окружности при диагонали квадрата {self.diagonal}:", int(self.diagonal)/2/(math.sqrt(2)))
#
# class CircleInSquare(SquareSide,SquarePerimeter, SquareDiagonal):
#     def __init__(self):
#         super().__init__()
#
# circl=CircleInSquare()
# circl.square_side(side=3)
# circl.square_perimeter(perimeter=16)
# circl.square_diagonal(diagonal=4)


#Задание 2

# class Wheel:
#     def __init__(self):
#         self.radius = ""
#         self.height =""
#         self.width = ""
#
#     def set_wheels_info(self, radius, height, width):
#         self.radius = radius
#         self.height = height
#         self.width = width
#
# class Engine:
#     def __init__(self):
#         self.power = ""
#         self.volume = ""
#
#     def set_engine_info(self,power, volume):
#         self.power = power
#         self.volume = volume
#
# class Doors:
#     def __init__(self):
#         self.quantity = ""
#     def set_doors_info(self, quantity):
#         self.quantity = quantity
#
# class Car (Wheel, Engine, Doors):
#     def __init__(self,name, car_tipe ,engine_tipe):
#         super ().__init__()
#         self.name = name
#         self.car_tipe = car_tipe #седан, купе, внедорожник
#         self.engine_tipe = engine_tipe #бензин, дизель
#
#     def car_info (self):
#         return (
#             f"name: {self.name}\n"
#             f"car_tipe: {self.car_tipe}\n"
#             f"engine_tipe: {self.engine_tipe}\n"
#             f"Колеса radius/height/width: {self.radius}/{self.height}/{self.width}\n"
#             f"Двигатель power/volume: {self.power}/{self.volume}\n"
#             f"Количество дверей: {self.quantity}\n"
#
#         )
#
# kalina=Car('калина','седан','бензин')
# kalina.set_wheels_info(radius=15, height=60, width=195)
# kalina.set_engine_info(power=1500, volume=98)
# kalina.set_doors_info(quantity=4)
# print(kalina.car_info())

#Задание 3

# class Pets:
#     def __init__(self, my_pets, age):
#         self.my_pets = my_pets
#         self.age = age
#     def print_pets(self):
#         print(f'\nМой питомец: {self.my_pets}')
#         print(f'Возраст: {self.age} ')
#
#
#
# class Dog(Pets):
#     def __init__(self, my_pets, age, name, sound, tipe):
#         super().__init__(my_pets, age)
#         self.name = name
#         self.sound = sound
#         self.tipe = tipe
#
#     def dog_sound(self):
#         return (f'sound : {self.sound}')
#     def dog_tipe(self):
#         return (f'tipe : {self.tipe}')
#     def dog_name(self):
#         return (f'name : {self.name}')
#
# class Cat(Pets):
#     def __init__(self, my_pets, age, name, sound, tipe):
#         super().__init__(my_pets, age)
#         self.name = name
#         self.sound = sound
#         self.tipe = tipe
#
#     def cat_sound(self):
#         return (f'sound : {self.sound}')
#
#     def cat_tipe(self):
#         return (f'tipe : {self.tipe}')
#
#     def cat_name(self):
#         return (f'name : {self.name}')
#
# class Parrot(Pets):
#     def __init__(self, my_pets, age, name, sound, tipe):
#         super().__init__(my_pets, age)
#         self.name = name
#         self.sound = sound
#         self.tipe = tipe
#
#     def parrot_sound(self):
#         return (f'sound : {self.sound}')
#
#     def parrot_tipe(self):
#         return (f'tipe : {self.tipe}')
#
#     def parrot_name(self):
#         return (f'name : {self.name}')
#
# class Hamster(Pets):
#     def __init__(self, my_pets, age, name, sound, tipe):
#         super().__init__(my_pets, age)
#         self.name = name
#         self.sound = sound
#         self.tipe = tipe
#
#     def hamster_sound(self):
#         return (f'sound : {self.sound}')
#
#     def hamster_tipe(self):
#         return (f'tipe : {self.tipe}')
#
#     def hamster_name(self):
#         return (f'name : {self.name}')
#
# dog=Dog(my_pets='Собака',name='Шарик',age=4,sound='Гав',tipe='Сторожевая')
# dog.print_pets()
# print(dog.dog_name())
# print(dog.dog_sound())
# print(dog.dog_tipe())
#
# cat=Cat(my_pets='Кот',name='Матроскин',age=2,sound='Мяу',tipe='Сибирский')
# cat.print_pets()
# print(cat.cat_name())
# print(cat.cat_sound())
# print(cat.cat_tipe())
#
# parrot=Parrot(my_pets='Попугай',name='Кеша',age=15,sound='Говоит на 3 языках',tipe='Жако')
# parrot.print_pets()
# print(parrot.parrot_name())
# print(parrot.parrot_sound())
# print(parrot.parrot_tipe())
#
# hamster=Hamster(my_pets='Хомяк',name='Борька',age=1,sound='Пи-пи',tipe='Ангорский')
# hamster.print_pets()
# print(hamster.hamster_name())
# print(hamster.hamster_sound())
# print(hamster.hamster_tipe())

#Задание 4

# class Employer:
#     def __init__(self, level):
#         self.level = level
#
#     def print_employer(self):
#         print('\nThis is Employer class.')
#         print (self.level)
#
#
# class President(Employer):
#     def __init__(self, level, age, name, service_life):
#         super().__init__(level)
#         self.name = name
#         self.age = age
#         self.service_life = service_life
#
#     def print_president(self):
#         return (f'Директор: {self.name}'
#                 f'\nВозраст: {self.age}'
#                 f'\nСрок работы в компании: {self.service_life}')
#
# class Manager(Employer):
#     def __init__(self, level, age, name, service_life):
#         super().__init__(level)
#         self.name = name
#         self.age = age
#         self.service_life = service_life
#
#     def print_manager(self):
#         return (f'Менеджер: {self.name}'
#                 f'\nВозраст: {self.age}'
#                 f'\nСрок работы в компании: {self.service_life}')
#
# class Worker(Employer):
#     def __init__(self, level, age, name, service_life):
#         super().__init__(level)
#         self.name = name
#         self.age = age
#         self.service_life = service_life
#
#     def print_worker(self):
#         return (f'Работник: {self.name}'
#                 f'\nВозраст: {self.age}'
#                 f'\nСрок работы в компании: {self.service_life}')
#
#
# president=President(level='Руководство',name='Иванов И.И.',age=48,service_life=6)
# president.print_employer()
# print(president.print_president())
#
# manager=Manager(level='Управение',name='Петров П.П.',age=30,service_life=4)
# manager.print_employer()
# print(manager.print_manager())
#
# worker=Worker(level='Рабокники',name='Сидоров С.С.',age=28,service_life=1)
# worker.print_employer()
# print(worker.print_worker())

#Задание 5

class Employer:
    def __init__(self, level):
        self.level = level

    def print_employer(self):
        print('\nThis is Employer class.')
        print (self.level)


class President(Employer):
    def __init__(self, level, age, name, service_life):
        super().__init__(level)
        self.name = name
        self.age = age
        self.service_life = service_life


    def __str__(self):
        return (f'Директор: {self.name}'
                f'\nСрок работы в компании: {self.service_life}')

    def __int__(self):
        return self.age

class Manager(Employer):
    def __init__(self, level, age, name, service_life):
        super().__init__(level)
        self.name = name
        self.age = age
        self.service_life = service_life

    def __str__(self):
        return (f'Менеджер: {self.name}'
                f'\nСрок работы в компании: {self.service_life}')

    def __int__(self):
        return self.age

class Worker(Employer):
    def __init__(self, level, age, name, service_life):
        super().__init__(level)
        self.name = name
        self.age = age
        self.service_life = service_life

    def __str__(self):
        return (f'Работник: {self.name}'
                f'\nСрок работы в компании: {self.service_life}')

    def __int__(self):
        return self.age


president=President(level='Руководство',name='Иванов И.И.',age=48,service_life=6)
president.print_employer()
print(president)
print("Возраст",president.__int__())


manager=Manager(level='Управение',name='Петров П.П.',age=30,service_life=4)
manager.print_employer()
print(manager)
print("Возраст",manager.__int__())

worker=Worker(level='Рабокники',name='Сидоров С.С.',age=28,service_life=1)
worker.print_employer()
print(worker)
print("Возраст",worker.__int__())