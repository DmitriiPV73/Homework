# Задание 1

# def text_screen ():
#     print("\"Don't let the noise of others' opinions\ndrown out your own inner voice.\""
#           "\n                      Steve Jobs")
#
# text_screen()

# Задание 2

# def numbers (a,b):
#     if a<b:
#         a1=a
#         b1=b
#     else:
#         a1 = b
#         b1 = a
#     li=list(range(a1,b1))
#     for i in li:
#         if i%2 != 0:
#             print(i)
#         else:
#             continue
#
# numbers(15,4)

# Задание 3

# def line (symbol, l, direction):
#     if direction=="h":
#         print(symbol*l)
#     elif direction=="v":
#         for i in range(l):
#             print(symbol)
#
#
# sumbol=input("Веди символ  ")
# l=int(input("Введи длину  "))
# while True:
#     direction=input("Введи \"H\", если по горионтали, или \"V\", если по верткали ")
#     direction=direction.lower()
#     if direction not in ("h", "v"):
#         print("Неверно уазано направение. Попробуйте снова.")
#         continue
#     else:
#         line(sumbol,l,direction)
#         break



# Задание 4

# def max_number (a,b,c,d):
#     list=[a,d,c,d]
#     return max(list)
#
# result=max_number(5,34,2,65)
# print(result)

# Задание 5

# def numbers (a,b):
#     if a<b:
#         a1=a
#         b1=b
#     else:
#         a1 = b
#         b1 = a
#     li=list(range(a1,b1))
#     return sum(li)
#
# result=numbers(15,4)
# print("Сумма чисел в диапазоне:",result)


# Задание 6

# def number (x):
#     if x<=1:
#         return False
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             return False
#         else:
#             return True
#
#
# x=int(input("Введи число для проверки  "))
# pesult=number(x)
# print(pesult)

# Задание 7

def partial_number (x):
    x = str(x)
    x = list(x)
    sum_1=int(x[0])+int(x[1])+int(x[2])
    sum_2=int(x[3])+int(x[4])+int(x[5])

    if sum_1==sum_2:
        return True
    else:
        return False

result=partial_number(723422)
print(result)