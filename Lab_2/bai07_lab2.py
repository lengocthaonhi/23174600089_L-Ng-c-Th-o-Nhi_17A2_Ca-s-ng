#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 2

#Bài 7. Tính chỉ số BMI
import math
height = float(input('Nhập chiều cao: '))
weight = float(input('Nhập cân nặng: '))
BMI = weight / (math.pow(height,2))
if BMI < 18.5:
          print('Gầy')
elif BMI >= 18.5 and BMI <= 24.9:
          print('Bình thường')
elif BMI >= 25 and BMI <= 29.9:
          print('Hơi béo')
else:
          print('Béo')