#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 3

#Bài 2.
#a. Tính tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000
S_a = 0
for i in range(2000, 4001):
          if (i % 7 == 0) and (i % 5 != 0):
                  S_a += i
print(f'Sa = {S_a}')

#b. Tính tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoảng từ 500 đến 1000
S_b = 0
for i in range(500, 1001):
          if (i % 4 == 0) and (i % 6 != 0):
                  S_b += i
print(f'Sb = {S_b}')