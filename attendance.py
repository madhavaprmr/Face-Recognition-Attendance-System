from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__ (self, root):
        self.root = root
        self.root.geometry ("1530x790+0+0")
        self.root.title ("Face Recognition System")

        ################## VARIABLES ##################
        self.var_atten_id = StringVar ()
        self.var_atten_roll = StringVar ()
        self.var_atten_name = StringVar ()
        self.var_atten_dept = StringVar ()
        self.var_atten_time = StringVar ()
        self.var_atten_date = StringVar ()
        self.var_atten_attendance = StringVar ()

        # Background Image
        bg_img = Image.open (r"Images\login.jpg")
        bg_img.resize ((1440, 790), Image.ANTIALIAS)
        self.bg_photoimg = ImageTk.PhotoImage (bg_img)

        bg_lbl = Label (self.root, image = self.bg_photoimg)
        bg_lbl.place (x = 0, y = 0, width = 1440, height = 790)

        # Title Label
        title_lbl = Label (bg_lbl, text = "ATTENDANCE MANAGEMENT SYSTEM", font = ("times new roman", 30, "bold"), bg = "#0a183d", fg = "#0660b1")
        title_lbl.place (x = 0, y = 0, width = 1440, height = 30)

        # Main Label Frame
        main_frame = Frame (bg_lbl, bd = 2, bg = "#0a183d")
        main_frame.place (x = 130, y = 80, width = 1120, height = 610)

        """
        Left Label Frame
        """
        left_frame = LabelFrame (main_frame, bd = 2, bg = "#0a183d", relief = RIDGE, text = "Student Attendance Details", font = ("times new roman", 14, "bold"), fg = "#0660b1")
        left_frame.place (x = 10, y = 10, width = 545, height = 585)

        left_inside_frame = Frame (left_frame, bd = 2, relief = RIDGE, bg = "#0a183d")
        left_inside_frame.place (x = 5, y = 5, width = 530, height = 545)

        """ LABEL AND ENTRY """
        # Attendance ID        
        attendanceID_label = Label (left_inside_frame, text = "Attendance ID", font = ("times new roman", 13, "bold"), bg = "#0a183d", fg = "#2596be")
        attendanceID_label.grid (row = 0, column = 0, padx = 10, pady = 17, sticky = W)
       
        attendanceID_entry = ttk.Entry (left_inside_frame,textvariable = self.var_atten_id, width = 25, font = ("times new roman", 13, "bold"))
        attendanceID_entry.grid (row = 0, column = 1, padx = 10, pady = 17, sticky = W)

        # Roll No        
        roll_label = Label (left_inside_frame, text = "Roll No.", font = ("times new roman", 13, "bold"), bg = "#0a183d", fg = "#2596be")
        roll_label.grid (row = 1, column = 0, padx = 10, pady = 17, sticky = W)
       
        roll_entry = ttk.Entry (left_inside_frame, textvariable = self.var_atten_roll, width = 25, font = ("times new roman", 13, "bold"))
        roll_entry.grid (row = 1, column = 1, padx = 10, pady = 17, sticky = W)

        # Name        
        name_label = Label (left_inside_frame, text = "Name", font = ("times new roman", 13, "bold"), bg = "#0a183d", fg = "#2596be")
        name_label.grid (row = 2, column = 0, padx = 10, pady = 17, sticky = W)
       
        name_entry = ttk.Entry (left_inside_frame, textvariable = self.var_atten_name, width = 25, font = ("times new roman", 13, "bold"))
        name_entry.grid (row = 2, column = 1, padx = 10, pady = 17, sticky = W)

        # Department        
        dept_label = Label (left_inside_frame, text = "Department", font = ("times new roman", 13, "bold"), bg = "#0a183d", fg = "#2596be")
        dept_label.grid (row = 3, column = 0, padx = 10, pady = 17, sticky = W)
       
        dept_entry = ttk.Entry (left_inside_frame, textvariable = self.var_atten_dept, width = 25, font = ("times new roman", 13, "bold"))
        dept_entry.grid (row = 3, column = 1, padx = 10, pady = 17, sticky = W)

        # Time        
        time_label = Label (left_inside_frame, text = "Time", font = ("times new roman", 13, "bold"), bg = "#0a183d", fg = "#2596be")
        time_label.grid (row = 4, column = 0, padx = 10, pady = 17, sticky = W)
       
        time_entry = ttk.Entry (left_inside_frame, textvariable = self.var_atten_time, width = 25, font = ("times new roman", 13, "bold"))
        time_entry.grid (row = 4, column = 1, padx = 10, pady = 17, sticky = W)

        # Date        
        date_label = Label (left_inside_frame, text = "Date", font = ("times new roman", 13, "bold"), bg = "#0a183d", fg = "#2596be")
        date_label.grid (row = 5, column = 0, padx = 10, pady = 17, sticky = W)
       
        date_entry = ttk.Entry (left_inside_frame, textvariable = self.var_atten_date, width = 25, font = ("times new roman", 13, "bold"))
        date_entry.grid (row = 5, column = 1, padx = 10, pady = 17, sticky = W)
        
        # Attendance
        attendance_label = Label (left_inside_frame, text = "Attendance Status", font = ("times new roman", 13, "bold"), bg = "#0a183d", fg = "#2596be")
        attendance_label.grid (row = 6, column = 0, padx = 10, pady = 17)
       
        attendance_combo = ttk.Combobox (left_inside_frame,textvariable = self.var_atten_attendance, font = ("times new roman", 10, "bold"), state = "readonly", width = 30)
        attendance_combo["values"] = ("Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid (row = 6, column = 1, padx = 10, pady = 17, sticky = W)

        # Buttons Frame
        btn_frame = Frame (left_inside_frame, bd = 2, relief = RIDGE, bg = "white")
        btn_frame.place (x = 25, y = 475, width = 476, height = 34)

        import_btn = Button (btn_frame, command = self.importCsv, text = "Import .csv",width = 12, font = ("times new roman", 11, "bold"), bg = "#0a183d", fg = "#2596be")
        import_btn.grid(row = 0, column = 0)

        export_btn = Button (btn_frame, command = self.exportCsv, text = "Export .csv",width = 12, font = ("times new roman", 11, "bold"), bg = "#0a183d", fg = "#2596be")
        export_btn.grid(row = 0, column = 1)

        update_btn = Button (btn_frame, text = "Update",width = 12, font = ("times new roman", 11, "bold"), bg = "#0a183d", fg = "#2596be")
        update_btn.grid(row = 0, column = 2)
        
        reset_btn = Button (btn_frame, command = self.reset_data, text = "Reset",width = 12, font = ("times new roman", 11, "bold"), bg = "#0a183d", fg = "#2596be")
        reset_btn.grid(row = 0, column = 3)

        """
        Right Label Frame
        """
        right_frame = LabelFrame (main_frame, bd = 2, bg = "#0a183d", relief = RIDGE, text = "Attendance Details", font = ("times new roman", 14, "bold"), fg = "#0660b1")
        right_frame.place (x = 570, y = 10, width = 545, height = 585)

        right_label_frame = Frame (right_frame, bd = 2, relief = RIDGE, bg = "#0a183d")
        right_label_frame.place (x = 5, y = 5, width = 530, height = 540)

        ############## SCROLL BAR TABLE ##############
        # Table Frame
        table_frame = Frame (right_frame, bd = 2, bg = "#0a183d", relief = RIDGE)
        table_frame.place (x = 5, y = 5, width = 530, height = 540)
                
        scroll_x = ttk.Scrollbar (table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar (table_frame, orient = VERTICAL)

        self.AttendanceReportTable = ttk.Treeview (table_frame, column = ("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack (side = BOTTOM, fill = X)
        scroll_y.pack (side = RIGHT, fill = Y)

        scroll_x.config (command = self.AttendanceReportTable.xview)
        scroll_y.config (command = self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading ("id", text = "Attendance ID")
        self.AttendanceReportTable.heading ("roll", text = "Roll")
        self.AttendanceReportTable.heading ("name", text = "Name")
        self.AttendanceReportTable.heading ("department", text = "Department")
        self.AttendanceReportTable.heading ("time", text = "Time")
        self.AttendanceReportTable.heading ("date", text = "Date")
        self.AttendanceReportTable.heading ("attendance", text = "Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column ("id", width = 100)
        self.AttendanceReportTable.column ("roll", width = 100)
        self.AttendanceReportTable.column ("name", width = 100)
        self.AttendanceReportTable.column ("department", width = 120)
        self.AttendanceReportTable.column ("time", width = 100)
        self.AttendanceReportTable.column ("date", width = 100)
        self.AttendanceReportTable.column ("attendance", width = 100)


        self.AttendanceReportTable.pack (fill = BOTH, expand = 1)
        self.AttendanceReportTable.bind ("<ButtonRelease>", self.get_cursor)

    ########################## FETCH DATA #########################
    def fetchData (self, rows):
        self.AttendanceReportTable.delete (*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert ("", END, values = i)

    ######################## IMPORT DATA ###########################
    def importCsv (self):
        global mydata
        mydata.clear ()
        fln = filedialog.askopenfilename (initialdir = os.getcwd (), title = "Open CSV", filetypes = (("CSV File", "*.csv"), ("All File", "*.*")), parent = self.root)

        with open (fln) as myfile:
            csvread = csv.reader (myfile, delimiter = ",")
            for i in csvread:
                mydata.append (i)
            self.fetchData(mydata)

    ####################### EXPORT DATA ############################
    def exportCsv (self):
        try:
            if len (mydata) < 1:
                messagebox.showerror ("No Data", "No data found to export!", parent = self.root)
                return False
            fln = filedialog.asksaveasfilename (initialdir = os.getcwd (), title = "Open CSV", filetypes = (("CSV File", "*.csv"), ("All File", "*.*")), parent = self.root)
            with open (fln, mode = "w", newline = "\n") as myfile:
                exp_write = csv.writer (myfile, delimiter = ",")
                for i in mydata:
                    exp_write.writerow (i)
                messagebox.showinfo ("Data Export", "Your data exported to " + os.path.basename (fln) + " successfully")
        
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)
        
    def get_cursor (self, event = ""):
        cursor_row = self.AttendanceReportTable.focus ()
        content = self.AttendanceReportTable.item (cursor_row)
        rows = content ['values']
        self.var_atten_id.set (rows[0])
        self.var_atten_roll.set (rows[1])
        self.var_atten_name.set (rows[2])
        self.var_atten_dept.set (rows[3])
        self.var_atten_time.set (rows[4])
        self.var_atten_date.set (rows[5])
        self.var_atten_attendance.set (rows[6])

    def reset_data (self):
        self.var_atten_id.set ("")
        self.var_atten_roll = ("")
        self.var_atten_name = ("")
        self.var_atten_dept = ("")
        self.var_atten_time = ("")
        self.var_atten_date = ("")
        self.var_atten_attendance = ("")

if __name__ == "__main__":
    root = Tk ()
    obj = Attendance (root)
    root.mainloop ()
