from tkinter import *

root = Tk()


background=Label(root,)
background.place(x=0,y=0,relwidth=1,relheight=1)

w = Label(root, text="Testo di prova su RaspBerry Pi 4") # This is the text I would like to make transparent.
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda e: root.destroy())

w.pack()

root.mainloop()








# # Import the required libraries
# from tkinter import *
# from tkinter import ttk


# # Create an instance of tkinter frame or window
# win = Tk()

# # Set the size of the window
# win.geometry("700x350")

# def on_click():
#    label.after(10, label.destroy())

# # Create a Label widget
# label = Label(win, text=" Deleting a Label in Python Tkinter", font=('Helvetica 15'))
# label.pack(pady=20)

# # Add a Button to Show/Hide Canvas Items
# ttk.Button(win, text="Delete", command=on_click).pack()

# win.mainloop()







# #Import the library
# from tkinter import *
# from tkinter import ttk

# #Create an instance of Tkinter frame
# win= Tk()

# #Set the window geometry
# win.geometry("750x200")

# #Create a Label
# Label(win, text= "Tkinter is a GUI Library in Python", font=('Helvetica 15 bold')).pack(pady=20)

# #Define a function to show the Main window
# def show_win():
#    win.deiconify()

# #Create another Toplevel Window
# new_win= Toplevel(win)
# new_win.geometry("700x250")
# new_win.title("NEW WINDOW")

# #Hide the Main Window
# win.withdraw()

# #Create a Button to Hide/ Reveal the Main Window
# button= ttk.Button(new_win, text="Show" ,command= show_win)
# button.pack(pady=50)

# win.mainloop()




# from tkinter import *
# from tkinter.ttk import *
# #tkinter window
# base = Tk()

# #This button can close the window
# button_1 = Button(base, text ="I close the Window", command = base.destroy)
# #Exteral paddign for the buttons
# button_1.pack(pady = 40)

# #This button closes the first button
# button_2 = Button(base, text ="I close the first button", command = button_1.destroy)
# button_2.pack(pady = 40)

# #This button closes the second button
# button_3 = Button(base, text ="I close the second button", command = button_2.destroy)
# button_3.pack(pady = 40)
# mainloop()





# # importing only those functions
# # which are needed
# from tkinter import * 
# from tkinter.ttk import *
  
# # creating tkinter window
# root = Tk()
  
# # Creating button. In this destroy method is passed
# # as command, so as soon as button 1 is pressed root
# # window will be destroyed
# btn1 = Button(root, text ="Button 1")
# btn1.pack(pady = 10)
  
# # Creating button. In this destroy method is passed
# # as command, so as soon as button 2 is pressed
# # button 1 will be destroyed
# btn2 = Button(root, text ="Button 2")
# btn2.pack(pady = 10)
  
# # after method destroying button-1
# # and button-2 after certain time
# btn1.after(3000, btn1.destroy)
# btn2.after(6000, btn2.destroy)
  
# # infinite loop
# mainloop()




# from tkinter import *

# class Window(Frame):

#     def __init__(self, master=None):
#         Frame.__init__(self, master)        
#         self.master = master

#         # widget can take all window
#         self.pack(fill=BOTH, expand=1)

#         # create button, link it to clickExitButton()
#         exitButton = Button(self, text="Exit", command=self.clickExitButton)

#         # place button at (0,0)
#         exitButton.place(x=0, y=0)

#     def clickExitButton(self):
#         exit()
        
# root = Tk()
# app = Window(root)
# root.wm_title("Tkinter button")
# root.geometry("320x200")
# root.mainloop()




# from tkinter import *

# def hide_me(event):
#     event.widget.pack_forget()

# root = Tk()
# btn=Button(root, text="Click")
# btn.bind('<Button-1>', hide_me)
# btn.pack()
# btn2=Button(root, text="Click too")
# btn2.bind('<Button-1>', hide_me)
# btn2.pack()
# root.mainloop()




# #Import the required library
# from tkinter import *

# #Create an instance of tkinter frame
# win= Tk()

# #Define the geometry of the window
# win.geometry("650x450")

# #Define function to hide the widget
# def hide_widget(widget):
#    widget.pack_forget()

# #Define a function to show the widget
# def show_widget(widget):
#    widget.pack()

# #Create an Label Widget
# label= Label(win, text= "Showing the Message", font= ('Helvetica bold', 14))
# label.pack(pady=20)

# #Create a button Widget
# button_hide= Button(win, text= "Hide", command= lambda:hide_widget(label))
# button_hide.pack(pady=20)

# button_show= Button(win, text= "Show", command= lambda:show_widget(label))
# button_show.pack()

# win.mainloop()


# from tkinter import *


# root = Tk()
# root.title('Frames')
# root.geometry('500x250+300+300')

# # Position frame
# frame = LabelFrame(root, text='Such a dilemma', padx=25, pady=25)
# frame.pack(padx=10, pady=50)

