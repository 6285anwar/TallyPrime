from distutils.cmd import Command
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from turtle import Screen, onclick
from cProfile import label
from textwrap import fill
from tkinter import *
from tkinter import ttk

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
    b1s = Button(top,text = "   Capital Account", command=groupsummry, activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b1s.place(x=0,y=220,width=980,height=18)
    l3f6=Label(f16,text="32424.00",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=0,anchor="nw") 
    f17=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    f17.place(x=1099,y=145,width=120,height=420)
    l4f6=Label(f17,text="456460.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=0,anchor="nw")

    b2s = Button(top,text = "   Current Liabilities", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b2s.place(x=0,y=250,width=980,height=18)
    l3f6=Label(f16,text="32445624.00",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=30,anchor="nw")
    l4f6=Label(f17,text="456460.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=30,anchor="nw")

    b3s = Button(top,text = "   Current Assets", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b3s.place(x=0,y=280,width=980,height=18)
    l3f6=Label(f16,text="32424.00",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=60,anchor="nw")
    l4f6=Label(f17,text="456475660.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=60,anchor="nw")

    b4s = Button(top,text = "   Sales Accounts", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b4s.place(x=0,y=320,width=980,height=18)
    l3f6=Label(f16,text="424.00",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=100,anchor="nw")
    l4f6=Label(f17,text="56475660.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=100,anchor="nw")

    b5s = Button(top,text = "   Purchase Accounts", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b5s.place(x=0,y=350,width=980,height=18)
    l3f6=Label(f16,text="21424.00",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=130,anchor="nw")
    l4f6=Label(f17,text="8560.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=130,anchor="nw")

    b6s = Button(top,text = "   Direct Expence", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b6s.place(x=0,y=380,width=980,height=18)
    l3f6=Label(f16,text="1424.00",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=160,anchor="nw")
    l4f6=Label(f17,text="6560.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=160,anchor="nw")

    b7s = Button(top,text = "   Indirect Expence", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b7s.place(x=0,y=410,width=980,height=18)
    l3f6=Label(f16,text="21424.00",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=190,anchor="nw")
    l4f6=Label(f17,text="76560.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=190,anchor="nw")

    b8s = Label(top,text = "    Differnce in opening balance", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  9 italic'),anchor="w")
    b8s.place(x=0,y=433,width=980,height=18)
    l3f6=Label(f16,text="741424.00",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=215,anchor="nw")
    l4f6=Label(f17,text="12146560.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=215,anchor="nw")



   

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
    




    f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=579,width=977,height=25)
    l5f6=Label(f18,text=" G r a n d  T o t a l",font=("Arial",11,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=0,y=0,anchor="nw")
    f19=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=978,y=579,width=120,height=25)
    l6f6=Label(f19,text="544650.00",font=("Arial",11,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")
    f20=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=1099,y=579,width=120,height=25)
    l7f6=Label(f20,text="544650.00",font=("Arial",11,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")


def groupsummry():
    sideheading = Label(top, text="Group Summary", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    sideheadingcolor = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1219, height=604)
    
    b4 = Button(top, text="x", command=trialbalance, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1204, y=60,height=12)

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
    b1s = Button(top,text = "   capital account ledger", command=ledgermonthlysummary, activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b1s.place(x=0,y=220,width=980,height=18)
    l3f6=Label(f16,text="-------",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=0,y=0,anchor="nw") 
    f17=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    f17.place(x=1099,y=145,width=120,height=420)
    l4f6=Label(f17,text="456460.00",font=("Arial",10),bg="white",fg="black")
    l4f6.place(x=0,y=0,anchor="nw")

    f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=579,width=977,height=25)
    l5f6=Label(f18,text=" G r a n d  T o t a l",font=("Arial",11,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=0,y=0,anchor="nw")
    f19=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=978,y=579,width=120,height=25)
    l6f6=Label(f19,text="-------",font=("Arial",11,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")
    f20=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=1099,y=579,width=120,height=25)
    l7f6=Label(f20,text="456460.00",font=("Arial",11,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")


def ledgermonthlysummary():
    sideheading = Label(top, text="Ledger Monthly Summary", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    sideheadingcolor = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1219, height=604)
    
    b4 = Button(top, text="x", command=groupsummry, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1204, y=60,height=12)

    global selected_ledgers_frame
    selected_ledgers_frame=Frame(top,bg="white",relief=RAISED,bd=0)
    selected_ledgers_frame.place(x=1, y=73,width=1219, height=604)
    
    f11=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=0.5)
    f11.grid(row=1,column=0,columnspan=3,ipadx=410,ipady=5)
    l1f1=Label(f11,text="    P e r t i c u l a r s",font=("Arial",11),fg="black",bg="white",anchor="w", borderwidth=0,relief=GROOVE,width=5,height=4)
    l1f1.pack(fill=X,pady=2,padx=2)

    f12=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=0.5)
    f12.place(x=873,y=0,width=346,height=40)
    l1f2=Label(f12,text="ledger Name",font=("Arial",8,"italic"),bg="white",fg="black")
    l1f2.place(x=175,y=7,anchor="center")
    l1f2=Label(f12,text="Company Name",font=("Arial",8,"bold"),bg="white",fg="black")
    l1f2.place(x=100,y=25,anchor="center")
    l1f3=Label(f12,text="For 1-1-1235",font=("Arial",8),bg="white",fg="black")
    l1f3.place(x=200,y=25,anchor="w")

    f111=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=0.5)
    f111.place(x=873,y=40,width=241,height=23)
    l1f2=Label(f111,text="Transactions",font=("Arial",9,"bold"),bg="white",fg="black",)
    l1f2.place(x=120,y=9,anchor="center")

    f14=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=873,y=63,width=120,height=23)
    l1f5=Label(f14,text="Debit",font=("Arial",9),bg="white",fg="black")
    l1f5.place(x=40,y=10,anchor="w")
    f15=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=994,y=63,width=120,height=23)
    l2f5=Label(f15,text="Credit",font=("Arial",9),bg="white",fg="black")
    l2f5.place(x=40,y=10,anchor="w")

    f15a=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f15a.place(x=1115,y=40,width=104,height=46)
    l2f5a=Label(f15a,text="Closing\nBalance",font=("Arial",10,"bold"),bg="white",fg="black")
    l2f5a.place(x=20,y=20,anchor="w")

    f16=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    f16.place(x=873,y=95,width=120,height=330)
    f17=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    f17.place(x=994,y=95,width=120,height=330)
    f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    f18.place(x=1115,y=95,width=104,height=330)

    b8s = Label(top,text = " Opening balance", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  9 italic'),anchor="w")
    b8s.place(x=0,y=185,width=874,height=18)
    l3f6=Label(f16,text="741424.00",font=("Arial",10,"bold"),bg="white",fg="black")
    l3f6.place(x=0,y=15,anchor="nw")
    l4f6=Label(f17,text="12146560.00",font=("Arial",10,"bold"),bg="white",fg="black")
    l4f6.place(x=0,y=15,anchor="nw")
    l5f6=Label(f18,text="00000.00",font=("Arial",10,"bold"),bg="white",fg="black")
    l5f6.place(x=0,y=15,anchor="nw")


    b2s = Button(top,text = " April",command=ledgervouchers, activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b2s.place(x=0,y=204,width=874,height=18)
    l3f6=Label(f16,text="32445624.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=35,anchor="nw")
    l4f6=Label(f17,text="456460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=35,anchor="nw")
    l5f6=Label(f18,text="8565445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=35,anchor="nw")


    b3s = Button(top,text = " May", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b3s.place(x=0,y=225,width=874,height=18)
    l3f6=Label(f16,text="846624.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=53,anchor="nw")
    l4f6=Label(f17,text="465460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=53,anchor="nw")
    l5f6=Label(f18,text="3455445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=53,anchor="nw")


    b4s = Button(top,text = " June", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b4s.place(x=0,y=245,width=874,height=18)
    l3f6=Label(f16,text="756624.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=74,anchor="nw")
    l4f6=Label(f17,text="95460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=74,anchor="nw")
    l5f6=Label(f18,text="34445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=74,anchor="nw")

    b5s = Button(top,text = " July", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b5s.place(x=0,y=265,width=874,height=17)
    l3f6=Label(f16,text="756624.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=93,anchor="nw")
    l4f6=Label(f17,text="95460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=93,anchor="nw")
    l5f6=Label(f18,text="34445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=93,anchor="nw")

    b6s = Button(top,text = " August", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b6s.place(x=0,y=285,width=874,height=17)
    l3f6=Label(f16,text="624.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=113,anchor="nw")
    l4f6=Label(f17,text="5460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=113,anchor="nw")
    l5f6=Label(f18,text="1445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=113,anchor="nw")

    b7s = Button(top,text = " September", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b7s.place(x=0,y=305,width=874,height=17)
    l3f6=Label(f16,text="7624.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=133,anchor="nw")
    l4f6=Label(f17,text="855460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=133,anchor="nw")
    l5f6=Label(f18,text="17445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=133,anchor="nw")

    b8s = Button(top,text = " October", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b8s.place(x=0,y=325,width=874,height=17)
    l3f6=Label(f16,text="47624.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=153,anchor="nw")
    l4f6=Label(f17,text="1855460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=153,anchor="nw")
    l5f6=Label(f18,text="7445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=153,anchor="nw")

    b9s = Button(top,text = " November", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b9s.place(x=0,y=345,width=874,height=17)
    l3f6=Label(f16,text="624.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=173,anchor="nw")
    l4f6=Label(f17,text="155460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=173,anchor="nw")
    l5f6=Label(f18,text="445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=173,anchor="nw")

    b10s = Button(top,text = " December", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b10s.place(x=0,y=365,width=874,height=17)
    l3f6=Label(f16,text="4624.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=193,anchor="nw")
    l4f6=Label(f17,text="6155460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=193,anchor="nw")
    l5f6=Label(f18,text="3445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=193,anchor="nw")

    b11s = Button(top,text = " January", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b11s.place(x=0,y=385,width=874,height=17)
    l3f6=Label(f16,text="3324.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=213,anchor="nw")
    l4f6=Label(f17,text="5460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=213,anchor="nw")
    l5f6=Label(f18,text="77445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=213,anchor="nw")

    b12s = Button(top,text = " February", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b12s.place(x=0,y=405,width=874,height=17)
    l3f6=Label(f16,text="43324.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=233,anchor="nw")
    l4f6=Label(f17,text="55460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=233,anchor="nw")
    l5f6=Label(f18,text="7445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=233,anchor="nw")

    b13s = Button(top,text = " March", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 '),anchor="w")
    b13s.place(x=0,y=425,width=874,height=17)
    l3f6=Label(f16,text="143324.00",font=("Arial",9),bg="white",fg="black")
    l3f6.place(x=0,y=253,anchor="nw")
    l4f6=Label(f17,text="255460.00",font=("Arial",9),bg="white",fg="black")
    l4f6.place(x=0,y=253,anchor="nw")
    l5f6=Label(f18,text="37445.00",font=("Arial",9),bg="white",fg="black")
    l5f6.place(x=0,y=253,anchor="nw")



    f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=398,width=874,height=20)
    l5f6=Label(f18,text=" G r a n d  T o t a l",font=("Arial",10,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=0,y=0,anchor="nw")

    f19=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=874,y=398,width=120,height=20)
    l6f6=Label(f19,text="544650.00",font=("Arial",10,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")

    f20=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=994,y=398,width=120,height=20)
    l7f6=Label(f20,text="544650.00",font=("Arial",10,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")

    f21=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f21.place(x=1114,y=398,width=104,height=20)
    l7f6=Label(f21,text="452650.00",font=("Arial",10,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")


   

def ledgervouchers():
    sideheading = Label(top, text="Ledger Vouchers", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    sideheadingcolor = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1219, height=604)
    
    b4 = Button(top, text="x", command=ledgermonthlysummary, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1204, y=60,height=12)

    global selected_ledgers_frame
    selected_ledgers_frame=Frame(top,bg="white",relief=RAISED,bd=0)
    selected_ledgers_frame.place(x=1, y=73,width=1219, height=504)
    
    f11=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=0.5)
    f11.grid(row=1,column=0,columnspan=3,ipadx=410,ipady=5)
    l1f1=Label(f11,text="    Ledger :",font=("Arial",11),fg="black",bg="white",anchor="w", borderwidth=0,relief=GROOVE,width=44,height=1)
    l1f1.pack(fill=X,pady=2,padx=2)

    f111=Frame(selected_ledgers_frame,bg="white",relief=RAISED)
    f111.place(x=75,y=3,width=100,height=23)
    l1f2=Label(f111,text=" Ledger name",font=("Arial",10,"bold"),bg="white",fg="black",)
    l1f2.place(x=40,y=10,anchor="center")
    
    l1f2=Label(top,text="April 1-2020 to April 1-2021",font=("Arial",10,"bold"),bg="white",fg="black")
    l1f2.place(x=1120,y=89,anchor="center")
    

    t3 = ttk.Treeview(top)
    t3['columns']=('Date','Particulars','Vch Type','Vch No.','Debit','Credit')
    t3.column('#0', width=0, stretch=NO)
    t3.column('Date', anchor=W, width=100,minwidth=100)
    t3.column('Particulars', anchor=W, width=405,minwidth=425)
    t3.column('Vch Type', anchor=CENTER, width=125,minwidth=125)
    t3.column('Vch No.', anchor=CENTER, width=125,minwidth=125)
    t3.column('Debit', anchor=CENTER, width=125,minwidth=125)
    t3.column('Credit', anchor=CENTER, width=125,minwidth=125)
    
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0.00, rely=0.19, relheight=0, relwidth=0.893)

    t3.heading('#0', text='', anchor=CENTER)
    t3.heading('Date', text='Date', anchor=W)
    t3.heading('Particulars', text='Particulars', anchor=W, )
    t3.heading('Vch Type', text='Vch Type', anchor=CENTER)
    t3.heading('Vch No.', text='Vch No.', anchor=CENTER)
    t3.heading('Debit', text='Debit', anchor=CENTER)
    t3.heading('Credit', text='Credit', anchor=CENTER)
   
    t3.insert(parent='', index=0, iid=0, text='', values=('-----','-','-','-','-','-'))
    t3.place(x=0, y=107, height=569, width=1220)


    f18=Frame(t3,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=500,width=1220,height=40)
    l5f6=Label(f18,text=" Opening Balance :",font=("Arial",9),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=200,y=0,)

    l5f6s=Label(f18,text=" 4564545.00",font=("Arial",9,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6s.place(x=1100,y=0,)
    l5f7=Label(f18,text="        Current Tottal :",font=("Arial",9),bg="white",fg="black",borderwidth=0)
    l5f7.place(x=200,y=18,)

    f19=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=874,y=798,width=120,height=20)
    l6f6=Label(f19,text="544650.00",font=("Arial",10,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")

    f20=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=994,y=798,width=120,height=20)
    l7f6=Label(f20,text="544650.00",font=("Arial",10,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")

    f21=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
    f21.place(x=1114,y=98,width=104,height=20)
    l7f6=Label(f21,text="452650.00",font=("Arial",10,"bold"),bg="white",fg="black",borderwidth=0)
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