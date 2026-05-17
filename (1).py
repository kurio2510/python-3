mang_so_nguyen = []
print("Vui lòng nhập vào 10 số nguyên:")
for i in range(10):
    while True:
        try:
            so = int(input(f"Phần tử [{i}]: "))
            mang_so_nguyen.append(so)
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
ket_qua = [so for so in mang_so_nguyen if so >= 10]
print("\n--- Kết quả ---")
if len(ket_qua) > 0:
    print(*(ket_qua))
else:
    print("Không có số nào lớn hơn 10")
