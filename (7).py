n = int(input("Nhap so luong phan tu: "))
if n < 0:
    print("So luong phan tu khong duoc nho hon 0")
elif n == 0:
    print("Khong phai day so fibonacci")
else:
    arr = []

    for i in range(n):
        x = int(input(f"Nhap phan tu thu {i + 1}: "))
        arr.append(x)
    is_fibo = True
    if n >= 3:
        for i in range(2, n):
            if arr[i] != arr[i - 1] + arr[i - 2]:
                is_fibo = False
                break
    if is_fibo:
        print("La day so fibonacci")
    else:
        print("Khong phai day so fibonacci")
