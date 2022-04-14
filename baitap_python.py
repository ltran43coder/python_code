from operator import itemgetter
import re
#B1 Viết chương trình tìm tất cả các số chia hết cho 7
# nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200).
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

# j = []
# for each in range(2000,3200):
#     if (each % 7 == 0) and (each % 5 != 0):
#         j.append(str(each))
# print(','.join(j))

#B2 Viết một chương trình có thể tính giai thừa của một số cho trước.
# Kết quả được in thành chuỗi trên một dòng,
# phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320
import math

n = 8
ketqua = 1
for each in range(1,n+1):
    ketqua = ketqua * each
print('bai2 giai thừa của n=:', n, " là:", ketqua)

# x=int(input("Nhập số cần tính giai thừa:"))
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
# print (fact(x))

# b3 Với số nguyên n nhất định, hãy viết chương trình để tạo ra
# một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.
# Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

# x=int(input("Nhập số cần thực hiện:"))
# result = dict()
# for each in range(1,x+1):
#     result[each]=each*each
# print(result)

# Bài 04:
# Viết chương trình chấp nhận một chuỗi số,
# phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
# Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Gợi ý:Viết lệnh yêu cầu nhập vào các giá trị sau đó dùng quy tắc chuyển đổi kiểu dữ liệu để hoàn tất.
chuoi =' 34, 67, aaaa, 33,    12,   98  '
result = []
def stringToList(string):
    # listRes = list(string.split(","))
    listRes = string.split(",")
    for ind in range(0,len(listRes)):
        # print(listRes[ind].isnumeric())
        if listRes[ind].strip().isnumeric() == True:
            result.append(listRes[ind].strip())
    return result
print('b4: ',stringToList(chuoi.strip()))

# bài 5: hàm có 3 phuong thuc
# class InputOutString(object):
#    def __init__(self):
#        self.s = ""
#
#    def getString(self):
#        self.s = input("Nhập chuỗi:")
# # Code by Quantrimang.com
#    def printString(self):
#        print (self.s.upper())
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()

# bai 6: Viết một method tính giá trị lap phương của một số.
so = 2.2
def lapphuong(num):
    return so**3
print("bai6:", lapphuong(so))

# Bài 09:
# Viết chương trình và in giá trị theo công thức cho trước:
# Q = √([(2 * C * D)/H]) (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
# Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến,
# được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.
# Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.
day = [100,150,180]
result = []
def bai9(num):
    return math.sqrt((2*50*num)/30)
for each in day:
    result.append(bai9(each))
print("bai9:", result)

# bai 11
# Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào,
# phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo
# thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
chuoi = 'chuoi,can,nhap1,biet,nhap2,gi,day,ban,hoi'
temp = []
temp = chuoi.split(',')
temp.sort()
print('bai11:', temp)

# bai 12
# Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào,
# chuyển các dòng này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là
chuoi12 = 'Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào'
def inhoa(input):
    return chuoi12.upper()
print('bai12:', inhoa(chuoi12))

# bai 13
# Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng,
# loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.
# Giả sử đầu vào là: hello world and practice makes perfect and hello world again
# Thì đầu ra là: again and hello makes perfect practice world
chuoi13 = 'hello world and practice makes perfect and hello world again'
new_menu = chuoi13.split(' ')
final_new_menu = list(set(new_menu))
final_new_menu.sort()
print('bai13:', final_new_menu)

# bai 14
# Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số,
# phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không.
# Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
# Ví dụ đầu vào là: 0100,0011,1010,1001
# Đầu ra sẽ là: 1010
bai14 = '0100,0011,1010,1001'
array = []
ketqua = []
array = bai14.split(',')
for each in array:
    if int(each,2)%5 == 0:
        ketqua.append(each)
print('bai14:', ketqua)

# bai 15
# Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này)
# sao cho tất cả các chữ số trong số đó là số chẵn.
# In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
bai15 = []
for each in range(1000,3001):
    if each%2==0:
        bai15.append(str(each))
print('bai15:', ','.join(bai15))

# bai 16
# Viết một chương trình chấp nhận đầu vào là một câu,
# đếm số chữ cái và chữ số trong câu đó.
# Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
# Thì đầu ra sẽ là:
# Số chữ cái là: 10
# Số chữ số là: 3
bai16 = 'hello world! 123'
sonum = 0
sostring = 0
for each in bai16:
    if each.isnumeric():
        sonum += 1
    if each.isalpha():
        sostring += 1
print('bai16 sonum=',sonum)
print('bai16 sostring=',sostring)

# bai17
# Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
# Giả sử đầu vào là: Quản Trị Mạng
# Thì đầu ra là:
# Chữ hoa: 3
# Chữ thường: 8
input17 = 'Quản Trị Mạng 9'
outputchuhoa = 0
outputchuthuong = 0
for each in input17:
    if each.islower():
        outputchuthuong +=1
    if each.isupper():
        outputchuhoa +=1