# # What do the buttons do
# def bad(frame):
#     frame.destroy()
#     frame = LabelFrame(root, text='Such a dilemma', padx=25, pady=25)
#     frame.pack(padx=10, pady=50)
#     slechtekeuze = Label(frame, text='Bad choice')
#     slechtekeuze.grid(row=0, column=0, columnspan=2)

#     # Option to got back
#     homepage = Button(frame, text='Go back', command=lambda:back(frame))
#     homepage.grid(row=1, column=0, columnspan=2, pady=10)

# def good(frame):
#     frame.destroy()
#     frame = LabelFrame(root, text='Such a dilemma', padx=25, pady=25)
#     frame.pack(padx=10, pady=50)
#     slechtekeuze = Label(frame, text='Good choice')
#     slechtekeuze.grid(row=0, column=0, columnspan=2)

#     # Option to go back
#     homepage = Button(frame, text='Terug', command=lambda:back(frame))
#     homepage.grid(row=1, column=0, columnspan=2, pady=10)


# def back(frame):
#     frame.destroy()
#     frame = LabelFrame(root, text='Such a dilemma', padx=25, pady=25)
#     frame.pack(padx=10, pady=50)

#     b = Button(frame, text="Don't click!!!", fg='red', command=lambda:bad(frame))
#     b2 = Button(frame, text='Click!!!', fg='green', command=lambda:good(frame))

#     b.grid(row=0, column=0, padx=3)
#     b2.grid(row=0, column=1, padx=3)

# # Create the buttons and put them in the frame
# b = Button(frame, text="Don't click!!!", fg='red', command=lambda:bad(frame))
# b2 = Button(frame, text='Click!!!', fg='green', command=lambda:good(frame))

# b.grid(row=0, column=0, padx=3)
# b2.grid(row=0, column=1, padx=3)

# root.mainloop()




# import tkinter

# window = tkinter.Tk()
# entry = tkinter.Entry(window)

# def encrypt():
#     encrypt_label = tkinter.Label(window, text="Please enter the message you'd like to encrypt", font=('Helvetica', 14))
#     encrypt_label.pack()
#     entry = tkinter.Entry(window)
#     entry.pack()
#     encrypt_confirm = tkinter.Button(window, text="Confirm")
#     encrypt_confirm.pack()
#     back_button = tkinter.Button(window, text="Back", command=back)
#     back_button.pack()
#     encrypt_button.destroy()
#     title_header.destroy() 
#     title_label.destroy()
#     heading_label.destroy()

# def back():
#     title_header = tkinter.Label(window, text="ENCRYPTION/DECRYPTION", font=('Helvetica', 16))
#     title_header.pack()
#     title_label = tkinter.Label(window, text="Welcome to this encryption and decryption program")
#     title_label.pack()
#     heading_label = tkinter.Label(window, text="When you are ready, press a button to continue")
#     heading_label.pack()
#     encrypt_button = tkinter.Button(window, text="Encrypt", command=encrypt)
#     encrypt_button.pack()
#     encrypt_label.destroy()
#     entry.destroy()
#     encrypt_confirm.destroy()
#     back_button.destroy()

# title_header = tkinter.Label(window, text="ENCRYPTION/DECRYPTION", font=('Helvetica', 16))
# title_header.pack()

# title_label = tkinter.Label(window, text="Welcome to this encryption and decryption program")
# title_label.pack()

# heading_label = tkinter.Label(window, text="When you are ready, press a button to continue")
# heading_label.pack()

# encrypt_button = tkinter.Button(window, text="Encrypt", command=encrypt)
# encrypt_button.pack()

# encrypt_label = tkinter.Label(window, text="Please enter the message you'd like to encrypt", font=('Helvetica', 14))

# entry = tkinter.Entry(window)

# encrypt_confirm = tkinter.Button(window, text="Confirm")

# back_button = tkinter.Button(window, text="Back", command=back)

# window.mainloop()




# try:
#     import tkinter as tk
# except:
#     import tkinter as tk
    
# class SampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self._frame = None
#         self.switch_frame(StartPage)

#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self._frame is not None:
#             self._frame.destroy()
#         self._frame = new_frame
#         self._frame.pack()

# class StartPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go to page one",
#                   command=lambda: master.switch_frame(PageOne)).pack()
#         tk.Button(self, text="Go to page two",
#                   command=lambda: master.switch_frame(PageTwo)).pack()

# class PageOne(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self,bg='blue')
#         tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()

# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self,bg='red')
#         tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()

# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()







# from tkinter import *


# def raise_frame(frame):
#     frame.tkraise()

# root = Tk()

# f1 = Frame(root)
# f2 = Frame(root)
# f3 = Frame(root)
# f4 = Frame(root)

# for frame in (f1, f2, f3, f4):
#     frame.grid(row=0, column=0, sticky='news')

# Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
# Label(f1, text='FRAME 1').pack()

# Label(f2, text='FRAME 2').pack()
# Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

