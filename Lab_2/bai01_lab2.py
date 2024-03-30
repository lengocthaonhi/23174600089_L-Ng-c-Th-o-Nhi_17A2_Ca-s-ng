#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 2

#Bài 1. Giải và biện luận phương trình
a, b = map(int, input('Nhập hệ số a và b: ').split(', '))
if a == 0:
          if b == 0:
                  print('Phương trình có vô số nghiệm')
          else:
                  print('Phương trình vô nghiệm')
else:
          if b == 0:
                  print('Phương trình có nghiệm = 0')
          else:
                  print(f'Phương trình có nghiệm duy nhất x = {-b/a}')