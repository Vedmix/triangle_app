from tkinter import *




def coordinates():
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    splitted_text1 = text1.split(';')
    splitted_text2 = text2.split(';')
    splitted_text3 = text3.split(';')
    points = [splitted_text1[0],splitted_text1[1],splitted_text2[0], splitted_text2[1],splitted_text3[0],splitted_text3[1]]
    # x1 = float(splitted_text1[0])
    # y1 = float(splitted_text1[1])
    # x1y1=[]
    #
    x2 = float()
    y2 = float()
    # x2y2 = []
    #
    x3 = float()
    y3 = float()
    # x3y3=[]


    # return x1,x2,x3,y1,y2,y3

def window2():
    window2 = Tk()
    window2.title('triangle')
    window2.geometry("1000x1000+700+500")
    window2.resizable(width=False, height=False)

window = Tk()
window.title('triangle')
window.geometry("420x200+700+500")
window.resizable(width=False, height=False)





label1 = Label(text="Координаты точки А:",font=("Arial", 14))
label1.place(x=20,y=20)
entry1=Entry(window, width = 15, font=('Arial', 14))
entry1.place(x=220,y=20)

label2 = Label(text="Координаты точки B:",font=("Arial", 14))
label2.place(x=20,y=60)
entry2=Entry(window, width = 15, font=('Arial', 14))
entry2.place(x=220,y=60)

label3 = Label(text="Координаты точки C:",font=("Arial", 14))
label3.place(x=20,y=100)
entry3=Entry(window, width = 15, font=('Arial', 14))
entry3.place(x=220,y=100)


btm_done= Button(window, bg='white', text='Готово', font=('Arial', 14), command = window2 )
btm_done.place(x=180,y=150, width=100, height=30)

btm_escape= Button(window, bg='white', text='Закрыть', font=('Arial', 14), command = window.quit)

btm_escape.place(x=290,y=150, width=100, height=30)
# coordinates()









window.mainloop()
