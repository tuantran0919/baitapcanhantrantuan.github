from decimal import Decimal, ROUND_HALF_UP

def round_excel(number, num_digits):
    # Tạo độ chính xác theo num_digits
    q = Decimal('1e{}'.format(-num_digits))
    # Dùng ROUND_HALF_UP giống Excel
    result = Decimal(str(number)).quantize(q, rounding=ROUND_HALF_UP)
    return float(result)

# ====== Chương trình chính ======
x = float(input("Nhap so: "))
n = int(input("Nhap so chu so can lam tron: "))

kq = round_excel(x, n)

print("Ket qua:", kq)
