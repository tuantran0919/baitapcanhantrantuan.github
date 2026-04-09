import random

# nhập n
n = int(input("Nhap bac ma tran: "))

# tạo ma trận A
A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

print("Ma tran A:")
for row in A:
    print(*row)

# tạo ma trận B
B = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        s = 0
        
        # đường chéo chính (↘ ↖)
        x, y = i, j
        while x >= 0 and y >= 0:
            s += A[x][y]
            x -= 1
            y -= 1
            
        x, y = i+1, j+1
        while x < n and y < n:
            s += A[x][y]
            x += 1
            y += 1
        
        # đường chéo phụ (↙ ↗)
        x, y = i-1, j+1
        while x >= 0 and y < n:
            s += A[x][y]
            x -= 1
            y += 1
            
        x, y = i+1, j-1
        while x < n and y >= 0:
            s += A[x][y]
            x += 1
            y -= 1
        
        B[i][j] = s

print("Ma tran B:")
for row in B:
    print(*row)
