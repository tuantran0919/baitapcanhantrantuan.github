def check_sin(s):
    if len(s) != 9 or not s.isdigit():
        return False
    d = list(map(int, s[::-1]))
    tong = d[0]  # số kiểm tra
    for i in range(1, 9):
        if i % 2 == 1:
            x = d[i] * 2
            tong += x // 10 + x % 10
        else:
            tong += d[i]
    return tong % 10 == 0
while True:
    s = input("Nhập SIN (0 để thoát): ")
    if s == "0":
        break
    print("Hợp lệ" if check_sin(s) else "Không hợp lệ")
