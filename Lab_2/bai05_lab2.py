#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 2

#Bài 5. Tính tiền phải trả khi mua vé xem phim
nguoi = int(input('Nhập số lượng người xem: '))
if nguoi == 1:
          cost = nguoi * 120000
          print(f'Giá vé cho 1 người là: {cost}')
elif nguoi >= 2 and nguoi < 4:
          cost_giam_1 = nguoi * 120000 * 0.05
          print(f'Giá vé cho từ 2 đến dưới 4 người là: {cost_giam_1}')
elif nguoi >= 4 and nguoi < 10:
          cost_giam_2 = nguoi * 120000 * 0.1
          print(f'Giá vé cho từ 4 đến dưới 10 người là: {cost_giam_2}')
else:
          cost_giam_3 = nguoi * 120000 * 0.2
          print(f'Giá vé cho từ 10 người trở lên là: {cost_giam_3}')