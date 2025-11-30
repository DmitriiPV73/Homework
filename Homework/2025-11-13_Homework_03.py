from tkinter import *
from tkinter import font

win = Tk()
win.title("Введение в язык программирования Python. Модуль 3. Циклы.") # называем окно
w = win.winfo_screenwidth() // 2 - 300  # расчет смещения окна по горизонтали
h=win.winfo_screenheight()//2-250 # расчет смещения окна по вертикали
win.geometry(f'600x500+{w}+{h}') # размр окна, смещение на середину

Label(win, text="Модуль 4. Стороки. Списки.", font=("Arial Bold", 15), fg="#000099").pack()
Label(win, text="Часть 1.", font=("Arial Bold", 15), fg="#000099").pack()
Label(win, text="Задание 3.", font=("Arial Bold", 15), fg="#4682B4").pack(anchor=NW)

font_1=font.Font(family="Arial Bold",  size=13, slant="italic")
Label(win, text="Есть текст.", font=font_1).pack(anchor=NW, padx=10)
Label(win, text="Посчитать и вывести количество предложений.", font=font_1).pack(anchor=NW, padx=10)

Label(win, text="Введи текст или вставь скопированный", font=("Arial Bold", 16)).pack(pady=5)

text_box = Text(width=70, height=10, bg='#e0ffff') # Характеристики окна ввода текста
# text_box.pack(fill='both', expand=True)
text_box.pack(pady=5)

def data ():
    text=text_box.get("1.0","end") # Получение текста из окна. Обязательно начало и конец

    sentences=0 # Используем счетчик. Проверяем наличие . ! ?
    for char in text:
        if char in ".!?":
            sentences += 1

    text_box.delete("1.0","end") # Очищаем окно ввода.
    text_box.insert("1.0", "Количество предложений - ")
    text_box.insert("2.0", sentences) # Выводим в нем результат

# Кнопка запуска функции data для выполнения основной задачи
button = Button(win, text="Выполнить!", font=("Arial Bold", 16), command=data)

class Winpaste: # Создаем класс (шаблон) для работы с окном ввода текста
        def __init__(self): # Создаем конструктор класса (шаблона)
            win.bind("<Control-KeyPress>", self.keypress)
        # метод bind привязан к основному окну и контролирует в данном случае использование клавиш <Control-KeyPress>

            button.pack(pady=15)  # Вводим кнопку запуска, ссылка на функцию
            win.mainloop()

        @staticmethod # Декоратор. Указывает на то, что метод статический и не имеет обязательного параметра
        def keypress(event): # Функия в которой генерируется событие при нажатии клавиш
            if event.keycode == 86:
                event.widget.event_generate('<<Paste>>') # Комбинация клавиш 86 - вставить
            elif event.keycode == 67:
                event.widget.event_generate('<<Copy>>') # Комбинация клавиш 67 - копировать
            elif event.keycode == 88:
                event.widget.event_generate('<<Cut>>') # Комбинация клавиш 88 - удалить

# __name__ - специальная переменная которая хранит имя или значение текущего модуля
# __main__ - значение __name__ когда скрипт выполняется как основной (автоматически)
# ОБЯЗАТЕЛЬНО ПРИ ИСПОЛЬЗОВАНИИ ИМПОРТА
if __name__ == '__main__':
    app = Winpaste()


