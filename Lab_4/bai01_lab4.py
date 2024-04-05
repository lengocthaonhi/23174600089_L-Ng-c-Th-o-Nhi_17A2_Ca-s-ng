#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 4

#Bài 5
while True:
          a,b = map(int, input('Nhập a và b: ').split())
          tong = a + b
          hieu = a - b
          tich = a * b
          thuong = a / b
          luy_thua = a ** b
          can_bac_hai_a = a ** 0.5
          can_bac_hai_b = b ** 0.5
          print(f'Tổng: {tong}')
          print(f'Hiệu: {hieu}')
          print(f'Tích: {tich}')
          print(f'Thương: {thuong}')
          print(f'Lũy thừa: {luy_thua}')
          print(f'Căn bậc 2 của a: {can_bac_hai_a}')
          print(f'Căn bậc 2 của b: {can_bac_hai_b}')
          cont = input('Bạn có muốn tiếp tục không? (y/n): ')
          if cont == 'n' or cont == 'N':
                  break

