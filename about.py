import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class About:
    def __init__ (self, root):
        self.root = root
        self.root.geometry ("1530x790+0+0")
        self.root.title ("Face Recognition System")

        # Background Image
        bg_img = Image.open (r"Images\about_main.jpg")
        bg_img.resize ((1440, 790), Image.ANTIALIAS)
        self.bg_photoimg = ImageTk.PhotoImage (bg_img)

        bg_lbl = Label (self.root, image = self.bg_photoimg)
        bg_lbl.place (x = 0, y = 0, width = 1440, height = 790)


if __name__ == "__main__":
    root = Tk ()
    obj = About (root)
    root.mainloop ()
    
