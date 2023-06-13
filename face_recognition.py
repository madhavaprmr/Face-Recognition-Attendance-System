from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
  def __init__ (self, root):
    self.root = root
    self.root.geometry ("1530x790+0+0")
    self.root.title ("Face Recognition System")

    # Background Image
    bg_img = Image.open (r"Images\train_data_bg.jpg")
    bg_img = bg_img.resize ((1440, 790), Image.ANTIALIAS)
    self.bg_photoimg = ImageTk.PhotoImage (bg_img)

    bg_lbl = Label (self.root, image = self.bg_photoimg)
    bg_lbl.place (x = 0, y = 0, width = 1440, height = 790)

    # # Title Label
    # title_lbl = Label (bg_lbl, text = "FACE RECOGNITION", font = ("times new roman", 30, "bold"), bg = "#012531", fg = "#014052")
    # title_lbl.place (x = 0, y = 0, width = 1440, height = 30)

    # Face Recognition Button
    face_recognition_btn = Button (bg_lbl, command = self.face_recog, text = "Face\nRecognition",width = 12, font = ("times new roman", 45, "bold"), bg = "#012531", fg = "#014052", activebackground = "#014052", activeforeground = "#012531")
    face_recognition_btn.place (x = 60, y = 280, width = 320, height = 190)

  """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  ############################# MARK ATTENDANCE #############################
  """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  def mark_attendance (self, i, r, n, d):
    with open ("attendance_list.csv", "r+", newline = "\n") as f:
      myDataList = f.readlines ()
      name_list = []
      for line in myDataList:
        entry = line.split ((","))
        name_list.append (entry [0])
      if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
        now = datetime.now ()
        d1 = now.strftime ("%d/%m/%Y")
        dtString = now.strftime ("%H:%M:%S")
        f.writelines(f"\n{i}, {r}, {n}, {d}, {dtString}, {d1}, Present")

  """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  ############################ FACE RECOGNITION #############################
  """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  def face_recog (self):
    try:
      def draw_boundary (img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale (gray_image, scaleFactor, minNeighbors)

        coord = []

        for (x, y, w, h) in features:
          cv2.rectangle (img, (x, y), (x + w, y + h), (0, 255, 0), 2)
          id, predict = clf.predict (gray_image [y: y + h, x: x + w])
          confidence = int ((100 * (1 - predict / 300)))

          conn = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "root", database = "face_recognizer", auth_plugin = "mysql_native_password")
          my_cursor = conn.cursor ()

          my_cursor.execute ("select Name from student where Student_ID = " + str (id))
          n = my_cursor.fetchone ()
          n = "+".join(n)
          
          my_cursor.execute ("select Roll from student where Student_ID = " + str (id))
          r = my_cursor.fetchone ()
          r = "+".join(r)

          my_cursor.execute ("select Dept from student where Student_ID = " + str (id))
          d = my_cursor.fetchone ()
          d = "+".join(d)
          
          my_cursor.execute ("select Student_ID from student where Student_ID = " + str (id))
          i = my_cursor.fetchone ()
          i = "".join(i)
          

          if confidence > 77:
            cv2.putText (img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText (img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText (img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText (img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
            self.mark_attendance (i, r, n, d)
          else:
            cv2.rectangle (img, (x,y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText (img, "Unknown Face" ,(x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

          coord = [x, y, w, h]
        
        return coord
      
      def recognize (img, clf, faceCascade):
        coord = draw_boundary (img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
        return img
      
      faceCascade = cv2.CascadeClassifier ("haarcascade_frontalface_default.xml")
      clf = cv2.face.LBPHFaceRecognizer_create ()
      clf.read("classifier.xml")
      
      video_cap = cv2.VideoCapture (0)

      while True:
        ret, img = video_cap.read ()
        img = recognize (img, clf, faceCascade)
        cv2.imshow("Face Recognizer", img)
        
        if cv2.waitKey (1) == 13:
          break
      video_cap.release ()
      cv2.destroyAllWindows ()
    
    except Exception as es:
      messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)


if __name__ == "__main__":
  root = Tk ()
  obj = Face_Recognition (root)
  root.mainloop ()