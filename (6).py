n = int(input("Nhap so luong phan tu: "))
if n < 0:
    print("So luong phan tu khong duoc nho hon 0")

elif n == 0:
    print("Mang khong co phan tu nao")
else:
    arr = []

    for i in range(n):
        x = int(input(f"Nhap phan tu thu {i + 1}: "))
        arr.append(x)
    arr.sort(reverse=True)
    if len(arr) < 2:
        print("Khong ton tai so lon thu 2")
    else:
        print("So lon thu 2 la:", arr[1])
