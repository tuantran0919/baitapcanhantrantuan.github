import tkinter as tk
from tkinter import messagebox

def get_values():
    try:
        d = int(entry_d.get())
        n = int(entry_n.get())
        if n < 0:
            raise ValueError
        return d, n
    except:
        messagebox.showerror("Lỗi", "Nhập số hợp lệ!")
        return None, None

def show_result(result):
    label_result.config(text=f"Kết quả (thập phân): {result}")
    label_binary.config(text=f"Dạng nhị phân: {bin(result)}")

def bit_on():
    d, n = get_values()
    if d is not None:
        result = d | (1 << n)
        show_result(result)

def bit_off():
    d, n = get_values()
    if d is not None:
        result = d & ~(1 << n)
        show_result(result)

def bit_flip():
    d, n = get_values()
    if d is not None:
        result = d ^ (1 << n)
        show_result(result)

def is_bit():
    d, n = get_values()
    if d is not None:
        result = (d >> n) & 1
        label_result.config(text=f"Bit thứ {n}: {result}")
        label_binary.config(text=f"Dạng nhị phân: {bin(d)}")


# Giao diện
root = tk.Tk()
root.title("Thao tác BIT GUI")
root.geometry("400x300")

tk.Label(root, text="Nhập số nguyên d:").pack()
entry_d = tk.Entry(root)
entry_d.pack()

tk.Label(root, text="Nhập vị trí bit n:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Button(root, text="Bật bit (bitOn)", command=bit_on).pack(pady=3)
tk.Button(root, text="Tắt bit (bitOff)", command=bit_off).pack(pady=3)
tk.Button(root, text="Đảo bit (bitFlip)", command=bit_flip).pack(pady=3)
tk.Button(root, text="Kiểm tra bit (isBit)", command=is_bit).pack(pady=3)

label_result = tk.Label(root, text="")
label_result.pack(pady=5)

label_binary = tk.Label(root, text="")
label_binary.pack()

root.mainloop()
