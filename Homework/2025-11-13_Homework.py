# Задание 1

# text=input("Введи текст: ")
#
# text = text.replace(" ","") # Убираем пробелы
# text = text.lower() # Приводим к одному регистру
#
# if text == text[::-1]:  # сравниваем с текстом в обратном порядке. Границы не указываются.
#     print("Палиндром")
# else:
#     print("Не палиндром")



# Задание 2

# list1=input("Введи текст: ")
# list2=input("Введи слова: ")
#
# list1 = list1.split()  # Перевод текста в список
# list2 = list2.split() # Перевод слов в список
#
# len_list1 = len(list1)  # длина списка текста
# len_list2 = len(list2) # длина списка слов
#
# for i in range(len_list2):
#     for j in range(len_list1):
#         if list2[i] == list1[j]:
#             list2[i] = list2[i].upper()  # Переход на верхний регистр
#             list1[j] = list1[j].upper()  # Переход на верхний регистр основного текста
#         else:
#             continue
#
# text = " ".join(list1)  # Преобразуем список в текст с пробелами
#
# print(text)


# Задание 3


text = ("Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.")
sentences = 0
for char in text:
    if char in ".!?":
        sentences += 1
print(sentences)