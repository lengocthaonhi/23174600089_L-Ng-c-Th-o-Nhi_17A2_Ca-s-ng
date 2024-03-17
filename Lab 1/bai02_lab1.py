#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 1

#Bài 2. Quản lý thông tin trong thư viện UNETI
so_luong_sach = int(input('Nhập số lượng sách: '))
ma_sach = input('Nhập mã sách: ')
ten_sach = input('Nhập tên sách: ')
tac_gia = input('Nhập tên tác giả: ')
nam_xuat_ban = int(input('Nhập năm xuất bản: '))
print(f'Thư viện ĐHKTKTCN có {so_luong_sach} sách {ten_sach} với mã số {ma_sach}', end = '\n')
print(f'Cuốn sách đó của tác giả {tac_gia} được xuất bản vào năm {nam_xuat_ban}')