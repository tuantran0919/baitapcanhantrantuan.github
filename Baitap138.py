import tkinter as tk
from tkinter import messagebox

def process_text():
    try:
        # Lấy toàn bộ nội dung
        content = input_text.get("1.0", tk.END)
        
        lines = content.splitlines()
        result = ""
        
        for line in lines:
            # Giới hạn 50 ký tự (nếu dài thì cắt)
            line = line[:50]
            # Canh phải 50 ký tự
            result += line.rjust(50) + "\n"
        
        # Hiển thị kết quả
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


# Tạo cửa sổ
root = tk.Tk()
root.title("Canh phải văn bản 50 ký tự")
root.geometry("600x500")

# Label nhập
tk.Label(root, text="Nhập nội dung (mỗi dòng ≤ 50 ký tự):").pack()

# Ô nhập
input_text = tk.Text(root, height=10, width=70)
input_text.pack()

# Nút xử lý
tk.Button(root, text="Canh phải", command=process_text).pack(pady=10)

# Label kết quả
tk.Label(root, text="Kết quả:").pack()

# Ô kết quả
output_text = tk.Text(root, height=10, width=70)
output_text.pack()

# Chạy chương trình
root.mainloop()
