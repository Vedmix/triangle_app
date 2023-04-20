from tkinter import *
from functions_triangle import*

def show_result():
    # Создаем окно с результатами
    result_window = Toplevel()
    result_window.title("Результат")
    window.geometry("500x500+700+500")

    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    splitted_text1 = text1.split(';')
    x1, y1 = [float(splitted_text1[0]), float(splitted_text1[1])]
    splitted_text2 = text2.split(';')
    x2, y2 = [float(splitted_text2[0]), float(splitted_text2[1])]
    splitted_text3 = text3.split(';')
    x3, y3 = [float(splitted_text3[0]), float(splitted_text3[1])]

    label1 = Label(result_window, text="Введённые координаты:", font=("Arial", 14))
    label1.place(x=20, y=20)
    label2 = Label(result_window, text="Точка А: ({},{})".format(x1, y1), font=("Arial", 14))
    label2.place(x=20, y=50)
    label3 = Label(result_window, text="Точка В: ({},{})".format(x2, y2), font=("Arial", 14))
    label3.place(x=20, y=80)
    label4 = Label(result_window, text="Точка С: ({},{})".format(x3, y3), font=("Arial", 14))
    label4.place(x=20, y=110)

    result_window.mainloop()


window = Tk()
window.title('triangle')
window.geometry("420x200+700+500")
window.resizable(width=False, height=False)


label1 = Label(text="Координаты точки А:", font=("Arial", 14))
label1.place(x=20, y=20)
entry1 = Entry(window, width=15, font=('Arial', 14))
entry1.place(x=220, y=20)

label2 = Label(text="Координаты точки B:", font=("Arial", 14))
label2.place(x=20, y=60)
entry2 = Entry(window, width=15, font=('Arial', 14))
entry2.place(x=220, y=60)

label3 = Label(text="Координаты точки C:", font=("Arial", 14))
label3.place(x=20, y=100)
entry3 = Entry(window, width=15, font=('Arial', 14))
entry3.place(x=220, y=100)


btm_done = Button(window, bg='white', text='Готово', font=('Arial', 14), command=show_result)
btm_done.place(x=180, y=150, width=100, height=30)

btm_escape = Button(window, bg='white', text='Закрыть', font=('Arial', 14), command=window.quit)
btm_escape.place(x=290, y=150, width=100, height=30)



window.mainloop()







