#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 1

#Bài 8. Tính giá trị biểu thức
import math
x = float(input('Nhập x: '))
z = float(input('Nhập z: '))
y = ((math.pow(x,2) * math.sin(z) + math.sqrt(abs(x))) / math.log(z) + math.exp(x - 1)) + math.atan(x * z)
print(f'Giá trị biểu thức: {y:.2f}')
