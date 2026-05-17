try:
    n = int(input())
    if n <= 0:
        print("Không có ký tự số")
    else:
        characters = []
        while len(characters) < n:
            user_input = input()
            parsed_chars = [x.strip("'").strip('"') for x in user_input.replace('[', '').replace(']', '').replace(',', ' ').split()]
            characters.extend(parsed_chars)
        characters = characters[:n]
        digit_characters = [x for x in characters if x.isdigit()]
        if digit_characters:
            print(" ".join(digit_characters))
        else:
            print("Không có ký tự số")
except ValueError:
    print("Không có ký tự số")
