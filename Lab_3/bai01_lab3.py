#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 3

#Bài 1. Tính tổng
S1 = 0
n = int(input('Nhập n: '))
if n <= 0:
          print('Nhập lại')
else:
          for i in range(1, n+1):
                  S1 += i
print(f'S1 = {S1}')

S2 = 0
n = int(input('Nhập n: '))
if n <= 0:
          print('Nhập lại')
else:
          for i in range(1, n+1):
                  S2 += 1/i
print(f'S2 = {S2}')

import math
S3 = 0
n = int(input('Nhập n: '))
if n <= 0:
          print('Nhập lại')
else:
          for i in range(1, n+1):
                    S3 += 1/(math.sqrt(2*i))
print(f'S3 = {S3}')

S4 = 0
n = int(input('Nhập n: '))
if n <= 0:
          print('Nhập lại')