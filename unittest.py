bai14 = '0100,0011,1010,1001'
array = []
ketqua = []
array = bai14.split(',')
for each in array:
    if int(each,2)%5 == 0:
        ketqua.append(each)
print('bai14:', ketqua)