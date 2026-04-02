# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
# Danh sách số nguyên tố < 1000
primes = [i for i in range(2, 1000) if is_prime(i)]

# Kiểm chứng và in kết quả
for n in primes:
    if n <= 5:
        continue
    for a in primes:
        for b in primes:
            c = n - a - b
            if c >= 2 and is_prime(c):
                print(f"{n} = {a} + {b} + {c}")
                break
        else:
            continue
        break
