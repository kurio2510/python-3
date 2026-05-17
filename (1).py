a = []

while True:
    print("\n----- MENU -----")
    print("1. Nhập mảng")
    print("2. Hiển thị mảng")
    print("3. Thêm phần tử")
    print("4. Sửa phần tử")
    print("5. Xóa phần tử")
    print("6. Thoát")

    chon = input("Nhập lựa chọn: ")
    # Nhập mảng
    if chon == "1":
        n = int(input("Nhập số phần tử: "))
        a = []
        for i in range(n):
            x = int(input("Nhập phần tử: "))
            a.append(x)
    # Hiển thị mảng
    elif chon == "2":
        print("Mảng là:", a)
    # Thêm phần tử
    elif chon == "3":
        x = int(input("Nhập phần tử cần thêm: "))
        a.append(x)
    # Sửa phần tử
    elif chon == "4":
        vt = int(input("Nhập vị trí cần sửa: "))
        moi = int(input("Nhập giá trị mới: "))

        a[vt] = moi
    # Xóa phần tử
    elif chon == "5":
        vt = int(input("Nhập vị trí cần xóa: "))

        a.pop(vt)
    # Thoát
    elif chon == "6":
        print("Đã thoát chương trình")
        break
    else:
        print("Chọn sai!")