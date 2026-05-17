print("Nhập vào 10 số nguyên khác nhau:")
mang = []
for i in range(10):
    while True:
        try:
            so = int(input(f"Nhập phần tử thứ {i+1}: "))
            if so in mang:
                print("Số này đã tồn tại trong mảng. Vui lòng nhập số khác!")
                continue
            mang.append(so)
            break
        except ValueError:
            print("Vui lòng chỉ nhập số nguyên hợp lệ!")
print("\n[Kết quả hiển thị]")
if len(mang) == 0:
    print("Không có số lớn nhất")
else:
    so_lon_nhat = max(mang)
    vi_tri = mang.index(so_lon_nhat)
    print(f"Số lớn nhất: {so_lon_nhat}")
    print(f"Vị trí: {vi_tri}")
