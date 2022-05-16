from tkinter import *

root = Tk()

text = Text(root)




# adding a tag to a part of text specifying the indices
text.tag_add("start", "1.8", "1.13")
text.tag_config("start", background="white", foreground="yellow")

root.mainloop()