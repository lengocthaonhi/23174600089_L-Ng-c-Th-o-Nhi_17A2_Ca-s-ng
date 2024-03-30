#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 2

#Bài 8. Ktra vị trí tương đối của 2 đường thẳng
#Bài này tương tự như bài giải hệ phương trình bậc nhất 2 ẩn
a1, b1, c1 = map(int, input('Nhập a1, b1, c1: '))
a2, b2, c2 = map(int, input('Nhập a2, b2, c2: '))
if (a2 / a1) == (b2 / b1) == (c2 / c1):
          print('Hai đường thẳng này trùng nhau')
elif (a2 / a1) == (b2 / b1) != (c2 / c1):
          print('Hai đường thẳng này song song')
else:
          print('Hai đường thẳng này cắt nhau')