print('bai17 chuahoa-chuthuong:', outputchuhoa,'-',outputchuthuong)

# bai 18
# Viết một chương trình tính giá trị của a+aa+aaa+aaaa với
# a là số được nhập vào bởi người dùng.
# Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234
input17 = 2
n1 = int( "%s" % input17 )
n2 = int( "%s%s" % (input17,input17) )
n3 = int( "%s%s%s" % (input17,input17,input17) )
n4 = int( "%s%s%s%s" % (input17,input17,input17,input17) )
output18 = n1+n2+n3+n4
print('bai18:', output18)

# bai 19
# Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.
# Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
input19 = '1,2,3,4,5,6,7,8,9'
output19 = []
list1 = input19.split(',')
for each in list1:
    if int(each) % 2 > 0:
        output19.append(each)
# numbers = [x for x in values.split(",") if int(x)%2!=0]
print('bai19:', ','.join(output19))

# bai 21
# Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký.
# Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.
# Các tiêu chí kiểm tra mật khẩu bao gồm:
# 1. Ít nhất 1 chữ cái nằm trong [a-z]
# 2. Ít nhất 1 số nằm trong [0-9]
# 3. Ít nhất 1 kí tự nằm trong [A-Z]
# 4. Ít nhất 1 ký tự nằm trong [$ # @]
# 5. Độ dài mật khẩu tối thiểu: 6
# 6. Độ dài mật khẩu tối đa: 12
# Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy
# và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không.
#     Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.
# Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345
# Thì đầu ra sẽ là: ABd1234@1
input21 = 'ABd1234@1,a F1#,2w3E*,2#We3345'
mang = input21.split(',')
output21 = []
for each in mang:
    if len(each) < 6 or len(each) > 12:
        continue
    else:
        pass
    if not re.search("[a-z]", each):
        continue
    elif not re.search("[0-9]", each):
        continue
    elif not re.search("[A-Z]", each):
        continue
    elif not re.search("[$#@]", each):
        continue
    elif re.search("\s", each):
        continue
    else:
        pass
    output21.append(each)
print('bai 21:',",".join(output21))

# bai 22
# Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần,
# name là string, age và height là number.
# Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp là:
# Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm.
# Nếu đầu vào là:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Thì đầu ra sẽ là:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


# bai 23
# Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j
for i in putNumbers (30):
     print (i)

# bai 25
# Viết chương trình tính tần suất các từ từ input. Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.
# Giả sử input là: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
input25 = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
freq = {}
for word in input25.split():
    freq[word] = freq.get(word,0)+1
words = sorted(freq.keys())
for w in words:
    print("%s:%d" % (w,freq[w]))


