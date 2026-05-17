try:
    n = int(input())
    if n < 0:
        print("Số lượng phần tử không được âm")
    elif n == 0:
        print("Mảng không có phần tử")
    else:
        characters = []
        while len(characters) < n:
            user_input = input()
            parsed_chars = [x.strip("'").strip('"') for x in user_input.replace('[', '').replace(']', '').replace(',', ' ').split()]
            characters.extend(parsed_chars)
        characters = characters[:n]        
        numbers = []
        for x in characters:
            try:
                numbers.append(int(x))
            except ValueError:
                pass             
        if numbers:
            total_sum = sum(numbers)
            print(total_sum)
        else:
            print("Không có phần tử nào là số")
except ValueError:
    print("Số lượng phần tử không được âm")
