from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter.font import BOLD

top = Tk()


w = top.winfo_screenwidth()
h = top.winfo_screenheight()
top.geometry("%dx%d" % (w, h))




# NavBar Start
name = Label(top, text="TallyPrime", fg='pink', bg='#3a646b', font=(
    "Arial", 13), anchor='w').place(x=0, y=0, width=1366, height=60)
name = Label(top, text="Gate WayOf Tally", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=0, y=60, width=1366, height=13)
name = Label(top, text="MANAGE", fg='#00c8ff', bg='#3a646b', font=(
    'Arial 9 underline'), anchor='w').place(x=110, y=9, width=206, height=10)

b1 = Button(top, text="K:Company", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=120, y=33)
b2 = Button(top, text="Y:Data", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=275, y=33)
b3 = Button(top, text="Z:Exchange", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=395, y=33)
b4 = Button(top, text="  G:Go To  ", activeforeground="black", activebackground="white",
            fg='black', bg='white', borderwidth=0, underline=2, font=('Arial 10 bold'),).place(x=565, y=33)
b5 = Button(top, text="O:Import", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=825, y=33)
b6 = Button(top, text="E:Export", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=925, y=33)
b7 = Button(top, text="M:E-mail", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=1025, y=33)
b8 = Button(top, text="P:Print", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=1127, y=33)
b9 = Button(top, text="F1:Help", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=1227, y=33)

# NavBar End



name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1220, y=60, width=147, height=700)

menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=753, y=250, width=202, height=300)

menuname = Label(top,text="Display More Reports", fg='white', bg='#0851a8', borderwidth=2, font=(
    'Arial 9 '), anchor='center').place(x=753, y=250, width=202, height=19)

menuname = Label(top,text="ACCOUNTING", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 7 '), anchor='center').place(x=753, y=288, width=202, height=19)


b10 = Button(top,text = "Trial Balance",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.440,relwidth=.148)
b11 = Button(top,text = "Day Book",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.480,relwidth=.148)
b12 = Button(top,text = "Cash Flow",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.520,relwidth=.148)
b13 = Button(top,text = "Funds Flow",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.560,relwidth=.148)
# b14 = Button(top,text = "Stock Transfer Journal Register",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.600,relwidth=.148)
# b15 = Button(top,text = "Physical Stock Register",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.640,relwidth=.148)
# b16 = Button(top,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.680,relwidth=.148)


# name = Label(top, fg='black',bg='#8accf2',font=('Arial 7 bold')).place(x = 506,y = 2,width=300,height=500,)


# name = Label(top, text = "Name",fg='pink',bg='gray').place(x = 80,y = 50,width=60,height=30)
# email = Label(top, text = "Email",fg='pink',bg='gray').place(x = 80, y = 90,width=60,height=30)
# password = Label(top, text = "Password",fg='pink',bg='gray').place(x = 80, y = 130,width=60,height=30)
# address = Label(top,text="Address",fg='pink',bg='gray').place(x = 80, y=170,width=60,height=30)
# e1 = Entry(top,fg='white',bg='blue').place(x = 150, y = 50,width=300,height=30)
# e2 = Entry(top,fg='white',bg='blue').place(x = 150, y = 90,width=300,height=30)
# e3 = Entry(top,fg='white',bg='blue',show='*').place(x = 150, y = 130,width=300,height=30)
# e4 = Entry(top,fg='white',bg='blue').place(x = 150, y = 170,width=300,height=30)
# checkvar1 = IntVar()
# checkvar2 = IntVar()
# checkvar3 = IntVar()

# chkbtn1 = Checkbutton(top, text = "Python", variable = checkvar1,  height = 2, width = 10)
# chkbtn2 = Checkbutton(top, text = "C++", variable = checkvar2,  height = 2, width = 10)
# chkbtn3 = Checkbutton(top, text = "Java", variable = checkvar3,  height = 2, width = 10)
# chkbtn1.place(x=140,y=250)
# chkbtn2.place(x=220,y=250)
# chkbtn3.place(x=300,y=250)
# radio = IntVar()
# name = Label(top, text = "Gender",fg='pink',bg='gray').place(x = 80,y = 290,width=60,height=30)
# R2 = Radiobutton(top, text="Male", variable=radio, value=2)
# R2.place(x=155,y=295)
# R3 = Radiobutton(top, text="Female", variable=radio, value=3)
# R3.place(x=220,y=295)
# R4 = Radiobutton(top, text="Other", variable=radio, value=4)
# R4.place(x=300,y=295)
# course=['Kerala','Karnataka','Thamilnadu','Maharashtra']
# name = Label(top, text = "State",fg='pink',bg='gray').place(x = 80,y = 330,width=370,height=30)
# cmb=ttk.Combobox(value=course,width=50,height=30)
# cmb.place(x=80,y=370)
# my_frame=Frame(top)
# my_scrollbar=Scrollbar(my_frame, orient=VERTICAL)

# label4=Label(top, text='Year Of Experience',fg='pink',bg='gray').place(x=80,y=400,width=130,height=30)

# my_listbox = Listbox(my_frame,yscrollcommand=my_scrollbar.set)
# my_scrollbar.config(command=my_listbox.yview)
# my_scrollbar.pack(side=RIGHT,fill=Y)
# my_frame.place(x=220,y=400)

# my_listbox.place (x=220,y=600)
# for line in range(20):
#  my_listbox.insert(END, "" + str(line))
# my_listbox.pack( side = LEFT )
# my_scrollbar.config( command = my_listbox.yview )
# b1 = Button(top,text = "submit",command = fun,activeforeground = "yellow",
# activebackground = "pink",fg='white',bg='red',pady=5, padx=80,width=5)
# b2 = Button(top,text = "submit",command = fun,activeforeground = "yellow",
# activebackground = "pink",fg='white',bg='red',pady=5, padx=80,width=5)

# b1.place (x=10,y=50)
# b2.place (x=10,y=100)


top.mainloop()
