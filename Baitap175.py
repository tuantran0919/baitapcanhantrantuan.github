import tkinter as tk
from tkinter import filedialog, messagebox

def choose_input():
    file_path = filedialog.askopenfilename()
    entry_input.delete(0, tk.END)
    entry_input.insert(0, file_path)

def choose_output():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    entry_output.delete(0, tk.END)
    entry_output.insert(0, file_path)

def convert_file():
    input_file = entry_input.get()
    output_file = entry_output.get()
    
    if not input_file or not output_file:
        messagebox.showerror("Lỗi", "Vui lòng chọn đủ file!")
        return
    
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Chuyển sang chữ hoa
        content_upper = content.upper()
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content_upper)
        
        messagebox.showinfo("Thành công", "Đã chuyển đổi thành chữ HOA!")
        
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


# Giao diện
root = tk.Tk()
root.title("Chuyển chữ thường → CHỮ HOA")
root.geometry("500x250")

# File input
tk.Label(root, text="File đầu vào:").pack()
entry_input = tk.Entry(root, width=50)
entry_input.pack()
tk.Button(root, text="Chọn file", command=choose_input).pack(pady=5)

# File output
tk.Label(root, text="File đầu ra:").pack()
entry_output = tk.Entry(root, width=50)
entry_output.pack()
tk.Button(root, text="Chọn nơi lưu", command=choose_output).pack(pady=5)

# Nút xử lý
tk.Button(root, text="Chuyển đổi", command=convert_file, bg="green", fg="white").pack(pady=15)

root.mainloop()
