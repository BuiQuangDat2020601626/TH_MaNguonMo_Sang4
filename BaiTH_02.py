# Giải PT
# Tính đạo hàm
# Tính tích phân
# Tính giới hạn

from tkinter import *
import sympy as sym

x = sym.symbols('x')

def solve_eq():
    eq_str = entry_n.get()
    try:
        eq = sym.Eq(sym.sympify(eq_str), 0)
        sol = sym.solve(eq, x)
        #result = ", ".join([f"x{i+1} = {j}" for i,j in enumerate(sol)])
        result = ", ".join([f"x{i+1} = {j:.2f}" if not j.is_integer else f"x{i+1} = {int(j)}" for i, j in enumerate(sol)])
        label_result.config(text="Nghiệm của phương trình là: \n"+result)
    except Exception as e:
        label_result.config(text=f"Lỗi: {e}")

def derivative_eq():
    eq_str = entry_n.get()
    try:
        n = int(entry_de.get())
        eq = sym.sympify(eq_str)
        derivative = sym.diff(eq, x, n)
        result = str(derivative)
        label_result.config(text="Đạo hàm của phương trình: \n"+result)
    except Exception as e:
        label_result.config(text=f"Lỗi: {e}")

def integral_eq():
    eq_str = entry_n.get()
    try:
        eq = sym.sympify(eq_str)
        integral = sym.integrate(eq, x)
        result = str(integral)
        label_result.config(text="Tích phân của phương trình: \n"+result)
    except Exception as e:
        label_result.config(text=f"Lỗi: {e}")

def limit_eq():
    eq_str = entry_n.get()
    try:
        limit_value = float(entry_limit.get())
        eq = sym.sympify(eq_str)
        limit = sym.limit(eq, x, limit_value) 
        result = str(limit)
        label_result.config(text=f"Giới hạn của phương trình khi x tiến đến {limit_value}: \n"+result)
    except Exception as e:
        label_result.config(text=f"Lỗi: {e}")


w = Tk()
w.title("Ứng dụng hỗ trợ giải tích")
w.geometry("360x480")


label_w = Label(w, text="Nhập phương trình ẩn x: ")
label_w.pack()
entry_n = Entry(w)
entry_n.pack()

button_solve = Button(w, text="Giải", command=solve_eq)
button_solve.pack()

frame_de = Frame(w)
frame_de.pack()
label_de = Label(frame_de, text="Nhập cấp đạo hàm: ")
label_de.pack(side=LEFT)
entry_de = Entry(frame_de)
entry_de.pack(side=LEFT)
button_der= Button(w, text="Đạo hàm", command=derivative_eq)
button_der.pack()

button_inte = Button(w, text="Tích phân", command=integral_eq)
button_inte.pack()

frame_limit = Frame(w)
frame_limit.pack()
label_limit = Label(frame_limit, text="Nhập giới hạn: ")
label_limit.pack(side=LEFT)
entry_limit = Entry(frame_limit)
entry_limit.pack(side=LEFT)
button_limit = Button(w, text="Giới hạn", command=limit_eq)
button_limit.pack()

label_result = Label(w, text="")
label_result.pack()

w.mainloop()