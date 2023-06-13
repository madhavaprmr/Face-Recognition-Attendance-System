from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__ (self, root):
        self.root = root
        self.root.geometry ("1530x790+0+0")
        self.root.title ("Face Recognition System")

        ############### VARIABLES ###############
        self.var_dept = StringVar ()
        self.var_course = StringVar ()
        self.var_year = StringVar ()
        self.var_semester = StringVar ()
        self.var_std_id = StringVar ()
        self.var_std_name = StringVar ()
        self.var_div = StringVar ()
        self.var_roll = StringVar ()
        self.var_gender = StringVar ()
        self.var_dob = StringVar ()
        self.var_email = StringVar ()
        self.var_phone = StringVar ()
        self.var_address = StringVar ()
        self.var_teacher = StringVar ()

        # Background Image
        bg_img = Image.open (r"Images\login.jpg")
        bg_img.resize ((1440, 790), Image.ANTIALIAS)
        self.bg_photoimg = ImageTk.PhotoImage (bg_img)

        bg_lbl = Label (self.root, image = self.bg_photoimg)
        bg_lbl.place (x = 0, y = 0, width = 1440, height = 790)

        # Title Label
        title_lbl = Label (bg_lbl, text = "STUDENT MANAGEMENT SYSTEM", font = ("times new roman", 30, "bold"), bg = "#0a183d", fg = "#0660b1")
        title_lbl.place (x = 0, y = 0, width = 1440, height = 30)

        # Main Label Frame
        main_frame = Frame (bg_lbl, bd = 2, bg = "#0a183d")
        main_frame.place (x = 20, y = 50, width = 1330, height = 650)

        """
        Left Label Frame
        """
        left_frame = LabelFrame (main_frame, bd = 2, bg = "#0a183d", relief = RIDGE, text = "Student Details", font = ("times new roman", 14, "bold"), fg = "#0660b1")
        left_frame.place (x = 10, y = 10, width = 640, height = 600)

        # Current Course
        current_course_frame = LabelFrame (left_frame, bd = 2, bg = "#0a183d", relief = RIDGE, text = "Current Course", font = ("times new roman", 12, "bold"), fg = "white")
        current_course_frame.place(x = 5, y = 5, width = 630, height = 120)

        # Department
        dept_label = Label (current_course_frame, text = "Department", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        dept_label.grid (row = 0, column = 0, padx = 10)

        dept_combo = ttk.Combobox (current_course_frame, textvariable = self.var_dept, font = ("times new roman", 10, "bold"), state = "readonly", width = 20)
        dept_combo["values"] = ("Select Department", "Computer Science", "Mechanical Engineering", "Civil Engineering", "Pharmacology", "Physiotherapy")
        dept_combo.current(0)
        dept_combo.grid (row = 0, column = 1, padx = 2, pady = 10, sticky = W)

        # Course
        course_label = Label (current_course_frame, text = "Course", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        course_label.grid (row = 0, column = 2, padx = 10)
       
        course_combo = ttk.Combobox (current_course_frame, textvariable = self.var_course, font = ("times new roman", 10, "bold"), state = "readonly", width = 20)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid (row = 0, column = 3, padx = 2, pady = 10, sticky = W)
    
        # Year
        year_label = Label (current_course_frame, text = "Year", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        year_label.grid (row = 1, column = 0, padx = 10)
       
        year_combo = ttk.Combobox (current_course_frame, textvariable = self.var_year, font = ("times new roman", 10, "bold"), state = "readonly", width = 20)
        year_combo["values"] = ("Select Year", "2019", "2020", "2021", "2022")
        year_combo.current(0)
        year_combo.grid (row = 1, column = 1, padx = 2, pady = 10, sticky = W)
        
        # Semester
        semester_label = Label (current_course_frame, text = "Semester", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        semester_label.grid (row = 1, column = 2, padx = 10)
       
        semester_combo = ttk.Combobox (current_course_frame, textvariable = self.var_semester, font = ("times new roman", 10, "bold"), state = "readonly", width = 20)
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2")
        semester_combo.current(0)
        semester_combo.grid (row = 1, column = 3, padx = 2, pady = 10, sticky = W)

        # Class Student Information
        class_student_frame = LabelFrame (left_frame, bd = 2, bg = "#0a183d", relief = RIDGE, text = "Class Student Imformation", font = ("times new roman", 12, "bold"), fg = "white")
        class_student_frame.place(x = 5, y = 150, width = 630, height = 400)

        # Student ID        
        studentID_label = Label (class_student_frame, text = "Student ID", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        studentID_label.grid (row = 0, column = 0, padx = 4, pady = 5, sticky = W)
       
        studentID_entry = ttk.Entry (class_student_frame, textvariable = self.var_std_id, width = 20, font = ("times new roman", 13, "bold"))
        studentID_entry.grid (row = 0, column = 1, padx = 4, pady = 6, sticky = W)

        # Student Name        
        studentName_label = Label (class_student_frame, text = "Student Name", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        studentName_label.grid (row = 0, column = 2, padx = 4, pady = 6, sticky = W)
       
        studentName_entry = ttk.Entry (class_student_frame, textvariable = self.var_std_name, width = 20, font = ("times new roman", 13, "bold"))
        studentName_entry.grid (row = 0, column = 3, padx = 4, pady = 6, sticky = W)
        
        # Class Division        
        class_div_label = Label (class_student_frame, text = "Class Division", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        class_div_label.grid (row = 1, column = 0, padx = 4, pady = 6, sticky = W)
       
        # class_div_entry = ttk.Entry (class_student_frame, textvariable = self.var_div, width = 20, font = ("times new roman", 13, "bold"))
        # class_div_entry.grid (row = 1, column = 1, padx = 4, pady = 6, sticky = W)

        div_combo = ttk.Combobox (class_student_frame, textvariable = self.var_div, font = ("times new roman", 10, "bold"), state = "readonly", width = 23)
        div_combo["values"] = ("A", "B", "C")
        div_combo.current(0)
        div_combo.grid (row = 1, column = 1, padx = 4, pady = 6, sticky = W)        

        # Roll No        
        roll_no_label = Label (class_student_frame, text = "Roll No.", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        roll_no_label.grid (row = 1, column = 2, padx = 4, pady = 6, sticky = W)
       
        roll_no_entry = ttk.Entry (class_student_frame, textvariable = self.var_roll, width = 20, font = ("times new roman", 13, "bold"))
        roll_no_entry.grid (row = 1, column = 3, padx = 4, pady = 6, sticky = W)
        
        # Gender        
        gender_label = Label (class_student_frame, text = "Gender", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        gender_label.grid (row = 2, column = 0, padx = 4, pady = 6, sticky = W)
        
        gender_combo = ttk.Combobox (class_student_frame, textvariable = self.var_gender, font = ("times new roman", 10, "bold"), state = "readonly", width = 23)
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid (row = 2, column = 1, padx = 4, pady = 6, sticky = W)        

        # Date of Birth        
        dob_label = Label (class_student_frame, text = "D.O.B.", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        dob_label.grid (row = 2, column = 2, padx = 4, pady = 6, sticky = W)
       
        dob_entry = ttk.Entry (class_student_frame, textvariable = self.var_dob, width = 20, font = ("times new roman", 13, "bold"))
        dob_entry.grid (row = 2, column = 3, padx = 4, pady = 6, sticky = W)
        
        # Email        
        email_label = Label (class_student_frame, text = "Email", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        email_label.grid (row = 3, column = 0, padx = 4, pady = 6, sticky = W)
       
        email_entry = ttk.Entry (class_student_frame, textvariable = self.var_email, width = 20, font = ("times new roman", 13, "bold"))
        email_entry.grid (row = 3, column = 1, padx = 4, pady = 6, sticky = W)

        # Phone No        
        phone_no_label = Label (class_student_frame, text = "Phone No.", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        phone_no_label.grid (row = 3, column = 2, padx = 4, pady = 6, sticky = W)
       
        phone_no_entry = ttk.Entry (class_student_frame, textvariable = self.var_phone, width = 20, font = ("times new roman", 13, "bold"))
        phone_no_entry.grid (row = 3, column = 3, padx = 4, pady = 6, sticky = W)

        # Address        
        address_label = Label (class_student_frame, text = "Address", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        address_label.grid (row = 4, column = 0, padx = 4, pady = 6, sticky = W)
       
        address_entry = ttk.Entry (class_student_frame, textvariable = self.var_address, width = 20, font = ("times new roman", 13, "bold"))
        address_entry.grid (row = 4, column = 1, padx = 4, pady = 6, sticky = W)

        # Teacher's Name        
        teacher_label = Label (class_student_frame, text = "Teacher's Name", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        teacher_label.grid (row = 4, column = 2, padx = 4, pady = 6, sticky = W)
       
        teacher_entry = ttk.Entry (class_student_frame, textvariable = self.var_teacher, width = 20, font = ("times new roman", 13, "bold"))
        teacher_entry.grid (row = 4, column = 3, padx = 4, pady = 6, sticky = W)

        # Radio Buttons
        self.var_radio1 = StringVar ()
        radio_btn1 = ttk.Radiobutton (class_student_frame, variable = self.var_radio1, text = "Take Photo Sample", value = "Yes")
        radio_btn1.grid (row = 6, column = 1, padx = 4, pady = 20)
        
        radio_btn2 = ttk.Radiobutton (class_student_frame, variable = self.var_radio1, text = "No Photo Sample", value = "No")
        radio_btn2.grid (row = 6, column = 2, padx = 4, pady = 20)
        
        # Buttons Frame
        btn_frame = Frame (class_student_frame, bd = 2, relief = RIDGE, bg = "white")
        btn_frame.place (x = 2.5, y = 250, width = 620, height = 37)

        save_btn = Button (btn_frame, command = self.add_data, text = "Save",width = 16, font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        save_btn.grid(row = 0, column = 0)

        update_btn = Button (btn_frame, command = self.update_data, text = "Update",width = 16, font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        update_btn.grid(row = 0, column = 1)

        delete_btn = Button (btn_frame, command = self.delete_data, text = "Delete",width = 16, font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        delete_btn.grid(row = 0, column = 2)
        
        reset_btn = Button (btn_frame, command = self.reset_data, text = "Reset",width = 16, font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        reset_btn.grid(row = 0, column = 3)

        # Buttons Frame
        btn_frame1 = Frame (class_student_frame, bd = 2, relief = RIDGE, bg = "white")
        btn_frame1.place (x = 3, y = 300, width = 619, height = 37)

        take_photo_btn = Button (btn_frame1,command = self.generate_dataset, text = "Take Photo Sample",width = 33, font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        take_photo_btn.grid(row = 0, column = 0)

        update_photo_btn = Button (btn_frame1, text = "Update Photo Sample",width = 33, font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        update_photo_btn.grid(row = 0, column = 1)

        
        """
        Right Label Frame
        """
        right_frame = LabelFrame (main_frame, bd = 2, bg = "#0a183d", relief = RIDGE, text = "Student Details", font = ("times new roman", 14, "bold"), fg = "#0660b1")
        right_frame.place (x = 676, y = 10, width = 640, height = 600)

        # Search System
        search_frame = LabelFrame (right_frame, bd = 2, bg = "#0a183d", relief = RIDGE, text = "Search System", font = ("times new roman", 12, "bold"), fg = "white")
        search_frame.place(x = 5, y = 5, width = 630, height = 120)

        search_label = Label (search_frame, text = "Search By", font = ("times new roman", 12, "bold"), bg = "#0a183d", fg = "#2596be")
        search_label.grid (row = 0, column = 0, padx = 4, pady = 6, sticky = W)

        search_combo = ttk.Combobox (search_frame, font = ("times new roman", 10, "bold"), state = "readonly", width = 17)
        search_combo["values"] = ("Select", "Roll No.", "Phone No.")
        search_combo.current(0)
        search_combo.grid (row = 0, column = 1, padx = 2, pady = 10, sticky = W)

        search_entry = ttk.Entry (search_frame, width = 20, font = ("times new roman", 13, "bold"))
        search_entry.grid (row = 0, column = 2, padx = 4, pady = 6, sticky = W)

        search_btn = Button (search_frame, text = "Search",width = 12, font = ("times new roman", 10, "bold"), bg = "#0a183d", fg = "#2596be")
        search_btn.grid(row = 0, column = 3, padx = 2, pady = 10, sticky = W)
        
        showAll_btn = Button (search_frame, text = "Show All",width = 12, font = ("times new roman", 10, "bold"), bg = "#0a183d", fg = "#2596be")
        showAll_btn.grid(row = 0, column = 4, padx = 2, pady = 10, sticky = W)

        # Table Frame
        table_frame = Frame (right_frame, bd = 2, bg = "#0a183d", relief = RIDGE)
        table_frame.place (x = 5, y = 150, width = 630, height = 400)
        
        scroll_x = ttk.Scrollbar (table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar (table_frame, orient = VERTICAL)

        self.student_table = ttk.Treeview (table_frame, column = ("dept", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack (side = BOTTOM, fill = X)
        scroll_y.pack (side = RIGHT, fill = Y)
        scroll_x.config (command = self.student_table.xview)
        scroll_y.config (command = self.student_table.yview)

        self.student_table.heading ("dept", text = "Department")
        self.student_table.heading ("course", text = "Course")
        self.student_table.heading ("year", text = "Year")
        self.student_table.heading ("sem", text = "Semester")
        self.student_table.heading ("id", text = "StudentID")
        self.student_table.heading ("name", text = "Name")
        self.student_table.heading ("div", text = "Division")
        self.student_table.heading ("roll", text = "Roll No.")
        self.student_table.heading ("gender", text = "Gender")
        self.student_table.heading ("dob", text = "DOB")
        self.student_table.heading ("email", text = "Email")
        self.student_table.heading ("phone", text = "Phone")
        self.student_table.heading ("address", text = "Address")
        self.student_table.heading ("teacher", text = "Teacher")
        self.student_table.heading ("photo", text = "photo")
        self.student_table["show"] = "headings"

        self.student_table.column ("dept", width = 110)
        self.student_table.column ("course", width = 100)
        self.student_table.column ("year", width = 100)
        self.student_table.column ("sem", width = 100)
        self.student_table.column ("id", width = 100)
        self.student_table.column ("name", width = 100)
        self.student_table.column ("div", width = 100)
        self.student_table.column ("roll", width = 100)
        self.student_table.column ("gender", width = 100)
        self.student_table.column ("dob", width = 100)
        self.student_table.column ("email", width = 130)
        self.student_table.column ("phone", width = 100)
        self.student_table.column ("address", width = 100)
        self.student_table.column ("teacher", width = 100)
        self.student_table.column ("photo", width = 100)

        self.student_table.pack (fill = BOTH, expand = 1)
        self.student_table.bind ("<ButtonRelease>", self.get_cursor)
        self.fetch_data ()

    ############## FUNCTION DECLARATION ################### 
    def add_data (self):
        if self.var_dept.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror ("Error", "All fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "face_recognizer", auth_plugin = "mysql_native_password")
                my_cursor = conn.cursor ()
                my_cursor.execute ("insert into student values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                                                self.var_dept.get(),
                                                                                                                                self.var_course.get(),
                                                                                                                                self.var_year.get(),
                                                                                                                                self.var_semester.get(),
                                                                                                                                self.var_std_id.get(),
                                                                                                                                self.var_std_name.get(),
                                                                                                                                self.var_div.get(),
                                                                                                                                self.var_roll.get(),
                                                                                                                                self.var_gender.get(),
                                                                                                                                self.var_dob.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_phone.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_teacher.get(),
                                                                                                                                self.var_radio1.get()
                                                                                                                            ))
                conn.commit ()
                self.fetch_data ()
                conn.close ()
                messagebox.showinfo("Success", "Student details has been added successfully", parent = self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)


    ########### FETCH DATA ############## 
    def fetch_data (self):
        conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "face_recognizer", auth_plugin = "mysql_native_password")
        my_cursor = conn.cursor ()

        my_cursor.execute ("select * from student")

        data = my_cursor.fetchall ()

        if len (data) != 0:
            self.student_table.delete (*self.student_table.get_children ())
            for i in data:
                self.student_table.insert ("", END, values = i)
            conn.commit ()
        conn.close ()


    ############## GET CURSOR #################
    def get_cursor (self, event = ""):
        cursor_focus = self.student_table.focus ()
        content = self.student_table.item (cursor_focus)
        data = content ["values"]

        self.var_dept.set (data[0])
        self.var_course.set (data[1])     
        self.var_year.set (data[2])     
        self.var_semester.set (data[3])     
        self.var_std_id.set (data[4])     
        self.var_std_name.set (data[5])     
        self.var_div.set (data[6])     
        self.var_roll.set (data[7])     
        self.var_gender.set (data[8])     
        self.var_dob.set (data[9])     
        self.var_email.set (data[10])     
        self.var_phone.set (data[11])     
        self.var_address.set (data[12])     
        self.var_teacher.set (data[13])     
        self.var_radio1.set (data[14])     

    ############## UPDATE DATA #################### 
    def update_data (self):
        if self.var_dept.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror ("Error", "All fields are required", parent = self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update the student details?", parent = self.root)
                if update > 0:
                    conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "face_recognizer", auth_plugin = "mysql_native_password")
                    my_cursor = conn.cursor ()

                    my_cursor.execute ("update student set Dept = %s, Course = %s, Year = %s, Semester = %s, Division = %s, Roll = %s, Gender = %s, DOB = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s, PhotoSample = %s where Student_ID = %s", (
                                                                                                                                                                                                                                                                self.var_dept.get(),
                                                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                                                self.var_std_id.get()
                                                                                                                                                                                                                                                            ))     
                               
                    conn.commit ()
                    self.fetch_data ()
                    conn.close ()
                    messagebox.showinfo ("Success", "Student details successfully updated.", parent = self.root)
                else:
                    if not update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)


    ############################## DELETE DATA ############################
    def delete_data (self):
        if self.var_std_id.get () == "":
            messagebox.showerror ("Error", "Student ID is required.", parent = self.root)
        else: 
            try:
                delete = messagebox.askyesno ("Student delete page", "Do you want to delete this student?", parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "face_recognizer", auth_plugin = "mysql_native_password")
                    my_cursor = conn.cursor ()

                    sql = "delete from student where Student_ID = %s"
                    val = (self.var_std_id.get (),)

                    my_cursor.execute (sql, val)
                else:
                    if not delete:
                        return
                    
                conn.commit ()
                self.fetch_data ()
                conn.close ()
                messagebox.showinfo ("Delete", "Successfully deleted student details.", parent = self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)

    #########################################################
    ##################### RESET DATA ########################
    #########################################################

    def reset_data (self):
        self.var_dept.set ("Select Department")
        self.var_course.set ("Select Course")     
        self.var_year.set ("Select Year")     
        self.var_semester.set ("Select Semester")     
        self.var_std_id.set ("")     
        self.var_std_name.set ("")     
        self.var_div.set ("Select Division")     
        self.var_roll.set ("")     
        self.var_gender.set ("Male")     
        self.var_dob.set ("")     
        self.var_email.set ("")     
        self.var_phone.set ("")     
        self.var_address.set ("")     
        self.var_teacher.set ("")     
        self.var_radio1.set ("")     

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    ############################## Generate Dataset or Take Photo Sample ######################################
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def generate_dataset (self):
        if self.var_dept.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror ("Error", "All fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "face_recognizer", auth_plugin = "mysql_native_password")
                my_cursor = conn.cursor ()
                my_cursor.execute ("select * from student")
                myresult = my_cursor.fetchall ()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute ("update student set Dept = %s, Course = %s, Year = %s, Semester = %s, Division = %s, Roll = %s, Gender = %s, DOB = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s, PhotoSample = %s where Student_ID = %s", (
                                                                                                                                                                                                                                                            self.var_dept.get(),
                                                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                                            self.var_std_id.get() == id + 1
                                                                                                                                                                                                                                                        ))
                conn.commit ()
                self.fetch_data ()
                self.reset_data ()
                conn.close ()

                """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                ############# LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV ###################
                """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                
                face_classifier = cv2.CascadeClassifier ("haarcascade_frontalface_default.xml")

                def face_cropped (img):
                    gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale (gray, 1.3, 5)
                    # SCALING FACTOR = 1.3
                    # MINIMUM NEIGHBOR = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img [y: y + h, x: x + w]
                        return face_cropped
                
                cap = cv2.VideoCapture (0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read ()
                    if face_cropped (my_frame) is not None:
                        img_id += 1
                        face = cv2.resize (face_cropped (my_frame), (450, 450))
                        face = cv2.cvtColor (face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str (id) + "." + str (img_id) + ".jpg"
                        cv2.imwrite (file_name_path, face)
                        cv2.putText (face, str (img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow ("Cropped face", face)

                    if cv2.waitKey(1) == 13 or int (img_id) == 100:
                        break
                cap.release ()
                cv2.destroyAllWindows ()
                messagebox.showinfo ("Result", "Dataset generated successfully")
            
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)



if __name__ == "__main__":
    root = Tk ()
    obj = Student (root)
    root.mainloop ()
    