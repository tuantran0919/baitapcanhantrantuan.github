import random

# Nhập kích thước
n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))

# Tạo ma trận ngẫu nhiên [-100, 100]
a = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(-100, 100))
    a.append(row)

# Xuất ma trận ban đầu
print("Ma trận ban đầu:")
for row in a:
    print(*row)

# Xoay 90 độ theo chiều kim đồng hồ
# (kết quả sẽ là ma trận m x n)
b = []
for j in range(m):
    new_row = []
    for i in range(n - 1, -1, -1):
        new_row.append(a[i][j])
    b.append(new_row)

# In ma trận sau khi xoay
print("\nMa trận sau khi xoay 90 độ:")
for row in b:
    print(*row)
