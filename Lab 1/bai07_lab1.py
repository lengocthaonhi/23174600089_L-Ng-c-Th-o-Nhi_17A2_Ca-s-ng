#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 1

#Bài 7. Giải HPT bậc nhất 2 ẩn
a1, b1, c1 = map(int, input('Nhập hệ số a, b, c cho pt thứ 1: '))
a2, b2, c2 = map(int, input('Nhập hệ số a, b, c cho pt thứ 2: '))
d = a1 * b2 - a2 * b1
dx = c1 * b2 - c2 * b1
dy = a1 * c2 - a2 * c1
x = dx / d 
y = dy / d
print(f'Hệ phương trình có 2 nghiệm là {x} và {y}')
