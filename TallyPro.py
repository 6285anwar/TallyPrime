from tkinter import *
from turtle import Screen, onclick

top = Tk()

w = top.winfo_screenwidth()
h = top.winfo_screenheight()
top.geometry("%dx%d" % (w, h))


def home():
    name = Label(top, text="Gate WayOf Tally", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=0, y=60, width=1366, height=13)
    home = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1219, height=604)
  
    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1220, y=60, width=147, height=700)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=753, y=250, width=202, height=300)

    menuname = Label(top,text="Display More Reports", fg='white', bg='#0851a8', borderwidth=2, font=(
    'Arial 9 '), anchor='center').place(x=753, y=250, width=202, height=19)

    menuname = Label(top,text="ACCOUNTING", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 7 '), anchor='center').place(x=753, y=288, width=202, height=19)


    b10 = Button(top,text = "Trial Balance",command=trialbalance, activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.440,relwidth=.148)
    b11 = Button(top,text = "Day Book",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.480,relwidth=.148)
    b12 = Button(top,text = "Cash Flow",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.520,relwidth=.148)
    b13 = Button(top,text = "Funds Flow",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.560,relwidth=.148)




def trialbalance():
    trialbalanc = Label(top, text="Trial Balance", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='green', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1219, height=604)
    

    b4 = Button(top, text="x", command=home, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1204, y=60,height=12)

# side buttons 
    side1 = Button(top, text="  Period",activeforeground="black", activebackground="white",
            fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10  '),anchor='w').place(x=1224, y=63,height=27,width=138)
    side2 = Button(top, text="  Company",activeforeground="black", activebackground="white",
            fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=91,height=27,width=138)
    side3 = Button(top, text="  Group",activeforeground="black", activebackground="white",
            fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=120,height=27,width=138) 

    side4 = Button(top, text="  Ledger-wise",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=165,height=27,width=138)
    side5 = Button(top, text="  Monthly",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=194,height=27,width=138)
    side6 = Button(top, text="  ",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=223,height=27,width=138) 
    side7 = Button(top, text="  ",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=251,height=27,width=138) 
    side9 = Button(top, text="  ",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=280,height=27,width=138)
    side10 = Button(top, text="  ",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=309,height=27,width=138)

    side11 = Button(top, text="  Basis of Values",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=350,height=27,width=138)
    side12 = Button(top, text="  Change View",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=378,height=27,width=138)
    side12 = Button(top, text="  Exception Reports",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=406,height=27,width=138)
    side13 = Button(top, text="  Save View",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=434,height=27,width=138)

    side14 = Button(top, text="  New Column",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=480,height=27,width=138)
    side15 = Button(top, text="  Alter Column",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=508,height=27,width=138)
    side16 = Button(top, text="  Delete Column",activeforeground="black", activebackground="white",
             fg='#cccccc', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=536,height=27,width=138)
    side16 = Button(top, text="  Auto Column",activeforeground="black", activebackground="white",
             fg='black', bg='#f0f8fc', borderwidth=1, font=('Arial 10 '),anchor='w').place(x=1224, y=564,height=27,width=138)

    # particulars

    global selected_ledgers_frame
    selected_ledgers_frame=Frame(top,bg="white",relief=RAISED,bd=0)
    selected_ledgers_frame.place(x=1, y=73,width=1219, height=604)
    
    f11=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=0.5)
    f11.grid(row=1,column=0,columnspan=3,ipadx=440,ipady=5)
    l1f1=Label(f11,text="    P e r t i c u l a r s",font=("Arial",11),fg="black",bg="white",anchor="w", borderwidth=0,relief=GROOVE,width=10,height=4)
    l1f1.pack(fill=X,pady=2,padx=2)

    f12=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=0.5)
    f12.place(x=978,y=0,width=241,height=40)
    l1f2=Label(f12,text="Company Name",font=("Arial",9,"bold"),bg="white",fg="black")
    l1f2.place(x=120,y=9,anchor="center")
    l1f3=Label(f12,text="1-1-1235",font=("Arial",8),bg="white",fg="black")
    l1f3.place(x=95,y=27,anchor="w")

    f111=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=0.5)
    f111.place(x=978,y=40,width=241,height=23)
    l1f2=Label(f111,text="Closing Balance",font=("Arial",9,"bold"),bg="white",fg="black",)
    l1f2.place(x=120,y=9,anchor="center")


    # l1f4=Label(f12,text="FOR 1-APR-20",font=("Arial",5,"bold"),bg="white",fg="black")
    # l1f4.place(x=1,y=30,anchor="w")

    # f13=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
    # f13.place(x=0,y=145,width=607,height=420)
    # f13bt1=Button(f13,text="1",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    # f13bt1.place(x=0,y=0,anchor="nw")
    # f13bt2=Button(f13,text="2",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    # f13bt2.place(x=0,y=30,anchor="nw")
    # f13bt3=Button(f13,text="3",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    # f13bt3.place(x=0,y=60,anchor="nw")
    # f13bt4=Button(f13,text="4",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    # f13bt4.place(x=0,y=90,anchor="nw")

    f14=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=978,y=63,width=120,height=23)
    l1f5=Label(f14,text="Debit",font=("Arial",9),bg="white",fg="black")
    l1f5.place(x=40,y=10,anchor="w")
    f15=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=1099,y=63,width=120,height=23)
    l2f5=Label(f15,text="Credit",font=("Arial",9),bg="white",fg="black")
    l2f5.place(x=40,y=10,anchor="w")


    f16=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    f16.place(x=978,y=145,width=120,height=420)
    b1s = Button(top,text = "   Capital Account", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b1s.place(x=0,y=220,width=980,height=20)
    l3f6=Label(f16,text="32424.00",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=0,anchor="nw") 
    f17=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    f17.place(x=1099,y=145,width=120,height=420)
    l4f6=Label(f17,text="456460.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=0,anchor="nw")

    # f161=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    # f161.place(x=978,y=160,width=120,height=420)
    # b2s = Button(top,text = "   Capital Account", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    # b2s.place(x=0,y=220,width=980,height=20)
    # l3f61=Label(f161,text="32424.00",font=("Arial",10),bg="white",fg="black")
    # l3f61.place(x=0,y=0,anchor="nw") 
    # f171=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    # f171.place(x=1099,y=145,width=120,height=420)
    # l4f61=Label(f171,text="456460.00",font=("Arial",10),bg="white",fg="black")
    # l4f61.place(x=0,y=0,anchor="nw")
    




    f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
    f18.place(x=0,y=565,width=607,height=30)
    l5f6=Label(f18,text="Grand Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=0,y=0,anchor="nw")

    f19=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
    f19.place(x=610,y=565,width=273,height=30)
    l6f6=Label(f19,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")

    f20=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
    f20.place(x=883,y=565,width=275,height=30)
    l7f6=Label(f20,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")







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


b10 = Button(top,text = "Trial Balance",command=trialbalance, activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.440,relwidth=.148)
b11 = Button(top,text = "Day Book",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.480,relwidth=.148)
b12 = Button(top,text = "Cash Flow",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.520,relwidth=.148)
b13 = Button(top,text = "Funds Flow",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='#a9ceeb',borderwidth=0,font=('Calibri  12')).place(relx=0.551, rely=0.560,relwidth=.148)


top.mainloop()