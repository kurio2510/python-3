import sys
try:
    n = int(input("Nhập n = "))
except ValueError:
    print("Vui lòng nhập một số nguyên!")
    sys.exit()
if n < 0:
    print("Số lượng phần tử không hợp lệ")
elif n == 0:
    print("Mảng không có phần tử")
else:
    mang = []
    print(f"Nhập {n} phần tử cho mảng:")
    for i in range(n):
        while True:
            try:
                so = float(input(f"Nhập phần tử thứ {i+1}: "))
                mang.append(so)
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")
    dem_so_nguyen_am = 0
    for num in mang:
        if num < 0 and num.is_integer():
            dem_so_nguyen_am += 1
    print("\n[Kết quả hiển thị]")
    print(dem_so_nguyen_am)
