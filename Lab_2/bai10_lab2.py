#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 2

#Bài 10. Lựa chọn các thể loại phim
choose = input('Chọn thể loại phim: ')
time = input('Chọn thời gian muốn xem phim: ')
if time == 'tối':
          if choose == 'Phim tình cảm':
                  print('Phim tình cảm')
          else:
                  print('Phim kinh dị')
elif time == 'sáng' and time == 'trưa':
          print('Phim hoạt hình')
else:
          print('Không có suất chiếu')
