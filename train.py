from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
  def __init__ (self, root):
    self.root = root
    self.root.geometry ("1530x790+0+0")
    self.root.title ("Face Recognition System")

    # Background Image
    bg_img = Image.open (r"Images\train_data_bg.jpg")
    bg_img.resize ((1440, 790), Image.ANTIALIAS)
    self.bg_photoimg = ImageTk.PhotoImage (bg_img)

    bg_lbl = Label (self.root, image = self.bg_photoimg)
    bg_lbl.place (x = 0, y = 0, width = 1440, height = 790)

    # # Title Label
    # title_lbl = Label (bg_lbl, text = "STUDENT MANAGEMENT SYSTEM", font = ("times new roman", 30, "bold"), bg = "#0a183d", fg = "#0660b1")
    # title_lbl.place (x = 0, y = 0, width = 1440, height = 30)
            
    train_btn = Button (bg_lbl,command = self.train_classifier, text = "Train\nData",width = 12, font = ("times new roman", 45, "bold"), bg = "#012531", fg = "#014052", activebackground = "#014052", activeforeground = "#012531")
    train_btn.place (x = 60, y = 280, width = 200, height = 250)

  def train_classifier (self):
    try:
      data_dir = ("data")
      path = [os.path.join (data_dir, file) for file in os.listdir (data_dir)]
      
      faces = []
      ids = []

      for image in path:
        img = Image.open (image).convert('L') # GRAY SCALE IMAGE
        imageNp = np.array (img, 'uint8')
        id = int (os.path.split (image) [1].split ('.') [1])

        faces.append (imageNp)
        ids.append (id)
        cv2.imshow ("Training", imageNp)
        cv2.waitKey (1) == 13

      ids = np.array (ids)

      ##################### TRAIN CLASSIFIER AND SAVE ##########################
      clf = cv2.face.LBPHFaceRecognizer_create ()
      clf.train (faces, ids)
      clf.write("classifier.xml")
      cv2.destroyAllWindows ()
      messagebox.showinfo ("Result", "Dataset trained successfully!")
    except Exception as es:
      messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)


if __name__ == "__main__":
  root = Tk ()
  obj = Train (root)
  root.mainloop ()
    
