# ЗАДАНИЕ 1

# import re
#
# text="пользователь с клавиатуры вводит текст. необходимо посчитать сумму элементов! результат вывести? 1235"
# result=re.split(r'[!?.\n]',text) #Переводим текст в список
#
# x=len(result) #Вычисляем количество элементов(предложений))в списке
# for i in range(x): #Запускаем цикл по кличеству предложений
#     result1=result[i].strip() #Убираем пробел в начале предложения
#     result2=result1.capitalize() #Заменяем превую букву предложения
#     text = re.sub(result1, result2, text, count=1) #Заменяем в тексте часть с маленькой
#     #буквы без пробела (после .strip()) на часть с большой буквы
#
# print(text)
#
# sentences = 0 # считаем количество цифр
# print("количество цифр: ")
# for char in text:
#     if char.isdigit():
#         sentences+=1
#     else:
#         continue
# print(sentences)
#
# sentences = 0 # считаем количество знаков препинания
# print("количество знаков препинания: ")
# for char in text:
#     if char in ",.:;?!":
#         sentences += 1
# print(sentences)
#
# sentences = 0 # считаем количество восклицательных знаков
# print("количество восклицательных знаков: ")
# for char in text:
#     if char in "!":
#         sentences += 1
# print(sentences)

# ЗАДАНИЕ 2

# list_1=[1,2,3,4,5,2,6,7,2,8,9,2]
# number=2
# sentences = 0
# for char in list_1:
#     if char==number:
#         sentences += 1
#     else:
#         continue
# print('Количество повторений - ',sentences)


# ЗАДАНИЕ 3

list_1=[1,2,3,4,5,2,6,7,2,8,9,2]
print(list_1)
number=2
x = len(list_1)
total=sum(list_1)
print("Сумма элемнтов:  ", total)
print('Среднее арифметическое:   ', total/x)
