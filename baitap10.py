import tkinter as tk  # import thư viện giao diện
# ===== HÀM KIỂM TRA SIN =====
def kiem_tra_sin(sin):
    # kiểm tra phải đúng 9 chữ số và toàn số
    if len(sin) != 9 or not sin.isdigit():
        return False
    digits = list(map(int, sin))  
    # -> chuyển chuỗi thành list số
    check_digit = digits[-1]  
    # -> số cuối là số kiểm tra
    core = digits[:-1]  
    # -> 8 số còn lại
    s1 = 0  # tổng vị trí lẻ
    s2 = 0  # tổng vị trí chẵn
    # ⚠️ QUAN TRỌNG: duyệt từ TRÁI sang PHẢI (đúng theo đề)
    for i in range(len(core)):
        d = core[i]

        if i % 2 == 0:  
            # vị trí lẻ (0,2,4,...)
            s1 += d
        else:  
            # vị trí chẵn
            doubled = d * 2
            if doubled >= 10:
                doubled = doubled // 10 + doubled % 10
            s2 += doubled
    total = s1 + s2 + check_digit  
    # tổng cuối cùng
    return total % 10 == 0  
    # chia hết cho 10 thì hợp lệ
# ===== HÀM XỬ LÝ NÚT =====
def xu_ly():
    sin = entry.get().strip()  
    # -> lấy dữ liệu từ ô nhập
    if sin == "0":
        root.quit()  
        # -> nhập 0 thì thoát
        return
    if kiem_tra_sin(sin):
        result_label.config(text="SIN hợp lệ!", fg="green")
    else:
        result_label.config(text="SIN không hợp lệ!", fg="red")
# ===== GIAO DIỆN =====
root = tk.Tk()  
# -> tạo cửa sổ chính
root.title("Kiểm tra SIN Canada")  
# -> tiêu đề
tk.Label(root, text="SIN (0 để thoát):").pack(pady=5)
# -> label hướng dẫn
entry = tk.Entry(root)  
# -> ô nhập
entry.pack(pady=5)
tk.Button(root, text="Kiểm tra", command=xu_ly).pack(pady=5)
# -> nút bấm
result_label = tk.Label(root, text="")  
# -> nơi hiển thị kết quả
result_label.pack(pady=5)
root.mainloop()  
# -> chạy giao diện
