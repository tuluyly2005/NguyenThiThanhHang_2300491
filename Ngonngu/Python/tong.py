n = int(input("Nhap N: "))

tong = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        tong += i

print("Tong cac so chan tu 1 den", n, "la:", tong)
