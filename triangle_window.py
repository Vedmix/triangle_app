from tkinter import *
from functions_triangle import*
import matplotlib.pyplot as plt
def show_result():
    window.withdraw()
    result_window = Toplevel()
    result_window.title("Result")
    result_window.geometry("550x500+700+500")
    result_window.configure(bg='#09070F')
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    splitted_text1 = text1.split(';')
    x1, y1 = [float(splitted_text1[0]), float(splitted_text1[1])]
    splitted_text2 = text2.split(';')
    x2, y2 = [float(splitted_text2[0]), float(splitted_text2[1])]
    splitted_text3 = text3.split(';')
    x3, y3 = [float(splitted_text3[0]), float(splitted_text3[1])]
    AB = side(x1, y1, x2, y2)
    BC = side(x2, y2, x3, y3)
    AC = side(x1, y1, x3, y3)

    angle_BAC = angle(AC, AB, BC)
    angle_ABC = angle(AC, BC, AB)
    angle_BCA = angle(AB, BC, AC)

    if (x1 == x2 == x3) or (y1 == y2 == y3):
        label1 = Label(result_window, text="Такого треугольника не существует!", font=("Arial", 14))
        label1.pack()
    if (AB + BC > AC) and (BC + AC > AB) and (AB + AC > BC):
        label1 = Label(result_window, bg='#09070F',fg='white', text="Введённые координаты:", font=("Arial", 14))
        label1.place(x=20, y=20)
        label2 = Label(result_window, bg='#09070F',fg='white', text="Точка А: ({},{})".format(x1, y1), font=("Arial", 14))
        label2.place(x=20, y=50)
        label3 = Label(result_window, bg='#09070F',fg='white', text="Точка В: ({},{})".format(x2, y2), font=("Arial", 14))
        label3.place(x=20, y=80)
        label4 = Label(result_window, bg='#09070F',fg='white', text="Точка С: ({},{})".format(x3, y3), font=("Arial", 14))
        label4.place(x=20, y=110)
        label5 = Label(result_window, bg='#09070F',fg='white', text="Длины сторон:", font=("Arial", 14))
        label5.place(x=20, y=140)
        label6 = Label(result_window, bg='#09070F',fg='white', text="Сторона АВ: {}".format('%.2f' % AB), font=("Arial", 14))
        label6.place(x=20, y=170)
        label7 = Label(result_window, bg='#09070F',fg='white', text="Сторона ВС: {}".format('%.2f' % BC), font=("Arial", 14))
        label7.place(x=20, y=200)
        label8 = Label(result_window, bg='#09070F', fg='white',text="Сторона АC: {}".format('%.2f' % AC), font=("Arial", 14))
        label8.place(x=20, y=230)

        label9=Label(result_window, bg='#09070F', fg='white',text="Углы треуголька:", font=("Arial", 14))
        label9.place(x=260, y=20)
        label6 = Label(result_window, bg='#09070F',fg='white', text="Угол BAC: {}°".format('%.2f' % degrees(angle_BAC)), font=("Arial", 14))
        label6.place(x=260, y=50)
        label7 = Label(result_window, bg='#09070F', fg='white',text="Угол ABC: {}°".format('%.2f' % degrees(angle_ABC)), font=("Arial", 14))
        label7.place(x=260, y=80)
        label8 = Label(result_window, bg='#09070F', fg='white',text="Угол BCA: {}°".format('%.2f' % degrees(angle_BCA)), font=("Arial", 14))
        label8.place(x=260, y=110)

        label13 = Label(result_window, bg='#09070F',fg='white', text="Уравнения сторон:", font=("Arial", 14))
        label13.place(x=260, y=140)
        label14 = Label(result_window, bg='#09070F', fg='white',text="АВ: {}".format(equation_side(x1, y1, x2, y2)), font=("Arial", 14))
        label14.place(x=260, y=170)
        label15 = Label(result_window, bg='#09070F',fg='white', text="ВС: {}".format(equation_side(x2, y2, x3, y3)), font=("Arial", 14))
        label15.place(x=260, y=200)
        label16 = Label(result_window, bg='#09070F',fg='white', text="АC: {}".format(equation_side(x1, y1, x3, y3)), font=("Arial", 14))
        label16.place(x=260, y=230)

        if AB == BC == AC:
            label17 = Label(result_window, bg='#09070F',fg='white', text="{}".format('Тип >> "Равносторонний треугольник"'), font=("Arial", 14))
            label17.place(x=100, y=260)

        elif (angle_BAC == 1, 5708) or (angle_ABC == 1, 5708) or (angle_BCA == 1, 5708):
            label17 = Label(result_window, bg='#09070F',fg='white', text="{}".format('Тип >> "Прямоугольный треугольник"'), font=("Arial", 14))
            label17.place(x=100, y=260)

        elif (angle_BAC < 1, 5708) and (angle_ABC < 1, 5708) and (angle_BCA < 1, 5708):
            label17 = Label(result_window, bg='#09070F',fg='white', text="{}".format('Тип >> "Остроугольный треугольник"'), font=("Arial", 14))
            label17.place(x=100, y=260)

        elif (angle_BAC > 1, 5708) or (angle_ABC > 1, 5708) or (angle_BCA > 1, 5708):
            label17 = Label(result_window, bg='#09070F',fg='white', text="{}".format('Тип >> "Тупоугольный треугольник"'), font=("Arial", 14))
            label17.place(x=100, y=260)

        elif (AB != BC == AC) or (AB == BC != AC) or (AB == AC != BC):
            label17 = Label(result_window, bg='#09070F',fg='white', text="{}".format('Тип >> Равнобедренный треугольник'), font=("Arial", 14))
            label17.place(x=100, y=260)
        label17 = Label(result_window, bg='#09070F',fg='white', text="Периметр треугольника: {}".format('%.2f' % perimeter_t(AB, BC, AC)),font=("Arial", 14))
        label17.place(x=100, y=290)
        label17 = Label(result_window, bg='#09070F',fg='white', text="Площадь треугольника: {}".format('%.2f' % square(AB, BC, AC)),font=("Arial", 14))
        label17.place(x=100, y=320)

        fig, ax = plt.subplots()

        x, y = [x1, x2, x3], [y1, y2, y3]
        x1, y1 = [x1, x3], [y1, y3]

        plt.plot(x, y, color='black')
        plt.plot(x1, y1, color='black')
        plt.plot(x, y, 'o')
        plt.plot(x1, y1, 'o')

        ax.grid()
        plt.title('Ваш треугольник:')
        plt.show()

    else:
        label1 = Label(result_window, text="Такого треугольника не существует!", font=("Arial", 14))
        label1.pack()
    result_window.mainloop()


window = Tk()
window.title('triangle')
window.geometry("420x200+700+500")
window.configure(bg='#09070F')
window.resizable(width=False, height=False)
label1 = Label(text="Координаты точки А:", bg='#192133', font=("Arial", 14))
label1.place(x=20, y=20)
entry1 = Entry(window, width=15, bg='#192133', font=('Arial', 14))
entry1.place(x=220, y=20)
label2 = Label(text="Координаты точки B:", bg='#192133', font=("Arial", 14))
label2.place(x=20, y=60)
entry2 = Entry(window, width=15, bg='#192133', font=('Arial', 14))
entry2.place(x=220, y=60)
label3 = Label(text="Координаты точки C:", bg='#192133', font=("Arial", 14))
label3.place(x=20, y=100)
entry3 = Entry(window, width=15, bg='#192133', font=('Arial', 14))
entry3.place(x=220, y=100)
btm_done = Button(window, bg='#192133', text='Готово', font=('Arial', 14), command=show_result)
btm_done.place(x=180, y=150, width=100, height=30)
btm_escape = Button(window, bg='#192133', text='Закрыть', font=('Arial', 14), command=window.quit)
btm_escape.place(x=290, y=150, width=100, height=30)
window.mainloop()
