# Nhap n
n = int(input("Nhap so phan tu: "))

# Nhap mang
a = []
for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

# Dem so lan xuat hien
count = {}

for x in a:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

# In ket qua
print("\nSo lan xuat hien:")
for k in count:
    print(k, "xuat hien", count[k], "lan")
