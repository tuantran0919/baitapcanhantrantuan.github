import tkinter as tk
from tkinter import scrolledtext

# Kiểm tra số nguyên tố
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tạo danh sách số nguyên tố < 1000
primes = [i for i in range(2, 1000) if la_nguyen_to(i)]

# Hàm kiểm chứng
def kiem_chung():
    output.delete(1.0, tk.END)

    count = 0

    for n in primes:
        if n <= 5:
            continue

        found = False

        # tìm a + b + c = n
        for i in range(len(primes)):
            for j in range(len(primes)):
                for k in range(len(primes)):
                    a, b, c = primes[i], primes[j], primes[k]

                    if a + b + c == n:
                        output.insert(tk.END, f"{n} = {a} + {b} + {c}\n")
                        count += 1
                        found = True
                        break
                if found:
                    break
            if found:
                break

    output.insert(tk.END, f"\nKiem chung dung voi {count} so nguyen to")


# ===== GUI =====
root = tk.Tk()
root.title("Goldbach lẻ (n < 1000)")
root.geometry("500x500")

btn = tk.Button(root, text="Kiểm chứng", command=kiem_chung)
btn.pack(pady=10)

output = scrolledtext.ScrolledText(root, width=60, height=25)
output.pack()

root.mainloop()
