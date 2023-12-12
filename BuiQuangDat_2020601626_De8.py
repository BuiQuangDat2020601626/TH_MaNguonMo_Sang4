## thêm vẽ biểu đồ đạo hàm
## thêm vẽ biểu đồ tích phân
## thêm button hiện thị lịch sử tính toán,các button tính toán, chọn file csv
## thêm nhập dữ dữ liệu đầu vào , hiện kết quả xuất ra file txt, bẫy lỗi

import tkinter as tk
from sympy import Symbol, diff, integrate, limit, solve, sin, cos
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def calculate_from_csv(filename):
    data = pd.read_csv(filename)  # Read the CSV file using pandas
    for index, row in data.iterrows():
        try:
            if row['Operation'] == 'derivative':
                expression = row['Expression']
                x = Symbol('x')
                expr = eval(expression.replace("sin", "sin").replace("cos", "cos"))
                derivative = diff(expr, x)
                result = f"Đạo hàm của {expr} là: {derivative}"
                display_and_save_result(result)

                x_vals = np.linspace(-10, 10, 1000)
                y_vals = [derivative.subs(x, val) for val in x_vals]
                plot_graph(x_vals, y_vals, f"Đồ thị của {derivative}")

            elif row['Operation'] == 'integral':
                expression = row['Expression']
                x = Symbol('x')
                expr = eval(expression.replace("sin", "sin").replace("cos", "cos"))
                integral = integrate(expr, x)
                result = f"Tích phân của {expr} là: {integral}"
                display_and_save_result(result)

                x_vals = np.linspace(-10, 10, 1000)
                y_vals = [integral.subs(x, val) for val in x_vals]
                plot_graph(x_vals, y_vals, f"Đồ thị của {integral}")

            # Similarly handle other operations in the CSV file

        except Exception as e:
            result = f"Đã xảy ra lỗi: {e}"
            display_and_save_result(result)

def choose_file():
    from tkinter import filedialog
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    calculate_from_csv(filename)

def plot_graph(x_vals, y_vals, title):
    plt.figure()
    plt.plot(x_vals, y_vals)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def display_and_save_result(result_text):
    result_label.config(text=result_text)
    with open('ketqua.txt', 'a', encoding='utf-8') as file:
        file.write(result_text + '\n')

def calculate_derivative():
    expression = entry.get()
    x = Symbol('x')
    try:
        expr = eval(expression.replace("sin", "sin").replace("cos", "cos"))
        derivative = diff(expr, x)
        result = f"Đạo hàm của {expr} là: {derivative}"
        display_and_save_result(result)

        x_vals = np.linspace(-10, 10, 1000)
        y_vals = [derivative.subs(x, val) for val in x_vals]
        plot_graph(x_vals, y_vals, f"Đồ thị của {derivative}")
    except Exception as e:
        result = f"Đã xảy ra lỗi: {e}"
        display_and_save_result(result)

def calculate_integral():
    expression = entry.get()
    x = Symbol('x')
    try:
        expr = eval(expression.replace("sin", "sin").replace("cos", "cos"))
        integral = integrate(expr, x)
        result = f"Tích phân của {expr} là: {integral}"
        display_and_save_result(result)

        x_vals = np.linspace(-10, 10, 1000)
        y_vals = [integral.subs(x, val) for val in x_vals]
        plot_graph(x_vals, y_vals, f"Đồ thị của {integral}")
    except Exception as e:
        result = f"Đã xảy ra lỗi: {e}"
        display_and_save_result(result)

def calculate_limit():
    expression = entry.get()
    x = Symbol('x')
    try:
        expr = eval(expression.replace("sin", "sin").replace("cos", "cos"))
        lim = limit(expr, x, 0)
        result = f"Giới hạn của {expr} khi x tiến đến 0 là: {lim}"
        display_and_save_result(result)
    except Exception as e:
        result = f"Đã xảy ra lỗi: {e}"
        display_and_save_result(result)

def calculate_solution():
    equation = entry.get()
    x = Symbol('x')
    try:
        eq = eval(equation.replace("sin", "sin").replace("cos", "cos"))
        solution = solve(eq, x)
        result = f"Các nghiệm của {eq} là: {solution}"
        display_and_save_result(result)
    except Exception as e:
        result = f"Đã xảy ra lỗi: {e}"
        display_and_save_result(result)

def display_history():
    history_window = tk.Toplevel(root)
    history_window.title("Lịch sử tính toán")

    history_list = tk.Listbox(history_window, width=50)
    history_list.pack()

    with open('ketqua.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            history_list.insert(tk.END, line.strip())

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=50)
entry.pack()
derivative_button = tk.Button(root, text="Tính Đạo hàm", command=calculate_derivative)
derivative_button.pack()

integral_button = tk.Button(root, text="Tính Tích phân", command=calculate_integral)
integral_button.pack()

limit_button = tk.Button(root, text="Tính Giới hạn", command=calculate_limit)
limit_button.pack()

solution_button = tk.Button(root, text="Giải Phương trình", command=calculate_solution)
solution_button.pack()

history_button = tk.Button(root, text="Xem Lịch sử Tính Toán", command=display_history)
history_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

file_button = tk.Button(root, text="Chọn File CSV", command=choose_file)
file_button.pack()

root.mainloop()