 🐧 Nguyễn Thị Thanh Hằng - 2300491

Bài tập thực hành Ubuntu Linux - Shell Script - Python

Dự án gồm các bài thực hành về thao tác thư mục, xử lý file CSV, lập trình Shell Script và Python trên hệ điều hành Ubuntu Linux.

---

 Thông tin sinh viên

 **Họ và tên:** Nguyễn Thị Thanh Hằng
 **Mã sinh viên:** 2300491
 **Môn học:** Hệ điều hành
 **Hệ điều hành sử dụng:** Ubuntu Linux

---

 ĐỀ 1 - QUẢN LÝ DOANH THU SẢN PHẨM

 Câu 1: Tạo cấu trúc thư mục

```text
Hang_2300491/
├── Sanpham
│   ├── Doanhthu
│   └── Tong
└── Ngonngu
    ├── shell
    └── Python
```

 Lệnh thực hiện

```bash
mkdir -p ~/Hang_2300491/Sanpham/{Doanhthu,Tong}
mkdir -p ~/Hang_2300491/Ngonngu/{shell,Python}
```

---

 Câu 2: Xử lý dữ liệu doanh thu

Tạo file `doanhthu.csv`

```csv
2026-05-01,Nguyen Van A,Laptop,1500
2026-05-02,Tran Thi B,Mouse,200
2026-05-03,Le Van C,Keyboard,350
2026-05-04,Pham Thi D,Monitor,2500
2026-05-05,Hoang Van E,Printer,1800
```

Trích cột Ngày và Doanh thu

```bash
cut -d',' -f1,4 doanhthu.csv > doanhso.csv
```

 Lấy 2 dòng đầu

```bash
head -n 2 doanhthu.csv > top.csv
```

---

 Câu 3: Ghép dữ liệu doanh thu

Tạo file `doanhthu1.csv`

```csv
2026-05-06,Do Van F,Camera,3200
2026-05-07,Bui Thi G,Speaker,900
2026-05-08,Nguyen Van H,Tablet,2200
```

Ghép file:

```bash
cat doanhthu.csv doanhthu1.csv > tongdoanhthu.csv
```

---

 Câu 4: Shell Script tính tổng doanh thu

File `tinhtong.sh`

```bash
#!/bin/bash

tong=0

while IFS=',' read ngay doanhthu
do
    tong=$((tong + doanhthu))
done < doanhso.csv

echo "Tong doanh thu la: $tong"
```

Cấp quyền thực thi:

```bash
chmod +x tinhtong.sh
```

Chạy chương trình:

```bash
./tinhtong.sh
```

---

 Câu 5: Python Script đếm từ trong chuỗi

File `demtu.py`

```python
chuoi = input("Nhap chuoi: ")

tu = chuoi.split()

print("So tu trong chuoi:", len(tu))

print("Cac tu dai hon 5 ky tu:")

for i in tu:
    if len(i) > 5:
        print(i)
```

Chạy chương trình:

```bash
python3 demtu.py
```

---

 ĐỀ 2 - QUẢN LÝ MÓN ĂN

 Câu 1: Tạo cấu trúc thư mục

```text
Hang_2300491/
├── Monan
│   ├── Thucdon
│   └── danhmuc
└── Ngonngu
    ├── shell
    └── Python
```

 Lệnh thực hiện

```bash
mkdir -p ~/Hang_2300491/Monan/{Thucdon,danhmuc}
mkdir -p ~/Hang_2300491/Ngonngu/{shell,Python}
```

---

 Câu 2: Xử lý dữ liệu món ăn

File `monan.csv`

```csv
Pho,Mon nuoc,40000,Viet Nam
Banh mi,Do an nhanh,25000,Viet Nam
Pizza,Mon Au,120000,Italy
Sushi,Mon song,150000,Japan
Hamburger,Do an nhanh,80000,My
```

Trích cột Tên món và Giá

```bash
cut -d',' -f1,3 monan.csv > giatien.csv
```

 Lấy 3 dòng đầu

```bash
head -n 3 monan.csv > topmon.csv
```

---

 Câu 3: Ghép dữ liệu món ăn

File `monan1.csv`

```csv
Com tam,Mon com,50000,Viet Nam
Mi y,Mon Au,90000,Italy
Tokbokki,Mon cay,70000,Korea
```

Ghép file:

```bash
cat monan.csv monan1.csv > monan2.csv
```

---

 Câu 4: Shell Script thống kê

File `thongke.sh`

```bash
#!/bin/bash

cd ~/Hang_2300491/Monan/danhmuc

so_dong=$(grep -c "Viet Nam" monan2.csv)

echo "So dong chua 'Viet Nam' la: $so_dong"
```

Cấp quyền thực thi:

```bash
chmod +x thongke.sh
```

Chạy chương trình:

```bash
./thongke.sh
```

---

 Câu 5: Python Script tính tổng số chẵn

File `tong.py`

```python
n = int(input("Nhap N: "))

tong = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        tong += i

print("Tong cac so chan tu 1 den", n, "la:", tong)
```

Ví dụ:

```text
Nhap N: 10
Tong cac so chan tu 1 den 10 la: 30
```

---

 Cấu trúc thư mục hoàn chỉnh

```text
Hang_2300491
├── Monan
│   ├── Thucdon
│   │   ├── giatien.csv
│   │   ├── monan.csv
│   │   ├── monan1.csv
│   │   └── topmon.csv
│   └── danhmuc
│       └── monan2.csv
├── Ngonngu
│   ├── Python
│   │   ├── demtu.py
│   │   └── tong.py
│   └── shell
│       ├── thongke.sh
│       └── tinhtong.sh
└── Sanpham
    ├── Doanhthu
    │   ├── doanhso.csv
    │   ├── doanhthu.csv
    │   ├── doanhthu1.csv
    │   └── top.csv
    └── Tong
        └── tongdoanhthu.csv


---

 Kết luận

Thông qua các bài thực hành, sinh viên đã làm quen với việc thao tác trên hệ điều hành Ubuntu Linux như tạo và quản lý thư mục, xử lý dữ liệu CSV bằng lệnh Linux, lập trình Shell Script và Python, đồng thời sử dụng Git và GitHub để quản lý mã nguồn.
