#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 1

#Bài 9. Tính và in ra tọa độ trung điểm
x1, y1 = map(int, input('Nhập tọa độ đỉnh M: '))
x2, y2 = map(int, input('Nhập tọa độ đỉnh N: '))
x3, y3 = map(int, input('Nhập tọa độ đỉnh P: '))
x4, y4 = map(int, input('Nhập tọa độ đỉnh Q: '))
x_mn = (x1 + x2) / 2
x_np = (x2 + x3) / 2
x_pq = (x3 + x4) / 2
x_qm = (x4 + x1) / 2
y_mn = (y1 + y2) / 2
y_np = (y2 + y3) / 2
y_pq = (y3 + y4) / 2
y_qm = (y4 + y1) / 2
print(f'Tọa độ trung điểm MN: {(x_mn, y_mn)}')
print(f'Tọa độ trung điểm NP: {(x_np, y_np)}')
print(f'Tọa độ trung điểm PQ: {(x_pq, y_pq)}')
print(f'Tọa độ trung điểm QM: {(x_qm, y_qm)}')