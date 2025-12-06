# Задание 1

# def text_screen ():
#     print("\"Don't compare yourself with anyone in this world...\nif you do so, you are insulting yourself.\""
#           "\n                      Bill Gates")
#
# text_screen()

# Задание 2

# def numbers (a,b):
#     """
#     Функция, котрая выводит все четные числа в диапазоне двух
#     чисел.
#     """
#
#     if a<b:
#         a1=a
#         b1=b
#     else:
#         a1 = b
#         b1 = a
#     li=list(range(a1,b1))
#     print("Четные числа диапазона: ", end="")
#
#     for i in li:
#         if i%2 == 0:
#             print(i, end=" ")
#         else:
#             continue
#
# numbers(21,9)

# Задание 3

# def square (symbol, l, x:bool):
#     """
#     Функция, которая выодит заполненный или пустой квадрат
#     по принятым символу, длине стороны, True - заполенный, False - путой
#     """
#     if x == True:
#         for i in range(l):
#             print(symbol*l)
#     elif x == False:
#
#         print(symbol*l)
#         i=2
#         for i in range(l-2):
#             print(symbol, end='')
#             print(" "*(l-2),end='')
#             print(symbol)
#         print(symbol * l)
#
#
# square("*",5,False)

# Задание 4

# def min_val (a,b, c, d, e):
#     """функция возвращает минимальное знаение из 5 чисел"""
#     list=[a,b, c, d, e]
#     return min(list)
#
# result=min_val(15,20,11,1,8)
# print("Минимальное из 5 чисел  ",result)

# Задание 5

# def composition(x,y):
#     """Фукция возращает произведение чисел в дипазоне"""
#     if x<y:
#         min_val=x
#         max_val=y
#     elif y<x:
#         min_val = y
#         max_val = x
#     l=list(range(min_val,max_val+1))
#
#     result=1
#     for i in l:
#         result=result*i
#
#     return result
#
#
# composition=composition(21,5)
# print("Произведение чисел в диапазоне:",composition)



# Задание 6

# def composition(x):
#     """Функция вовращает количество цифр в чсле"""
#     if x<0:
#         x=x*-1
#
#     x=str(x)
#
#     return len(x)
#
# result=composition(-83456)
# print("Количество цифр в числе: ", result)

# Задание 7

def composition(x):
    """
    Функция определяет, является ли число палиндромом
    Если палинбром - возвращает True
    Если не палиндром - возвраает False
    """
    line_x=str(x)
    list_x=list(line_x)
    count_x=len(list_x)
    divider=10**(count_x/2)

    count_x1=int(x//divider)
    count_x1=str(count_x1)
    count_x1=count_x1[::-1]
    count_x1=int(count_x1)

    count_x2=int(x%divider)

    if count_x2==count_x1:
        return True
    else:
        return False

result=composition(421987)
print(result)