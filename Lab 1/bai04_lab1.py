#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 1

#Bài 4. Tính diện tích xung quanh, diện tích toàn phần và thể tích của hình chóp tứ giác đều (hình chóp vuông)
import math
a = float(input('Nhập độ dài cạnh đáy: '))
h = float(input('Nhập chiều cao: '))
S_xq = (4 * a * h) / 3
print(f'Diện tích xung quanh: {S_xq}')
S_tp = S_xq + math.pow(a,2)
print(f'Diện tích toàn phần: {S_tp}')
V = (math.pow(a,2) * h) * 1/3
print(f'Thể tích: {V}')
