import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition
from about import About

def main ():
  win = Tk ()
  app = Login_Window (win)
  win.mainloop ()

class Login_Window:
  def __init__ (self, root):
    self.root = root
    self.root.title ("Login")
    self.root.geometry ("1530x790+0+0")

    self.bg = ImageTk.PhotoImage (file = r"Images\background.jpg")
    bg_lbl = Label (self.root, image = self.bg)
    bg_lbl.place (x = 0, y = 0, relwidth = 1, relheight = 1)
    
    frame = Frame (self.root, bg = "#1e243a")
    frame.place (x = 800, y = 170, width = 370, height = 450)

    get_str = Label (frame, text = "Get started", font = ("times new roman", 20, "bold"), fg = "#114c90", bg = "#1e243a")
    get_str.place (x = 115, y = 30)

    # Label
    username = Label (frame, text = "Username", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    username.place (x = 40, y = 80)

    self.txtuser = ttk.Entry (frame, font = ("times new roman", 15, "bold"))
    self.txtuser.place (x = 40, y = 120, width = 270)

    password = Label (frame, text = "Password", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    password.place (x = 40, y = 160)

    self.txtpass = ttk.Entry (frame, font = ("times new roman", 15, "bold"))
    self.txtpass.place (x = 40, y = 200, width = 270)
    
    # Login Button
    loginbtn = Button (frame, command = self.login, text = "Login", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1", activebackground =  "#114c90", activeforeground = "#1e243a")
    loginbtn.place (x = 110, y = 260, width = 135, height = 35)
    
    # Register Button
    registerbtn = Button (frame, command = self.register_window, text = "Create new account", font = ("times new roman", 10), borderwidth = 0, bg = "#1e243a", fg = "#0660b1", activebackground =  "#1e243a", activeforeground = "#1e243a")
    registerbtn.place (x = 40, y = 340, width = 135)
    
    # Forgot Passoword Button
    fpassbtn = Button (frame, command = self.forgot_password_window, text = "Forgot Password", font = ("times new roman", 10), borderwidth = 0, bg = "#1e243a", fg = "#0660b1", activebackground =  "#1e243a", activeforeground = "#1e243a")
    fpassbtn.place (x = 35, y = 360, width = 135)

  def register_window (self):
    self.new_window = Toplevel (self.root)
    self.app = Register (self.new_window)

  def login (self):
    if self.txtuser.get () == "" or self.txtpass.get () == "":
      messagebox.showerror ("Error", "All fields are required!")
    elif self.txtuser.get () == "kapu" and self.txtpass.get () == "ashu":
      messagebox.showinfo ("Success", "Welcome to face recognition attendance system!")
    else:
      conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "user", auth_plugin = "mysql_native_password")
      my_cursor = conn.cursor ()
      my_cursor.execute ("select * from register where email = %s and password = %s", (
                                                                                          self.txtuser.get (),
                                                                                          self.txtpass.get ()
                                                                                      ))   
      row = my_cursor.fetchone ()
      if row == None:
        messagebox.showerror ("Error", "Invalid username or password!")
      else:
        open_main = messagebox.askyesno ("Yes or No", "Do you wish to continue?")
        if open_main > 0:
          self.new_window = Toplevel (self.root)
          self.app = Face_Recognition_System (self.new_window)
        else:
          if not open_main:
            return
        conn.commit ()
        conn.close ()
        
  ######################################  RESET PASSWORD  #######################################
  def reset_pass (self):
    if self.combo_security_Q.get () == "Select":
      messagebox.showerror ("Error", "Select security question!", parent = self.root2)
    elif self.txt_security.get () == "":
      messagebox.showerror ("Error", "Please, enter the security answer!", parent = self.root2)
    elif self.txt_newpass.get () == "":
      messagebox.showerror ("Error", "Please, enter the new password!", parent = self.root2)
    else:
      conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "user", auth_plugin = "mysql_native_password")
      my_cursor = conn.cursor ()
  
      query = ("select * from register where email = %s and securityQ = %s and securityA = %s")
      value = (self.txtuser.get (), self.combo_security_Q.get (), self.txt_security.get ())
  
      my_cursor.execute (query, value)
      row = my_cursor.fetchone ()
  
      if row == None:
        messagebox.showerror ("Error", "Please, enter the correct answer!", parent = self.root2)
      else:
        query1 = ("update register set password = %s where email = %s")
        value1 = (self.txt_newpass.get (), self.txtuser.get ())
        my_cursor.execute (query1, value1)

        conn.commit ()
        conn.close ()
        messagebox.showinfo ("Success", "Your password has been reset, please login with new password", parent = self.root2)
        self.root2.destroy ()

  ######################################  FORGOT PASSWORD #######################################
  def forgot_password_window (self):
    if self.txtuser.get () == "":
      messagebox.showerror ("Error", "Please enter your email address")
    else:
      conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "user", auth_plugin = "mysql_native_password")
      my_cursor = conn.cursor ()
      query = ("select * from register where email = %s")
      value = (self.txtuser.get (),)
      my_cursor.execute(query, value)
      row = my_cursor.fetchone ()

      if row == None:
        messagebox.showerror ("Error", "Please enter the valid username!")
      else:
        conn.close ()
        self.root2 = Toplevel ()
        self.root2.geometry ("350x400+600+150")
        
        # Background Image
        bg_img = Image.open (r"Images\forgot_password.jpg")
        bg_img.resize ((350, 400), Image.ANTIALIAS)
        self.bg_photoimg = ImageTk.PhotoImage (bg_img)

        bg_lbl = Label (self.root2, image = self.bg_photoimg)
        bg_lbl.place (x = 0, y = 0, width = 350, height = 450)

        l = Label (bg_lbl, text = "Forgot Password", font = ("times new roman", 15, "bold"), bg = "#1c2c4c", fg = "#0660b1", width = 358)
        l.place (x = 0, y = 0, relwidth = 1)
        
        # Select Security Questions
        security_Q = Label (self.root2, text = "Select Security Question", font = ("times new roman", 15, "bold"), bg = "#1c2c4c", fg = "#0660b1")
        security_Q.place (x = 40, y = 40)

        self.combo_security_Q = ttk.Combobox (self.root2, font = ("times new roman", 10, "bold"), state = "readonly", width = 23)
        self.combo_security_Q["values"] = ("Select", "What is your birth place?", "What is your first pet's name?", "What is your favorite book?", "What is the name of your best friend?")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place (x = 40, y = 80, width = 200)
  
        # Security Answer
        security_A = Label (self.root2, text = "Security Answer", font = ("times new roman", 15, "bold"), bg = "#1c2c4c", fg = "#0660b1")
        security_A.place (x = 40, y = 120)

        self.txt_security = ttk.Entry (self.root2, font = ("times new roman", 15, "bold"))
        self.txt_security.place (x = 40, y = 160, width = 200)
        
        # New Password
        new_password = Label (self.root2, text = "New Password", font = ("times new roman", 15, "bold"), bg = "#1c2c4c", fg = "#0660b1")
        new_password.place (x = 40, y = 200)

        self.txt_newpass = ttk.Entry (self.root2, font = ("times new roman", 15, "bold"))
        self.txt_newpass.place (x = 40, y = 240, width = 200)

        btn = Button (self.root2, command = self.reset_pass, text = "Reset", font = ("times new roman", 15, "bold"), bg = "#1c2c4c", fg = "#0660b1", activebackground =  "#0660b1", activeforeground = "#1c2c4c")
        btn.place (x = 85, y = 290, width = 100, height = 30)
              
          
