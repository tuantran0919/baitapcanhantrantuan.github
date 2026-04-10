import tkinter as tk
from tkinter import messagebox

def xu_ly():
    try:
        n = int(entry_n.get())

        if n < 1 or n > 99:
            messagebox.showerror("Lỗi", "n phải từ 1 đến 99")
            return

        arr = list(map(int, entry_arr.get().split()))

        if len(arr) != n:
            messagebox.showerror("Lỗi", "Số phần tử không đúng!")
            return

        # Đếm số lần xuất hiện
        count = {}
        for x in arr:
            count[x] = count.get(x, 0) + 1

        # Tìm max và min theo yêu cầu (ưu tiên xuất hiện đầu tiên)
        max_val = arr[0]
        min_val = arr[0]

        for x in arr:
            if count[x] > count[max_val]:
                max_val = x
            if count[x] < count[min_val]:
                min_val = x

        label_kq.config(
            text=f"Phan tu xuat hien nhieu nhat: {max_val}[{count[max_val]}]\n"
                 f"Phan tu xuat hien it nhat: {min_val}[{count[min_val]}]"
        )

    except:
        messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ!")


# ===== GUI =====
root = tk.Tk()
root.title("Xử lý mảng")
root.geometry("400x250")

tk.Label(root, text="Nhập n [1-99]:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Label(root, text="Nhập các phần tử (cách nhau bằng dấu cách):").pack()
entry_arr = tk.Entry(root, width=40)
entry_arr.pack()

tk.Button(root, text="Xử lý", command=xu_ly).pack(pady=10)

label_kq = tk.Label(root, text="")
label_kq.pack()

root.mainloop()
