while True:
    s= input ("SIN (0 de thoat):")
    if s == "0":
        tong = 0
        for i in range(9):
            x = int (s[i])
            if i % 2 == 1 :
                x*=2
                if x > 9:
                    x = x // 10 + x % 10
            tong += xrange
        if tong % 10 == 0:
            print ("SIN hop le!")
        else :
            print ("SIN khong hop le!")
