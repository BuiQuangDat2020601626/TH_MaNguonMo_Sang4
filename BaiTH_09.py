import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def open_file_img():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG", "*.jpeg"), ("PNG", "*.png"), ("All file", "*.*")])
    if file_path:
        label_text_re.config(text="Ảnh kết quả")
        try:
            global img
            img = cv2.imread(file_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            img_tk = ImageTk.PhotoImage(img_pil)

            label_img_or.config(image=img_tk)
            label_img_or.image = img_tk
        except:
            label_text_re.config(text="Hãy chọn ảnh")

def improve_img():
    if img is not None:
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        # equalize the histogram of the Y channel
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        # convert the YUV image back to RGB format
        global img_output
        img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        img_rgb = cv2.cvtColor(img_output, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        label_img_re.config(image=img_tk)
        label_img_re.image = img_tk
    else:
        label_text_re.config(text="Hãy chọn ảnh")

def save_img():
    if img is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=[".jpeg", ".png"],filetypes=[("JPEG", "*.jpeg"), ("PNG", "*.png")])
        if file_path:
            cv2.imwrite(file_path, img_output)
            print("Lưu ảnh thành công")
    else:
        label_text_re.config(text="Không có ảnh để lưu")


w = Tk()
w.title("Tăng chất lượng hình ảnh thiếu sáng")

frame_input = Frame(w)
frame_input.pack()

button_file = Button(frame_input, text="Chọn ảnh", command=open_file_img)
button_file.pack(side=LEFT)

button_cre = Button(frame_input, text="Cải thiện ảnh", command=improve_img)
button_cre.pack(side=LEFT)

button_save = Button(frame_input, text="Lưu ảnh", command=save_img)
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