#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 5

#Bài 8
chuoi = input('Nhập chuỗi có 10 ký tự: ')
from_2_to_8 = chuoi[1:7]
from_5_to_9 = chuoi[4:8]
chuoi_3_ky_tu_cuoi = chuoi[8:]
chuoi_thuong = chuoi.lower()
chuoi_hoa = chuoi.upper()
chuoi_nguoc = chuoi[::-1]
print(f'Trích chuỗi ký tự con từ 2 đến 8: {from_2_to_8}')
print(f'Trích chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5: {from_5_to_9}')
print(f'Trích chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự: {chuoi_3_ky_tu_cuoi} ')
print(f'Chuyển đổi các ký tự trong chuỗi thành chữ thường: {chuoi_thuong}')
print(f'Chuyển đổi các ký tự trong chuỗi thành chữ hoa: {chuoi_hoa}')
print(f'Đảo ngược chuỗi ký tự: {chuoi_nguoc}')