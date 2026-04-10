import tkinter as tk
from tkinter import messagebox
import math

# Hàm làm tròn kiểu Excel
def excel_round(x, n):
    factor = 10 ** n
    y = x * factor

    # Làm tròn "0.5 ra xa 0"
    if y >= 0:
        y = math.floor(y + 0.5)
    else:
        y = math.ceil(y - 0.5)

    return y / factor


# Hàm xử lý khi bấm nút
def tinh_toan():
    try:
        x = float(entry_x.get())
        n = int(entry_n.get())

        result = excel_round(x, n)

        label_kq.config(text=f"Kết quả: {result}")

    except:
        messagebox.showerror("Lỗi", "Nhập sai dữ liệu!")


# ===== Giao diện =====
root = tk.Tk()
root.title("Mô phỏng ROUND Excel")
root.geometry("350x220")

# Nhập số x
tk.Label(root, text="Nhập số thực x:").pack(pady=5)
entry_x = tk.Entry(root)
entry_x.pack()

# Nhập n
tk.Label(root, text="Độ chính xác (n):").pack(pady=5)
entry_n = tk.Entry(root)
entry_n.pack()

# Nút tính
tk.Button(root, text="Làm tròn", command=tinh_toan).pack(pady=10)

# Hiển thị kết quả
label_kq = tk.Label(root, text="Kết quả: ")
label_kq.pack()

# Chạy chương trình
root.mainloop()
