from tkinter import *
from tkinter import font

win = Tk() # создаем окно
win.title("Введение в язык программирования Python. Модуль 3. Циклы.") # называем окно

w=win.winfo_screenwidth()//2-400 # расчет смещения окна по горизонтали
h=win.winfo_screenheight()//2-250 # расчет смещения окна по вертикали
win.geometry(f'800x500+{w}+{h}') # размр окна, смещение на середину

Label(win, text="Модуль 4. Стороки. Списки.", font=("Arial Bold", 15), fg="#000099").pack()
Label(win, text="Часть 1.", font=("Arial Bold", 15), fg="#000099").pack()
Label(win, text="Задание 2.", font=("Arial Bold", 15), fg="#4682B4").pack(anchor=NW)

font_1=font.Font(family="Arial Bold",  size=13, slant="italic")
Label(win, text="Пользователь вводит с клавиатуры текст.", font=font_1).pack(anchor=NW, padx=10)
Label(win, text="Пользователь вводит с клавиатуры зарезервированные слова.", font=font_1).pack(anchor=NW, padx=10)
Label(win, text="Найти в тексте зарезервированные слова.", font=font_1).pack(anchor=NW, padx=10)
Label(win, text="Изменить регистр зарезервированных слов на верхний.", font=font_1).pack(anchor=NW, padx=10)

def data():
    text1 = line_1.get() # Присваиваем введенное значение переменной
    list1 = text1.split() # Перевод текста в список
    text2 = line_2.get() # Присваиваем введенное значение переменной
    list2 = text2.split() # Перевод текста в список

    len_list1 = len(list1)  # длина списка
    len_list2 = len(list2)

    for i in range(len_list2):
        for j in range(len_list1):
            if list2[i] == list1[j]:
                list2[i] = list2[i].upper()  # Переход на верхний регистр
                list1[j] = list1[j].upper()  # Переход на верхний регистр основного текста
            else:
                continue

    text = " ".join(list1)  # Преобразуем список в текст с пробелами
    Label(win, text=text, font=("Arial Bold", 15)).pack()



Label(win, text="Введи текст", font=("Arial Bold", 16)).pack(pady=5)
line_1 = Entry(win, width=50, font=("Arial Bold", 16)) # Данные окна ввода
line_1.pack(pady=10)

Label(win, text="Введи слова", font=("Arial Bold", 16)).pack(pady=5)
line_2 = Entry(win, width=50, font=("Arial Bold", 16)) # Данные окна ввода
line_2.pack(pady=10)

label = Label(win, font=("Arial Bold", 9)) # Характеристики текста в строке ВЫВОДА результата

button = Button(win, text="Выполнить!", font=("Arial Bold", 16), command=data) #Вводим кнопку запуска, ссылка на функцию


button.pack()
label.pack()

win.mainloop()