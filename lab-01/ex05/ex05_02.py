def tinh_tong_chuoi(chuoi):
    # Tách các từ từ chuỗi và lọc các số nguyên dương và âm
    so_nguyen_duong = []
    so_am = []

    word = ""
    for char in chuoi:
        if char.isdigit() or char == "-":
            word += char
        else:
            if word:
                if int(word) > 0:
                    so_nguyen_duong.append(int(word))
                elif int(word) < 0:
                    so_am.append(int(word))
                word = ""

    # Kiểm tra từ cuối cùng nếu có
    if word:
        if int(word) > 0:
            so_nguyen_duong.append(int(word))
        elif int(word) < 0:
            so_am.append(int(word))

    # Tính tổng các số nguyên dương và âm
    tong_duong = sum(so_nguyen_duong)
    tong_am = sum(so_am)

    return tong_duong, tong_am


# Chuỗi đầu vào
chuoi = "-100#^sdfkj8902w3ir021@swf-20"

# Tính tổng và in kết quả
tong_duong, tong_am = tinh_tong_chuoi(chuoi)
print("Giá trị dương:", tong_duong)
print("Giá trị âm:", tong_am)