# bai 26
# Định nghĩa 1 hàm với 2 số là đối số. Bạn có thể tính tổng trong hàm và trả về giá trị.
def tinhtong(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1+num2
    else:
        return None
print('bai 26.a:', tinhtong(3,4))
print('bai 26.b:', tinhtong('3',4))

# bai 27
# Định nghĩa một hàm có thể chuyển số nguyên thành chuỗi và in nó ra giao diện điều khiển
def chuyendoisothanhchuoi(num):
    if isinstance(num,int):
        return str(num)
    else:
        return None
print('bai 27:', chuyendoisothanhchuoi(78))

# bai 28:
# Định nghĩa hàm có thể nhận hai số nguyên trong dạng chuỗi và tính tổng của chúng, sau đó in tổng ra giao diện điều khiển.
def tinhtong28(num1, num2):
    if isinstance(num1, str) and isinstance(num2, str):
        return int(num1)+int(num2)
    else:
        return None
print('bai 28.a:', tinhtong28('3',4))
print('bai 28.b:', tinhtong28('31','41'))

# bai 29
# Định nghĩa hàm có thể nhận 2 chuỗi từ input và nối chúng sau đó in ra giao diện điều khiển
def noichuoi(chuoi1,chuoi2):
    return chuoi1+chuoi2
print('bai 29:', noichuoi('noi the nao ','123 duoc chua'))

# bai 30: lay chieu dai chuoi > len()

# bai 31: tim so chan le > %2

# bai 32:
# Định nghĩa một hàm có thể in dictionary chứa key là các số từ 1 đến 3
# (bao gồm cả hai số) và các giá trị bình phương của chúng.
def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print ('bai 32:', d)
printDict()

# bai 33
# Định nghĩa một hàm có thể in dictionary chứa các key là số từ 1 đến 20 (bao gồm cả 1 và 20)
# và các giá trị bình phương của chúng.
# > for range(1,21) và dict, **2

# bai 34:
# giống bài 33 nhưng chỉ in key
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for (k,v) in d.items():
       print (v)
printDict()

# bai 37
# Định nghĩa một hàm có thể tạo list chứa các giá trị bình phương
# của các số từ 1 đến 20 (bao gồm cả 1 và 20) và in 5 mục đầu tiên trong list.
def bai37():
    # TypeError: 'list' object is not callable => []
    lamlist = []
    for each in range(1,21):
        lamlist.append(each**2)
    print('bai 37: ', lamlist[:5])
bai37()

# bai 38
# Định nghĩa một hàm có thể tạo ra list chứa các giá trị
# bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20),
# rồi in 5 mục cuối cùng trong list.
def bai38():
    list38 = []
    for each in range(1, 21):
        list38.append(each ** 2)
    print('bai 38: ', list38[-5:])
bai38()

# bai 39:
# Định nghĩa một hàm có thể tạo list chứa giá trị bình phương
# của các số từ 1 đến 20 (bao gồm cả 1 và 20). Sau đó in tất cả
# các giá trị của list, trừ 5 mục đầu tiên.

# bai 39b: in tru 5 muc cuoi cung
def bai39():
    list39 = []
    for each in range(1, 21):
        list39.append(each ** 2)
    print('bai 39a: ', list39[5:])
    print('bai 39b: ', list39[:-5])
bai39()

# bai 40
# Định nghĩa 1 hàm có thể tạo và in một tuple chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20).
def bai40():
    li=[]
    for i in range(1,21):
        li.append(i**2)
    print('bai 40:', tuple(li))
bai40()

# bai 41
# Với tuple (1,2,3,4,5,6,7,8,9,10) cho trước,
# viết một chương trình in một nửa số giá trị đầu tiên trong 1 dòng và 1 nửa số giá trị cuối trong 1 dòng.
tp=(1,2,3,4,5,6,7,8,9,10,11,12)
dodai = int(len(tp)/2) #phai convert tu fload sang int
print('bai 41a:', tp[:dodai])
print('bai 41b:', tp[dodai:])

# bai 42
# Viết một chương trình để tạo tuple khác, chứa các giá trị là số chẵn trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước.
# tao li, for append li, tao tuple voi li vua tao
tp1=(1,2,3,4,5,6,7,8,9,10,11,12)
bai42=[]
for each in tp1:
    if each%2 == 0:
        bai42.append(each)
print('bai 42:', tuple(bai42))

# bai 44
# Viết một chương trình Python nhận chuỗi nhập
# vào bởi người dùng, in "Yes" nếu chuỗi là "yes" hoặc "YES" hoặc "Yes", nếu không in "No"
# s = input ("bai 44: Nhập chuỗi: ")
# if s.lower() == 'yes':
#     print('YES')
# else:
#     print('NO')

# bai 45
# Viết chương trình Python có thể lọc các số chẵn trong danh sách sử dụng hàm filter.
# Danh sách là [1,2,3,4,5,6,7,8,9,10].
bai45 = [1,2,3,4,5,6,7,8,9,10]
result45a = filter(lambda x: x%2==0, bai45)
result45b = filter(lambda x: x%2==1, bai45)
print('bai 45a:', list(result45a))
print('bai 45b:', result45b)

# bai 46
# giong bai 45 nhung dùng map
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = list(map (lambda x: x ** 2, li))
print ('bai 46:', squaredNumbers)

# ko su dung list = ..... se bao loi TypeError: 'list' object is not callable

# bai 47:
# Viết chương trình Python dùng map() và filter() để tạo list
# chứa giá trị bình phương của các số chẵn trong [1,2,3,4,5,6,7,8,9,10]
li47 = [1,2,3,4,5,6,7,8,9,10]
mang47 = filter(lambda x: x%2==0, li47)
result47a = list(map(lambda x: x**2, mang47))
print ('bai 47:', result47a)

# bai 48:
# Viết chương trình Python dùng filter() để tạo danh sách chứa các số chẵn trong đoạn [1,20].
li48 = []
for each in range(1,21):
    li48.append(each)
mang48 = filter(lambda x: x%2==0, li48)
print ('bai 48:', list(mang48))

# bai 49
# Viết chương trình Python sử dụng map() để tạo list
# chứa giá trị bình phương của các số trong đoạn [1,20].
mang49 = map(lambda x: x**2, range(1,21))
print ('bai 49:', list(mang49))

# bai 50
# Định nghĩa một class có tên là Vietnam, với static method là printNationality.

class Vietnam (object):
    @staticmethod
    def printNationality ():
        print ("Vietnam")
VietnamVodich = Vietnam ()
VietnamVodich.printNationality ()
Vietnam.printNationality()

# bai 51:
# Định nghĩa một class tên Vietnam và class con của nó là Hanoi.
class Vietnam(object):
    pass
class Hanoi(Vietnam):
    pass
VietnamVodich = Vietnam()
NguoiHanoi = Hanoi()
















