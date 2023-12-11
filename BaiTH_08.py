import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def open_file_img():
    file_path = filedialog.askopenfilename(filetypes=[("JEPG", "*.jpeg"), ("PNG", "*.png")])
    if file_path:
        label_img_re.config(text="Ảnh kết quả")
        global img
        image = cv2.imread(file_path)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        label_img_or.config(image=img_tk)
        label_img_or.image = img_tk

def detect_egde():
    if img is not None:
        global canny
        canny = cv2.Canny(img, 50, 240)
        img_rgb = cv2.cvtColor(canny, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        label_img_re.config(image=img_tk)
        label_img_re.image = img_tk
    else:
        label_text_re.config(text="Hãy chọn ảnh")

def save_image():
    if img is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=[".png", ".jpeg"], filetypes=[("PNG", "*.png"), ("JPEG", "*.jpeg")])
        if file_path:
            cv2.imwrite(file_path, canny)
            print("Lưu ảnh thành công.")
    else:
        label_text_re.config(text="Không có ảnh để lưu")


w = Tk()
w.title("Ứng dụng thực hiện tách biên ảnh")

frame_input = Frame(w)
frame_input.pack()

button_file = Button(frame_input, text="Chọn ảnh", command=open_file_img)
button_file.pack(side=LEFT)

button_cre = Button(frame_input, text="Tách biên ảnh", command=detect_egde)
button_cre.pack(side=LEFT)

button_save = Button(frame_input, text="Lưu ảnh", command=save_image)
button_save.pack(side=LEFT)

frame_output = Frame(w)
frame_output.pack()

frame_origin = Frame(frame_output)
frame_origin.pack(side=LEFT)

label_text_or = Label(frame_origin, text="Ảnh gốc")
label_text_or.pack()

label_img_or = Label(frame_origin)
label_img_or.pack()

frame_resutl = Frame(frame_output)
frame_resutl.pack(side=LEFT)

label_text_re = Label(frame_resutl, text="Ảnh kết quả")
label_text_re.pack()

label_img_re = Label(frame_resutl)
label_img_re.pack()

w.mainloop()