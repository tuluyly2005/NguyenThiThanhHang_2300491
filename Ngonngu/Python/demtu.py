chuoi = input("Nhap chuoi: ")

# Tách từ
tu = chuoi.split()

# Đếm số từ
print("So tu trong chuoi:", len(tu))

# Liệt kê từ dài hơn 5 ký tự
print("Cac tu dai hon 5 ky tu:")

for i in tu:
    if len(i) > 5:
        print(i)
