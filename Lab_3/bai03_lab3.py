#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 3
#e. Tổng các số ngũ giác trong [1, 200]
tong_ngu_giac = 0
n = int(input('Nhập n: '))
if n <= 0:
          print('Nhập lại')
else:
          for i in range(1, 201):
                    Pn = n * (3 * n - 1) / 2
                    tong_ngu_giac += Pn
print(f'Tổng các số ngũ giác: {tong_ngu_giac}')