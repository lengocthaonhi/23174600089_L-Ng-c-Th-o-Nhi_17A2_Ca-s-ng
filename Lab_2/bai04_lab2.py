#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Bài thực hành lab 2

#Bài 4. Thông báo điểm số
mark = float(input('Nhập điểm: '))
if mark >= 0 and mark < 5:
        print('Điểm kém')
elif mark >= 5 and mark < 7:
        print('Điểm trung bình')
elif mark >= 7 and mark < 8.5:
        print('Điểm khá')
elif mark >= 8.5 and mark <= 10:
        print('Điểm tốt')
else:
        print('Nhập lại điểm')