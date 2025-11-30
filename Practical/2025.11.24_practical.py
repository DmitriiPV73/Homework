# ЗАДАНИЕ 1

list = [-2, 5, 15, -6, -5, 8, 10, -55]

result=0
for i in list: # вычисляем сумму отрицательных чисел
    if i<0:
        result=result+i
    else:
        continue
print("сумма отрицательных чисел: ",result)

result=0
for i in list: # вычисляем сумму четных чисел
    if i%2==0:
        result=result+i
    else:
        continue
print("сумма четных чисел: ",result)

result=0
for i in list: # вычисляем сумму нечетных чисел
    if i%2!=0:
        result=result+i
    else:
        continue
print("сумма нечетных чисел: ",result)

result=1
for i in list: # вычисляем произведение элементов кратных 3
    if i%3==0:
        result=result*i
    else:
        continue
print("произведение элементов кратных 3: ",result)

result=1
min_number=min(list)
max_number=max(list)
for i in list: # вычисляем произведение элементов между минимальным и максимальным элементом
    if min_number<i<max_number:
        result=result*i
    else:
        continue
print("произведение элементов между минимальным и максимальным элементом: ",result)

# Вычисляем сумму элементов, находящихся между первым и последним
# положительными элементами

for i in list:
    if list[-1] < 0:
        del list[-1]
    else:
        break

for i in list:
    if i < 0:
        del list[0]
    else:
        break

del list[0]
del list[-1]
result = 0
for i in list:
    result = result + i
print("Сумма элементов между првым и последним полжительными элементами: ", result)

# ЗАДАНИЕ 2

# list = [-2, 5, -6, -7, 10, -55, 20, -3]
# list_result = []
# for i in list:  # Создаем список целых только из четных чисел
#     if i % 2 == 0:
#         list_result.append(i)
#     else:
#         continue
# print("Список из четных чисел: ",list_result)
#
# list_result_2 = []
# for i in list:  # Создаем список целых только из нечетных чисел
#     if i % 2 != 0:
#         list_result_2.append(i)
#     else:
#         continue
# print("Список из нечетных чисел: ", list_result_2)
#
# negative_list = []
# for i in list:  # Создаем список целых только из отрицательных чисел
#     if i < 0:
#         negative_list.append(i)
#     else:
#         continue
# print("Список из отрицательных чисел: ", negative_list)
#
#
# positive_list =[]
# for i in list:  # Создаем список целых только из положительных чисел
#     if i > 0:
#         positive_list.append(i)
#     else:
#         continue
#
# print("Список из положительных чисел: ",positive_list)
