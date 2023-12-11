import numpy as np
from tkinter import *
from tkinter import filedialog
import pandas as pd

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
    print(file_path)
    if file_path:
        label_text.config(text="Kết quả")
        data = pd.read_csv(file_path, header=None)
        global n_data
        n_data = np.array(data)
        print(n_data)

def sort_tang():
    data = entry.get()
    data = data.split(',')
    n = None
    try:
        n = [float(value) for value in data]
        print(n)
    except ValueError:
        label_text.config(text="Hãy nhập số")
    if n:
        sx_tang = np.sort(n)
        label_text.config(text="Sắp xếp tăng: "+str(sx_tang))
    else:
        sx_tang = np.sort(n_data)
        label_text.config(text="Sắp xếp tăng: "+str(sx_tang))

def sort_giam():
    data = entry.get()
    data = data.split(',')
    n = None
    try:
        n = [float(value) for value in data]
        print(n)
    except ValueError:
        label_text.config(text="Hãy nhập số")
    if n:
        sx_tang = np.sort(n)
        sx_giam = sx_tang[::-1]
        label_text.config(text="Sắp xếp giảm: " + str(sx_giam))
    else:
        sx_tang = np.sort(n_data)
        sx_giam = sx_tang[::-1]
        label_text.config(text="Sắp xếp giảm: " + str(sx_giam))

w = Tk()
w.title("Sap xep")

button_file = Button(w, text="Chon file", command=open_file)
button_file.pack()

entry = Entry(w)
entry.pack()

button_fun = Frame(w)
button_fun.pack()

values = StringVar()
button_tang = Button(button_fun, text="SX tang", command=sort_tang)
button_tang.pack(side=LEFT)
button_giam = Button(button_fun, text="SX Giam", command=sort_giam)
button_giam.pack(side=LEFT)

label_text = Label(w, text="Kết quả")
label_text.pack()

w.mainloop()