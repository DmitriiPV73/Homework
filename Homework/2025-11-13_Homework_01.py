from tkinter import *
from tkinter import font

win = Tk() # создаем окно
win.title("Введение в язык программирования Python. Модуль 3. Циклы.") # называем окно

w=win.winfo_screenwidth()//2-300 # расчет смещения окна по горизонтали
h=win.winfo_screenheight()//2-200 # расчет смещения окна по вертикали
win.geometry(f'600x400+{w}+{h}') # размр окна, смещение на середину

Label(win, text="Модуль 4. Стороки. Списки.", font=("Arial Bold", 15), fg="#000099").pack()
Label(win, text="Часть 1.", font=("Arial Bold", 15), fg="#000099").pack()
Label(win, text="Задание 1.", font=("Arial Bold", 15), fg="#4682B4").pack(anchor=NW)

font_1=font.Font(family="Arial Bold",  size=13, slant="italic")
Label(win, text="Пользователь вводит с клавиатуры строку.", font=font_1).pack(anchor=NW, padx=10)
Label(win, text="Проверить, является ли строка палиндромом.", font=font_1).pack(anchor=NW, padx=10)

def data():
    text = line_1.get()  # Присваиваем введенноьу тексту значение переменной
    text = text.replace(" ","") # Убираем пробелы
    text = text.lower() # Приводим к одному регистру

    if text == text[::-1]: #сравниваем с текстом в обратном порядке. Границы не указываются.
         Label(win, text="Палиндром", font=("Arial Bold",15)).pack(pady=5)
    else:
         Label(win, text="Не палиндром", font=("Arial Bold",15)).pack()


Label(win, text="Введи строку ", font=("Arial Bold", 16)).pack()

label = Label(win, font=("Arial Bold", 9)) # Характеристики текста в строке ВЫВОДА результата

button = Button(win, text="Выполнить!", font=("Arial Bold", 16), command=data) #Вводим кнопку запуска, ссылка на функцию
line_1 = Entry(win, width=50, font=("Arial Bold", 16)) # Данные окна ввода
line_1.pack(pady=10)

button.pack(pady=10)
label.pack(pady=5)
win.mainloop()




