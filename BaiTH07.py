import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

img = None
def open_file_img():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG", "*.jpeg"), ("JPG", "*.jpg"), ("PNG", "*.png")])
    if file_path:
        label_text_re.config(text="Ảnh kết quả:")
        global img
        img = cv2.imread(file_path)
        #cv2.imshow('Original', img)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        label_img.config(image=img_tk)
        label_img.image = img_tk

def choice_button_1():
    if img is not None:
        button_lv1.pack()
        button_lv2.pack()
        entry.destroy()
        button_entry.destroy()
    else:
        label_text_re.config(text="Hãy chọn ảnh")
        
def choice_button_2():
    if img is not None:
        entry.pack()
        button_entry.pack()
        button_lv1.destroy()
        button_lv2.destroy()
        label_text_re.config(text="Hãy chọn ảnh")
    else:
        label_text_re.config(text="Hãy chọn ảnh")

def lv1():
    kernel_5x5 = np.ones((5,5), np.float32) / 25.0
    output = cv2.filter2D(img, -1, kernel_5x5)
    img_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)

    label_img_re.config(image=img_tk)
    label_img_re.image = img_tk

def lv2():
    kernel_8x8 = np.ones((8,8), np.float32) / 64.0
    output = cv2.filter2D(img, -1, kernel_8x8)
    img_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)

    label_img_re.config(image=img_tk)
    label_img_re.image = img_tk

def entry_button():
    if img is not None:
        try:
            n = int(entry.get())
            kernel = np.ones((n,n), np.float32) / float(n*n)
            output = cv2.filter2D(img, -1, kernel)
            img_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            img_tk = ImageTk.PhotoImage(img_pil)

            label_img_re.config(image=img_tk)
            label_img_re.image = img_tk
        except:
            label_text_re.config(text="Hãy nhập số nguyên")
    else:
        label_text_re.config(text="Hãy chọn ảnh")


w = Tk()
w.title("Ứng dụng lọc làm mịn")

frame_input = Frame(w)
frame_input.pack()

button_file = Button(frame_input, text="Chọn ảnh", command=open_file_img)
button_file.pack(side=LEFT, anchor='w')

frame_button = Frame(frame_input)
frame_button.pack(side=LEFT)


button_1 = Button(frame_button, text="Chọn mức làm mịn",command=choice_button_1)
button_1.pack(anchor='w')

button_2 = Button(frame_button, text="Nhập độ mịn", command=choice_button_2)
button_2.pack(anchor='w') 

button_lv1 = Button(frame_button, text="Mịn nhẹ", command=lv1)
button_lv2 = Button(frame_button, text="Mịn vừa", command=lv2)

frame_button = Frame(frame_input)
frame_button.pack(side=LEFT)

entry = Entry(frame_button)
button_entry = Button(frame_button, text="Xác nhận", command=entry_button)


frame_output = Frame(w)
frame_output.pack()

frame_origin = Frame(frame_output)
frame_origin.pack(side=LEFT)

label_text = Label(frame_origin, text="Ảnh gốc:")
label_text.pack()

label_img = Label(frame_origin)
label_img.pack()

frame_resutl = Frame(frame_output)
frame_resutl.pack(side=LEFT)

label_text_re = Label(frame_resutl, text="Ảnh kết quả:")
label_text_re.pack()

label_img_re = Label(frame_resutl)
label_img_re.pack()

w.mainloop()