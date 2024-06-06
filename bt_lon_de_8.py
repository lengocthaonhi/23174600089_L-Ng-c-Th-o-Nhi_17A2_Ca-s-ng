#Lê Ngọc Thảo Nhi - DHKL17A2HN

import csv

#1. Tạo 1 list để lưu trữ tên của 15 người tham gia

list_name = []

while True:
        name = input('Nhập tên: ')
        if name == '*':
                break
        list_name.append()

print(f'Danh sách tên của 15 người tham gia: {list_name}')

#2. Tạo 1 set để lưu trữ tên của những người đã được chia vào nhóm

group_set = set()
group_size = 3

for i in range(0, len(list_name), group_size):
        group = list_name[i:i+group_size]
        group_set.update(group)

print(f'Danh sách lưu trữ tên của những người đã được chia vào nhóm: {group_set}')

#3. Tạo một dictionary để lưu trữ số lượng người trong mỗi nhóm

group_dict = {}
for i in range(0, len(list_name), group_size):
        group_dict[f'Nhóm {i//group_size + 1}'] = len(group)

print(f'Số lượng người trong mỗi nhóm: {group_dict}')

#4. Viết các hàm để thực hiện các chức năng chính

#4.1. Chia ngẫu nhiên người tham gia vào các nhóm (3 thành viên/nhóm)
import random

def chia_nhóm(nguoi_tham_gia):
    random.shuffle(nguoi_tham_gia)
    so_luong_nguoi = len(nguoi_tham_gia)
    so_luong_nhóm = so_luong_nguoi // 3
    nhom = [nguoi_tham_gia[i * 3:(i + 1) * 3] for i in range(so_luong_nhóm)]
    return nhom

#4.2. Tính xác suất một người được chia vào một nhóm cụ thể
def xac_suat_cho_nguoi(nguoi, nhom):
    so_luong_nhom_tham_gia = sum(1 for nhom_moi in nhom if nguoi in nhom_moi)
    so_luong_nhom = len(nhom)
    return so_luong_nhom_tham_gia / so_luong_nhom if so_luong_nhom > 0 else 0

#4.3. Hiển thị danh sách nhóm và thành viên trong mỗi nhóm
def hien_thi_danh_sach_nhóm(nhom):
    for i, nhom_moi in enumerate(nhom):
        print(f"Nhóm {i + 1}: {nhom_moi}")

#5. Sử dụng module random để thực hiện việc chia nhóm ngẫu nhiên (đã làm ở ý 1)

#6. Lưu lại kết quả của quá trình chia nhóm vào một file CSV: tên người tham gia, tên nhóm, xác suất được chia vào nhóm
def ghi_vào_csv(nguoi_tham_gia, nhom):
    with open('ket_qua_chia_nhom.csv', mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['Tên người tham gia', 'Tên nhóm', 'Xác suất được chia vào nhóm'])
        for i, nhom_moi in enumerate(nhom):
            for nguoi in nhom_moi:
                xac_suat = xac_suat_cho_nguoi(nguoi, nhom)
                writer.writerow([nguoi, f'Nhóm {i + 1}', xac_suat])