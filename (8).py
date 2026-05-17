numbers = []

while True:
    print("======================MENU======================")
    print("1. Nhập số phần tử cần nhập và giá trị các phần tử")
    print("2. In ra giá trị các phần tử đang quản lý")
    print("3. In ra giá trị các phần tử chẵn và tính tổng")
    print("4. In ra giá trị lớn nhất và nhỏ nhất trong mảng")
    print("5. In ra các phần tử là số nguyên tố trong mảng và tính tổng")
    print("6. Nhập vào một số và thống kê trong mảng có bao nhiêu phần tử đó")
    print("7. Thêm một phần từ vào vị trí chỉ định")
    print("8. Thoát")
    
    choice = input("Lựa chọn của bạn: ").strip()
    
    if choice == '1':
        try:
            n = int(input("Nhập số phần tử: "))
            if n < 0:
                print("Số lượng phần tử không hợp lệ")
            else:
                numbers = []
                while len(numbers) < n:
                    user_input = input(f"Nhập các phần tử (còn thiếu {n - len(numbers)} phần tử): ")
                    parsed_numbers = [int(x) for x in user_input.replace('[', '').replace(']', '').replace(',', ' ').split() if x.isdigit() or (x.startswith('-') and x[1:].isdigit())]
                    numbers.extend(parsed_numbers)
                numbers = numbers[:n]
                print("Đã nhập mảng thành công")
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ")      
    elif choice == '2':
        if not numbers:
            print("Mảng trống")
        else:
            print(f"Các phần tử đang quản lý: {numbers}")         
    elif choice == '3':
        if not numbers:
            print("Mảng trống")
        else:
            even_numbers = [x for x in numbers if x % 2 == 0]
            if even_numbers:
                total_even = sum(even_numbers)
                print(f"Các phần tử chẵn: {even_numbers}")
                print(f"Tổng các phần tử chẵn: {total_even}")
            else:
                print("Không có phần tử chẵn trong mảng")           
    elif choice == '4':
        if not numbers:
            print("Mảng trống")
        else:
            max_value = max(numbers)
            min_value = min(numbers)
            print(f"Giá trị lớn nhất: {max_value}")
            print(f"Giá trị nhỏ nhất: {min_value}")       
    elif choice == '5':
        if not numbers:
            print("Mảng trống")
        else:
            prime_numbers = []
            for x in numbers:
                if x > 1:
                    is_prime = True
                    for i in range(2, int(x**0.5) + 1):
                        if x % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        prime_numbers.append(x)          
            if prime_numbers:
                total_prime = sum(prime_numbers)
                print(f"Các phần tử là số nguyên tố: {prime_numbers}")
                print(f"Tổng các số nguyên tố: {total_prime}")
            else:
                print("Không có số nguyên tố nào trong mảng")                
    elif choice == '6':
        if not numbers:
            print("Mảng trống")
        else:
            try:
                search_value = int(input("Nhập số cần thống kê: "))
                count_value = numbers.count(search_value)
                print(f"Số {search_value} xuất hiện {count_value} lần trong mảng")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ")                
    elif choice == '7':
        try:
            value_to_add = int(input("Nhập giá trị phần tử cần thêm: "))
            index_to_add = int(input(f"Nhập vị trí cần thêm (từ 0 đến {len(numbers)}): "))
            if 0 <= index_to_add <= len(numbers):
                numbers.insert(index_to_add, value_to_add)
                print("Thêm phần tử thành công")
            else:
                print("Vị trí chỉ định vượt quá phạm vi của mảng")
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ")         
    elif choice == '8':
        print("Đang thoát chương trình...")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại từ 1 đến 8")
