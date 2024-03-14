#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 1

#Bài 6. Viết chương trình nhập tọa độ 2 vector a, b và tính toán
#1. Phép cộng/trừ vector a và b
x1, y1, z1 = map(int, input('Nhập tọa độ vector a: '))
x2, y2, z2 = map(int, input('Nhập tọa độ vector b: '))
x_c = x1 + x2
y_c = y1 - y2
z_c = z1 + z2
print(f'Phép cộng vector a + b: {(x_c, y_c, z_c)}')
x_d = x1 - x2
y_d = y1 - y2
z_d = z1 - z2
print(f'Phép trừ vector a - b: {(x_d, y_d, z_d)}')

#2. Độ dài vector a, độ dài vector b
import math
do_dai_a = math.sqrt(x1 + y1 + z1)
print(f'Độ dài vector a: {do_dai_a}')
do_dai_b = math.sqrt(x2 + y2 + z2)
print(f'Độ dài vector a: {do_dai_b}')

#3. Tính góc giữa 2 vector a và b
import math
tich_vo_huong = x1 * x2 + y1 * y2 + z1 * z2
tich_do_dai = do_dai_a * do_dai_b
cos = (tich_vo_huong / tich_do_dai)
goc = math.acos(cos)
print(f'Góc xen giữa 2 vector a và b: {goc:.2f}')