# Label(f3, text='FRAME 3').pack(side='left')
# Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

# Label(f4, text='FRAME 4').pack()
# Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

# raise_frame(f1)
# root.mainloop()



# import tkinter as tk

# def game():
#     window = tk.Toplevel()
#     window.geometry("1280x720")

# root = tk.Tk()
# root.title('testgame')
# root.resizable(False,False)
# root.geometry("500x500")
# pbutton = tk.Button(root, text='Play', width=25, command=game and root.withdraw).place(relx = 0.5,rely = 0.5, anchor = 'center')

# root.mainloop()






# root = tk.Tk()

# #In order to hide main window
# root.withdraw()

# tk.Label(root, text="Main Window").pack()

# aWindow = tk.Toplevel(root)

# def change_window():
#     #remove the other window entirely
#     aWindow.destroy()

#     #make root visible again
#     root.iconify()
#     root.deiconify()

# tk.Button(aWindow, text="This is aWindow", command=change_window).pack()

# root.mainloop()






# from tkinter import *

# def hide(x):
#     x.pack_forget()

# root = Tk() 
# d=Button(root, text="Click to hide me!")

# d.configure(command=lambda: hide(d))
# d.pack()
# root.mainloop()







# import tkinter as tk
    

# def write_slogan():
#     print("Tkinter is easy to use!")

# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# button = tk.Button(frame, 
#                    text="QUIT", 
#                    fg="red",
#                    command=quit)
# button.pack(side=tk.LEFT)
# slogan = tk.Button(frame,
#                    text="Hello",
#                    command=write_slogan)
# slogan.pack(side=tk.LEFT)

# root.mainloop()





# import tkinter as tk

# # --- functions ---

# def select_button():
#     print('value:', v.get())  # selected value

# # --- main ---

# names = ['Button A', 'Button B', 'Button C']

# root = tk.Tk()

# v = tk.IntVar()  # variable for selected value

# for i, name in enumerate(names, 2):
#     btn = tk.Radiobutton(root, text=name, variable=v, value=i)  # assign variable and value

#     btn['indicatoron'] = 0  # display button instead of radiobutton
#     btn['selectcolor'] = 'green' # color after selection

#     btn['command'] = select_button  # function without variables

#     btn.grid(row=i, column=0, sticky='w', ipadx=5, ipady=5)

# root.mainloop()




# import tkinter as tk
# win = tk.Tk()

# def changetext():
# 	a.config(text="changed text!")
    
# a = tk.Label(win, text="hello world")
# a.pack()
# tk.Button(win, text="Change Label Text", command=changetext).pack()

# win.mainloop()





# import tkinter as tk
# import tkinter.messagebox

# def btn_clicked():
#     tkinter.messagebox.showinfo("Login","Login Success, Welcome!")
#     b2 = tk.Button(
#         borderwidth = 0,
#         highlightthickness = 0,
#         command = btn_clicked,
#         relief = "flat"
#     )
#     b2.place(
#         x = 200, y = 200,
#         width = 213,
#         height = 72
#     )

# window = tk.Tk()

# window.geometry("1000x600")
# window.configure(bg = "#293335")

# b1 = tk.Button(
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = btn_clicked,
#     relief = "flat"
# )

# b1.place(
#     x = 5, y = 5,
#     width = 213,
#     height = 72
# )

# window.resizable(False, False)
# window.mainloop()






# import tkinter as tk
# anthem = ['with', 'golden', 'soil', 'and', 'wealth', 'for', 'toil']
# length_of_song = 7
# position = 0
# ROOT = tk.Tk()
# def sing_loop():
#     global position, length_of_song
#     sing['text'] = anthem[position]
#     position = (position + 1) % length_of_song

# sing = tk.Button(text='Press to sing',
#                  command=sing_loop)
# sing.pack(fill='both')
# ROOT.mainloop()







# import tkinter as tk

# class Page(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#     def show(self):
#         self.lift()

# class Page1(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 1")
#        label.pack(side="top", fill="both", expand=True)

# class Page2(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        L=[]
#        for x in ["A","B"]:
#            print(x)
#            L.append(x)
#        label = tk.Label(self, text=L)
#        label.pack(side="top", fill="both", expand=True)


# class Page3(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 3")
#        label.pack(side="top", fill="both", expand=True)

# class MainView(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         p1 = Page1(self)
#         p2 = Page2(self)
#         p3 = Page3(self)

#         buttonframe = tk.Frame(self)
#         container = tk.Frame(self)
#         buttonframe.pack(side="top", fill="x", expand=False)
#         container.pack(side="top", fill="both", expand=True)

#         p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

#         b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
#         b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
#         b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

#         b1.pack(side="left")
#         b2.pack(side="left")
#         b3.pack(side="left")

#         p1.show()

# if __name__ == "__main__":
#     root = tk.Tk()
#     main = MainView(root)
#     main.pack(side="top", fill="both", expand=True)
#     root.wm_geometry("400x400")
#     root.mainloop()