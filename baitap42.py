def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sinh danh sách số nguyên tố < 1000
primes = [i for i in range(2, 1000) if is_prime(i)]

def check_number(n):
    length = len(primes)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if primes[i] + primes[j] + primes[k] == n:
                    return True, (primes[i], primes[j], primes[k])
    return False, ()

# Kiểm chứng với n < 1000
failed = []

for n in range(7, 1000, 2):  # chỉ số lẻ > 5
    ok, triple = check_number(n)
    if not ok:
        failed.append(n)
    else:
        print(f"{n} = {triple[0]} + {triple[1]} + {triple[2]}")

# Kết luận
if not failed:
    print("\nTat ca cac so le < 1000 deu thoa man!")
else:
    print("\nCac so khong thoa man:", failed)
