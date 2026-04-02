# Nhập số phần tử
n = int(input("Nhập n: "))

# Nhập mảng
a = []
for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

# Đếm số lần xuất hiện
count = {}
for x in a:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

# Tìm phần tử xuất hiện nhiều nhất (lấy cái xuất hiện đầu tiên)
max_freq = max(count.values())
for x in a:
    if count[x] == max_freq:
        print("Phần tử xuất hiện nhiều nhất:", x)
        break

# Tìm phần tử xuất hiện ít nhất (lấy cái xuất hiện đầu tiên)
min_freq = min(count.values())
for x in a:
    if count[x] == min_freq:
        print("Phần tử xuất hiện ít nhất:", x)
        break
