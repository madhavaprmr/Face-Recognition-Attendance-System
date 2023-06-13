from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

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
    # Gender        
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

    loginbtn = Button (frame, text = "Login", font = ("times new roman", 10, "bold"), bg = "#1e243a", fg = "#0660b1", activebackground =  "#114c90", activeforeground = "#1e243a")
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

if __name__ == "__main__":
  root = Tk ()
  app = Register (root)
  root.mainloop ()
