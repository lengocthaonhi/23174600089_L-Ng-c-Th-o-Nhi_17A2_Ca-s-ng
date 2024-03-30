#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 1

#Bài 10. Tính xác suất các viên bi
#1. Tất cả là bi đỏ
import math
k1 = int(input('Nhập số lượng bi đỏ chọn ngẫu nhiên: '))
bc_1 = math.comb(20,k1)
kgm_1 = math.comb(50,k1)
xs_1 = bc_1 / kgm_1
print(f'Xác suất để lấy ra toàn bộ bi đỏ là: {xs_1:.4f}')

#2. Ít nhất 1 viên bi xanh
k2 = int(input('Nhập số lượng bi vàng chọn ngẫu nhiên: '))
bc_2 = math.comb(15,k2)
bc_do_vang = bc_1 * bc_2
bc_xanh = 1 - bc_do_vang
kgm_2 = math.comb(50,k2)
xs_2 = bc_xanh / kgm_2
print(f'Xác suất để lấy ra toàn bộ bi đỏ là: {xs_2:.4f}')

#3. Đúng 2 viên là bi vàng
k3 = int(input('Nhập số lượng bi vàng chọn ngẫu nhiên: '))
bc_3 = math.comb(15,2) * math.comb(35,k3-2)
kgm_3 = math.comb(50,k3)
xs_3 = bc_3 / kgm_3
print(f'Xác suất để lấy ra toàn bộ bi đỏ là: {xs_3:.4f}')
