#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 1

#Bài 5. Tính tiền phải trả cho việc sử dụng máy lọc không khí
t = input('Nhập thời gian sử dụng: ')
U = 220
I = 1.5
A = (U * I * t) / 1000
gia_ban_dien = 5000
tien_dien = A * gia_ban_dien
print(f'Số tiền điện phải trả: {tien_dien}')