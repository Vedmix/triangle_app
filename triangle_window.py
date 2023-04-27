
import customtkinter

from math import *

from math import acos, degrees, sqrt, sin

from functions_triangle import *

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("290x230+700+500")
app.title("Triangle")
app.resizable(width=False, height=False)


def result():

    app.withdraw()

    result = customtkinter.CTk()
    result.title("Triangle")
    result.geometry("400x280")

    frame_1 = customtkinter.CTkFrame(master=result)
    frame_1.pack(pady=20, padx=20, fill="both", expand=True)

    text1 = entry_1.get()
    text2 = entry_2.get()
    text3 = entry_3.get()

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

        result.geometry("500x190")
        app.resizable(width=False, height=False)
        label_1 = customtkinter.CTkLabel(master=frame_1, text="Такого треугольника не существует!", justify=customtkinter.LEFT, font=("Arial", 15))
        label_1.pack(pady=10, padx=10)
        button_1 = customtkinter.CTkButton(master=frame_1, width=100, text='Закрыть', font=("Arial", 15), command=result.quit)
        button_1.pack(pady=10, padx=10)

    if (AB + BC > AC) and (BC + AC > AB) and (AB + AC > BC):

        if (AB + BC > AC) and (BC + AC > AB) and (AB + AC > BC):

            if AB == BC == AC:
                type_triangle = 'Равносторонний треугольник'

            elif (round(angle_BAC, 15) == round((pi/2), 15)) or (round(angle_ABC, 15) == round((pi/2), 15)) or (round(angle_BCA, 15) == round((pi/2), 15)):
                type_triangle = 'Прямоугольный треугольник'

            elif (round(angle_BAC, 15) < round((pi/2), 15)) and (round(angle_ABC, 15) < round((pi/2), 15)) and (round(angle_BCA, 15) < round((pi/2), 15)):
                type_triangle = 'Остроугольный треугольник'

            elif (round(angle_BAC, 15) > round((pi/2), 15)) or (round(angle_ABC, 15) > round((pi/2), 15)) or (round(angle_BCA, 15) > round((pi/2), 15)):
                type_triangle = 'Тупоугольный треугольник'

            elif (AB != BC == AC) or (AB == BC != AC) or (AB == AC != BC):
                type_triangle='Равнобедренный треугольник'

        text_1 = customtkinter.CTkTextbox(master=frame_1, width=320, height=170)
        text_1.place(x=20, y=20)
        text_1.insert("0.0", "Введённые координаты:\nTочкa A: ({}, {})\nTочкa B: ({}, {})\nTочкa C: ({}, {})\n"
                             "Тип: {}\n"
                             "Периметр треугольника: {}\n"
                             "Площадь треугольника: {}\n"
                             "Длины сторон:\nСторона АВ: {}\nСторона ВС: {}\nСторона АC: {}\n"
                             "Углы треуголька:\nУгол BAC: {}°\nУгол ABC: {}°\nУгол BCA: {}°\n"
                             "Уравнения сторон:\nАВ: {}\nВС: {}\nАC: {}\n"
        .format(x1, y1, x2, y2, x3, y3, type_triangle, '%.2f' % perimeter_t(AB, BC, AC), '%.2f' % square(AB, BC, AC),
        '%.2f' % AB, '%.2f' % BC, '%.2f' % AC, '%.2f' % degrees(angle_BAC), '%.2f' % degrees(angle_ABC),
        '%.2f' % degrees(angle_BCA), equation_side(x1, y1, x2, y2), equation_side(x2, y2, x3, y3), equation_side(x1, y1, x3, y3)))
        button_1 = customtkinter.CTkButton(master=frame_1, width=100, text='Закрыть', font=("Arial", 15),
                                           command=app.quit)
        button_1.place(x=140, y=200)

    else:
        result.geometry("500x150")
        app.resizable(width=False, height=False)

        label_1 = customtkinter.CTkLabel(master=frame_1, text="Такого треугольника не существует!", justify=customtkinter.LEFT, font=("Arial", 15))
        label_1.pack(pady=10, padx=10)

        button_1 = customtkinter.CTkButton(master=frame_1, width=100, text='Закрыть', font=("Arial", 15), command=result.quit)
        button_1.pack(pady=10, padx=10)

    result.mainloop()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

entry_1 = customtkinter.CTkEntry(master=frame_1, width=210, placeholder_text="       Координаты точки А", font=("Arial", 15))
entry_1.place(x=20, y=20)

entry_2 = customtkinter.CTkEntry(master=frame_1, width=210, placeholder_text="       Координаты точки B", font=("Arial", 15))
entry_2.place(x=20, y=60)

entry_3 = customtkinter.CTkEntry(master=frame_1, width=210, placeholder_text="       Координаты точки C", font=("Arial", 15))
entry_3.place(x=20, y=100)

button_1 = customtkinter.CTkButton(master=frame_1, width=100, text='Готово', font=("Arial", 15), command=result)
button_1.place(x=20, y=140)

button_1 = customtkinter.CTkButton(master=frame_1, width=100, text='Закрыть', font=("Arial", 15), command=app.quit)
button_1.place(x=129, y=140)

app.mainloop()