#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 1

#Bài 3. Thực hiện tính toán vốn đầu tư
print('1. Tính toán số tiền sẽ có sau 5 năm')
import math
tien_ban_dau = 10000
lai_suat_hang_nam = 0.06
amount_after_5_years = math.pow((tien_ban_dau * (1 + lai_suat_hang_nam)),5)
print(f'Số tiền có sau 5 năm: {amount_after_5_years}')

print('2. Tính toán số tiền sẽ có sau 10 năm')
import math
tien_ban_dau = 10000
lai_suat_hang_nam = 0.06
amount_after_10_years = math.pow((tien_ban_dau * (1 + lai_suat_hang_nam)),10)
print(f'Số tiền có sau 10 năm: {amount_after_10_years}')

print('3. Tỷ lệ tăng trưởng của số tiền sẽ có sau 10 năm so với số tiền sẽ có sau 5 năm')
growth_rate = (amount_after_10_years - amount_after_5_years) / amount_after_5_years
print(f'Tỷ lệ tăng trưởng: {growth_rate}')
