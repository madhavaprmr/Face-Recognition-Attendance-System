import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition
from about import About

class Face_Recognition_System:
    def __init__ (self, root):
        self.root = root
        self.root.geometry ("1530x790+0+0")
        self.root.title ("Face Recognition System")

        # Background Image
        bg_img = Image.open (r"Images\login.jpg")
        bg_img.resize ((1440, 790), Image.ANTIALIAS)
        self.bg_photoimg = ImageTk.PhotoImage (bg_img)

        bg_lbl = Label (self.root, image = self.bg_photoimg)
        bg_lbl.place (x = 0, y = 0, width = 1440, height = 790)

        # Title Label
        title_lbl = Label (bg_lbl, text = "FACE RECOGNITION ATTENDENCE SYSTEM", font = ("times new roman", 30, "bold"), bg = "#0a183d", fg = "#0660b1")
        title_lbl.place (x = 0, y = 0, width = 1440, height = 30)

        # Student Button
        s_img = Image.open (r"Images\student_logo.jpg")
        s_img.resize ((220, 220), Image.ANTIALIAS)
        self.s_photoimg = ImageTk.PhotoImage (s_img)

        s_b = Button (bg_lbl, image = self.s_photoimg, command = self.student_details, cursor = "hand2")
        s_b.place (x = 443, y = 200, width = 170, height = 170)

        s_b1 = Button (bg_lbl, text = "Student Details", command = self.student_details, cursor = "hand2", font = ("times new roman", 15, "bold"), bg = "#0a183d", fg = "#0660b1")
        s_b1.place (x = 443, y = 350, width = 170, height = 20)

        # Face Detector Button
        d_img = Image.open (r"Images\face_detector.jpg")
        d_img.resize ((220, 220), Image.ANTIALIAS)
        self.d_photoimg = ImageTk.PhotoImage (d_img)

        d_b = Button (bg_lbl,command = self.face_recognition, image = self.d_photoimg, cursor = "hand2")
        d_b.place (x = 633, y = 200, width = 170, height = 170)

        d_b1 = Button (bg_lbl,command = self.face_recognition, text = "Face Detector", cursor = "hand2", font = ("times new roman", 15, "bold"), bg = "#0a183d", fg = "#0660b1")
        d_b1.place (x = 633, y = 350, width = 170, height = 20)

        # Attendence Button
        a_img = Image.open (r"Images\attendance.jpg")
        a_img.resize ((220, 220), Image.ANTIALIAS)
        self.a_photoimg = ImageTk.PhotoImage (a_img)

        a_b = Button (bg_lbl,command = self.attendance, image = self.a_photoimg, cursor = "hand2")
        a_b.place (x = 823, y = 200, width = 170, height = 170)

        a_b1 = Button (bg_lbl,command = self.attendance, text = "Attendance", cursor = "hand2", font = ("times new roman", 15, "bold"), bg = "#0a183d", fg = "#0660b1")
        a_b1.place (x = 823, y = 350, width = 170, height = 20)
        
        # Train Data Button
        t_img = Image.open (r"Images\train_data.jpg")
        t_img.resize ((220, 220), Image.ANTIALIAS)
        self.t_photoimg = ImageTk.PhotoImage (t_img)

        t_b = Button (bg_lbl, command = self.train_data, image = self.t_photoimg, cursor = "hand2")
        t_b.place (x = 443, y = 420, width = 170, height = 170)

        t_b1 = Button (bg_lbl, command = self.train_data, text = "Train Data", cursor = "hand2", font = ("times new roman", 15, "bold"), bg = "#0a183d", fg = "#0660b1")
        t_b1.place (x = 443, y = 570, width = 170, height = 20)

        # Photos Button
        p_img = Image.open (r"Images\photos.jpg")
        p_img.resize ((220, 220), Image.ANTIALIAS)
        self.p_photoimg = ImageTk.PhotoImage (p_img)

        p_b = Button (bg_lbl,command = self.open_img, image = self.p_photoimg, cursor = "hand2")
        p_b.place (x = 633, y = 420, width = 170, height = 170)

        p_b1 = Button (bg_lbl,command = self.open_img, text = "Photos", cursor = "hand2", font = ("times new roman", 15, "bold"), bg = "#0a183d", fg = "#0660b1")
        p_b1.place (x = 633, y = 570, width = 170, height = 20)

        # About Button
        h_img = Image.open (r"Images\help.jpg")
        h_img.resize ((220, 220), Image.ANTIALIAS)
        self.h_photoimg = ImageTk.PhotoImage (h_img)

        h_b = Button (bg_lbl,command = self.about, image = self.h_photoimg, cursor = "hand2")
        h_b.place (x = 823, y = 420, width = 170, height = 170)

        h_b1 = Button (bg_lbl,command = self.about, text = "About", cursor = "hand2", font = ("times new roman", 15, "bold"), bg = "#0a183d", fg = "#0660b1")
        h_b1.place (x = 823, y = 570, width = 170, height = 20)
        
    def open_img (self):
        os.startfile ("data")

    ########### FUNCTION BUTTONS ############
    def student_details (self):
        self.new_window = Toplevel (self.root)
        self.app = Student (self.new_window)

    def train_data (self):
        self.new_window = Toplevel (self.root)
        self.app = Train (self.new_window)

    def face_recognition (self):
        self.new_window = Toplevel (self.root)
        self.app = Face_Recognition (self.new_window)

    def attendance (self):
        self.new_window = Toplevel (self.root)
        self.app = Attendance (self.new_window)

    def about (self):
        self.new_window = Toplevel (self.root)
        self.app = About (self.new_window)


if __name__ == "__main__":
    root = Tk ()
    obj = Face_Recognition_System (root)
    root.mainloop ()
    
