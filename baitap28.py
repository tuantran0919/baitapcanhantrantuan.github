from decimal import Decimal, ROUND_HALF_UP
import tkinter as tk
from tkinter import messagebox

# ===== Hàm làm tròn kiểu Excel =====
def round_excel(number, num_digits):
    q = Decimal('1e{}'.format(-num_digits))
    d = Decimal(str(number))
    result = d.quantize(q, rounding=ROUND_HALF_UP)
    return float(result)

# ===== Xử lý khi bấm nút =====
def tinh_toan():
    try:
        x = float(entry_so.get())
        n = int(entry_chuso.get())
        
        kq = round_excel(x, n)
        label_kq.config(text=f"Kết quả: {kq}")
        
    except:
        messagebox.showerror("Lỗi", "Nhập sai định dạng!")

# ===== Giao diện =====
root = tk.Tk()
root.title("ROUND Excel - Tkinter")
root.geometry("300x200")

# Nhập số
tk.Label(root, text="Nhập số:").pack()
entry_so = tk.Entry(root)
entry_so.pack()

# Nhập số chữ số làm tròn
tk.Label(root, text="Số chữ số làm tròn:").pack()
entry_chuso = tk.Entry(root)
entry_chuso.pack()

# Nút bấm
tk.Button(root, text="Tính", command=tinh_toan).pack(pady=10)

# Hiển thị kết quả
label_kq = tk.Label(root, text="Kết quả: ")
label_kq.pack()

# Chạy app
root.mainloop()