class Register:
  def __init__ (self, root):
    self.root = root
    self.root.title ("Login")
    self.root.geometry ("1530x790+0+0")

    ############ TEXT VARIABLE ################
    self.var_fname = StringVar ()
    self.var_lname = StringVar ()
    self.var_contact = StringVar ()
    self.var_email = StringVar ()
    self.var_securityQ = StringVar ()
    self.var_securityA = StringVar ()
    self.var_pass = StringVar ()
    self.var_confpass = StringVar ()

    ########### BACKGROUND IMAGE ##############
    self.bg = ImageTk.PhotoImage (file = r"Images\background.jpg")
    bg_lbl = Label (self.root, image = self.bg)
    bg_lbl.place (x = 0, y = 0, relwidth = 1, relheight = 1)
    
    frame = Frame (self.root, bg = "#1e243a")
    frame.place (x = 700, y = 170, width = 550, height = 520)

    register_lbl = Label (frame, text = "Register Here", font = ("times new roman", 20, "bold"), fg = "#114c90", bg = "#1e243a")
    register_lbl.place (x = 180, y = 30)

    # Label
    # First Name
    fname = Label (frame, text = "First Name", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    fname.place (x = 40, y = 80)

    fname_entry = ttk.Entry (frame, textvariable = self.var_fname, font = ("times new roman", 15, "bold"))
    fname_entry.place (x = 40, y = 120, width = 200)
    
    # Last Name
    lname = Label (frame, text = "Last Name", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    lname.place (x = 300, y = 80)

    lname_entry = ttk.Entry (frame, textvariable = self.var_lname, font = ("times new roman", 15, "bold"))
    lname_entry.place (x = 300, y = 120, width = 200)
    
    # Contact Number
    contact = Label (frame, text = "Contact", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    contact.place (x = 40, y = 160)

    self.txt_contact = ttk.Entry (frame, textvariable = self.var_contact, font = ("times new roman", 15, "bold"))
    self.txt_contact.place (x = 40, y = 200, width = 200)
    
    # Email
    email = Label (frame, text = "Email", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    email.place (x = 300, y = 160)

    self.txt_email = ttk.Entry (frame, textvariable = self.var_email, font = ("times new roman", 15, "bold"))
    self.txt_email.place (x = 300, y = 200, width = 200)
    
    # Select Security Questions
    security_Q = Label (frame, text = "Select Security Question", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    security_Q.place (x = 40, y = 240)

    # security_Q = ttk.Entry (frame, font = ("times new roman", 15, "bold"))
    # security_Q.place (x = 40, y = 280, width = 200)
    security_Q_combo = ttk.Combobox (frame, textvariable = self.var_securityQ, font = ("times new roman", 10, "bold"), state = "readonly", width = 23)
    security_Q_combo["values"] = ("Select", "What is your birth place?", "What is your first pet's name?", "What is your favorite book?", "What is the name of your best friend?")
    security_Q_combo.current(0)
    security_Q_combo.place (x = 40, y = 280, width = 200)

    # Security Answer
    security_A = Label (frame, text = "Security Answer", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    security_A.place (x = 300, y = 240)

    self.txt_security = ttk.Entry (frame, textvariable = self.var_securityA, font = ("times new roman", 15, "bold"))
    self.txt_security.place (x = 300, y = 280, width = 200)
    
    # Password
    password = Label (frame, text = "Password", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    password.place (x = 40, y = 320)

    self.txt_password = ttk.Entry (frame,textvariable = self.var_pass, font = ("times new roman", 15, "bold"))
    self.txt_password.place (x = 40, y = 360, width = 200)
    
    # Confirm Password
    lname = Label (frame, text = "Confirm Password", font = ("times new roman", 15, "bold"), bg = "#1e243a", fg = "#0660b1")
    lname.place (x = 300, y = 320)

    lname_entry = ttk.Entry (frame, textvariable = self.var_confpass, font = ("times new roman", 15, "bold"))
    lname_entry.place (x = 300, y = 360, width = 200)

    # Terms and conditions
    self.var_check = IntVar ()
    checkbtn = Checkbutton(frame, variable = self.var_check, text = " I agree to the Terms and Conditions", font = ("times new roman", 10), onvalue = 1, offvalue = 0)
    checkbtn.place (x = 40, y = 420)

    # Button
    registerbtn = Button (frame, command = self.register_data, text = "Register", font = ("times new roman", 10, "bold"), bg = "#1e243a", fg = "#0660b1", activebackground =  "#114c90", activeforeground = "#1e243a")
    registerbtn.place (x = 80, y = 480, width = 120, height = 30)

    loginbtn = Button (frame, command = self.return_login, text = "Login", font = ("times new roman", 10, "bold"), bg = "#1e243a", fg = "#0660b1", activebackground =  "#114c90", activeforeground = "#1e243a")
    loginbtn.place (x = 320, y = 480, width = 120, height = 30)

  ############# FUNCTION DECLARATION ############
  def register_data (self):
    if self.var_fname.get () == "" or self.var_email.get () == "" or self.var_securityQ.get () == "":
      messagebox.showerror ("Error", "All fields are required!")
    elif self.var_pass.get () != self.var_confpass.get ():
      messagebox.showerror ("Error", "Password do not match with confirm password!")
    elif self.var_check.get () == 0:
      messagebox.showerror ("Error", "Please agree to Terms and Conditions!")
    else:
      messagebox.showinfo ("Success", "Welcome to Face Recognition Attendance System")
      conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "user", auth_plugin = "mysql_native_password")
      my_cursor = conn.cursor ()
      query= ("select * from register where email = %s")
      value = (self.var_email.get (), )
      my_cursor.execute (query, value)
      row = my_cursor.fetchone ()
      if row != None:
        messagebox.showerror("Error", "User already exists, please try another email.")
      else:
        my_cursor.execute ("insert into register values (%s, %s, %s, %s, %s, %s, %s)", (
                                                                                          self.var_fname.get (),
                                                                                          self.var_lname.get (),
                                                                                          self.var_contact.get (),
                                                                                          self.var_email.get (),
                                                                                          self.var_securityQ.get (),
                                                                                          self.var_securityA.get (),
                                                                                          self.var_pass.get ()
                                                                                       ))
        conn.commit ()
        conn.close ()
        messagebox.showinfo ("Success", "Successfully registered.")

  def return_login (self):
    self.root.destroy ()



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
  main ()