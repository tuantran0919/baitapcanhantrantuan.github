import tkinter as tk
from tkinter import messagebox
import math

# Hàm đệ quy
def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

# Hàm công thức đóng (Binet)
def fib_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return round((phin - psin) / math.sqrt(5))

# Xử lý khi bấm nút
def calculate():
    try:
        n = int(entry.get())
        
        if n <= 0 or n >= 40:
            messagebox.showerror("Lỗi", "Nhập n trong khoảng 1 < n < 40")
            return
        
        # Tính toán
        result_recursive = fib_recursive(n)
        result_binet = fib_binet(n)
        
        # Hiển thị
        label_recursive.config(text=f"Đệ quy: F({n}) = {result_recursive}")
        label_binet.config(text=f"Công thức đóng: F({n}) = {result_binet}")
        
        if result_recursive == result_binet:
            label_check.config(text="✔ Hai kết quả KHỚP nhau", fg="green")
        else:
            label_check.config(text="✘ Hai kết quả KHÔNG khớp", fg="red")
            
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ")

# Giao diện
root = tk.Tk()
root.title("Fibonacci GUI")
root.geometry("400x300")

tk.Label(root, text="Nhập n (1 < n < 40):").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Tính Fibonacci", command=calculate).pack(pady=10)

label_recursive = tk.Label(root, text="")
label_recursive.pack()

label_binet = tk.Label(root, text="")
label_binet.pack()

label_check = tk.Label(root, text="")
label_check.pack(pady=10)

root.mainloop()
