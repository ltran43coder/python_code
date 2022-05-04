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

# bai 52 20Apr2022
# Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính. Circle có một method có thể tính diện tích.
class Circle(object):
    def __init__(self,r):
        self.radius = r
    def dientich(self):
        return 3.14*self.radius**2
tempCircle = Circle(3)
print('bai 52:', tempCircle.dientich())

# bai 53
# Định nghĩa class có tên là Hinhchunhat được xây dựng
# bằng chiều dài và chiều rộng.
# Class Hinhchunhat có method để tính diện tích
class Hinhchunhat(object):
    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong
    def dientich(self):
        return self.dai*self.rong
tempHinhchunhat = Hinhchunhat(2,3)
print('bai 53:', tempHinhchunhat.dientich())

# bai 54
# Định nghĩa một class có tên là Shape và class con là Square.
# Square có hàm init để lấy đối số là chiều dài.
# Cả 2 class đều có hàm area để in diện tích của hình, diện tích mặc định của Shape là 0.
class Shape(object):
    def __init__(self):
        pass
    def dientich(self):
        return 0
class Square(Shape):
    def __init__(self,l):
        Shape.__init__(self)
        self.length = l
    def dientich(self):
        return self.length*self.length
tempSquare = Square(5)
print('bai 54:', tempSquare.dientich())

# bai 55
# Đưa ra một RuntimeError exception.
# cai nay se quang ra exception
# raise RuntimeError('something wrong')
#cach ko quang ca exception , chi quang ra print voi exception
class RuntimeError(Exception):
    def __init__(self, mismatch):
       Exception.__init__(self, mismatch)
try:
    print ("Bai 55a: And now, the Vocational Guidance Counsellor Sketch.")
    raise RuntimeError("Does not have proper hat, let see")
    print ("Bai 55c: This print statement will not be reached.")
except RuntimeError as problem:
    print ("Bai 55b: Vocation problem: {0}".format(problem))

# bai 56 21Apr2022
# Viết hàm để tính 5/0 và sử dụng try/exception để bắt lỗi.
def bai56(num):
    try:
        num/0
    except ZeroDivisionError:
        print('bai 56a: chia mot so cho 0')
    except Exception as problem:
        print('bai 56b: bat duoc mot exception')
    finally:
        print('bai 56c: Phep tinh bi huy')
bai56(10)

# bai 57
# Định nghĩa một class exception tùy chỉnh, nhận một thông báo là thuộc tính.
class myErr(Exception):
    def __init__(self, inmsg):
        self.msg = inmsg
error = myErr('Bai 57: Dien gi vao day')
print(error)

# bai 58
# Giả sử rằng chúng ta có vài địa chỉ email dạng username@companyname.com,
# hãy viết một chương trình để in username của địa chỉ email cụ thể.
# Cả username và companyname chỉ bao gồm chữ cái.
# emailAdd = 'ltran43coder'
# pat2 = "(\w+)@((\w+\.)+(com))"
# re2 = re.match(pat2,emailAdd)
# print (re2.group(1))
# AttributeError: 'NoneType' object has no attribute 'group'

def bai58(email):
    try:
        pat2 = "(\w+)@((\w+\.)+(com))"
        re2 = re.match(pat2, email)
        print('Bai 58:', re2.group(1))
        print('Bai 59:', re2.group(2))
    except AttributeError:
        print('bai 58,59: ',email, ' email khong dung dinh dang')
    except Exception as problem:
        print('bai 58b,59b: bat duoc mot exception')
bai58('ltran43coder@gmail.com')

# bai 60 regex
# Viết một chương trình chấp nhận chuỗi từ được phân tách bằng khoảng trống và in các từ chỉ gồm chữ số.
s = 'Nhu the nao la dung 1, nhu the nao 2 la sai 4'
print (re.findall("\d+",s))
print (re.findall("\w+",s))

# bai 61 ???
# In chuỗi Unicode "Hello world".
unicodeString = u"Thế này là thế nào"
str1 = "Thế này là thế nào"
print(unicodeString)
print(str1)

# bai 62
# Viết chương trình để đọc chuỗi ASCII và chuyển đổi nó sang một chuỗi Unicode được mã hóa bằng UTF-8.
en= str.encode('utf-8')
print(en)
de = en.decode()
print(de)

# bai 64
# Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với một n là số được nhập vào (n> 0).
# Ví dụ, nếu n là số sau đây được nhập vào:
# 5
# Thì đầu ra phải là:
# 3.55
def bai64(num):
    if num<=0:
        return "Vui lòng nhập số > 0"
    else:
        sum= 0.0
        for each in range(1,num+1):
            sum += float(float(each)/(each+1))
        return sum
print('bai 64:',bai64(10))

# bai 65
# Viết chương trình tính: f(n)=f(n-1)+100 khi n>0 và f(0)=1, với n là số được nhập vào (n>0).
# Ví dụ: Nếu n được nhập vào là 5 thì đầu ra phải là 500.
def bai65(num):
    if num < 0:
        return "Vui lòng nhập số >= 0"
    else:
        sum = 0
        if num == 0:
            return 1
        else:
            for each in range(1,num+1):
                sum += 100
            return sum
print('bai 65:', bai65(0))
print('bai 65:', bai65(10))

# bai 66
# Dãy Fibonacci được tính dựa trên công thức sau:
# f(n)=0 nếu n=0
# f(n)=1 nếu n=1
# f(n)=f(n-1)+f(n-2) nếu n>1
# Hãy viết chương trình tính giá trị của f(n) với n là số được người dùng nhập vào.
# Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là 13.
# def f(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return f(n-1)+f(n-2)
def fibo(n):
    result = 0
    if n < 0:
        return -1
    else:
        if n == 0:
            result = 0
        else:
            if n == 1:
                result = 1
            else:
                result = fibo(n-1) + fibo(n-2)
        return result
# 0 1 2 3 4 5 6 7     8   9   10  11  12  13  14  15  16  17  18  19  20
# 0 1 1 2 3 5 8 13    21  34  55  89  144
print('bai 66b:',fibo(12))

# bai 67
# cung fibo nhưng in ra list
# Hãy viết chương trình sử dụng list
# comprehension để in dãy Fibonacci dưới dạng tách biệt bằng dấu ",", n được người dùng nhập vào.
# TypeError: 'str' object is not callable => ko dc viet str = vì str la` 1 ham trong python
n = 12
temp = [str(fibo(x)) for x in range(0, n+1)]
# temp = []
# for x in range(0,n+1):
#     temp.append(str(fibo(x)))
print(",".join(temp))

# bai 68
# Viết chương trình sử dụng generator để in số chẵn trong khoảng từ 0 đến n, cách nhau bởi dấu phẩy, n là số được nhập vào.
# Ví dụ nếu n=10 được nhập vào thì đầu ra của chương trình là: 0,2,4,6,8,10
temp = []
def sochan(n):
    for each in range(0,n+1):
        if each%2 == 0:
            temp.append(str(each))
    print(','.join(temp))
sochan(15)

# bai 69
# Viết chương trình sử dụng generator để in số chia hết cho 5 và 7 giữa 0 và n,
# cách nhau bằng dấu phẩy, n được người dùng nhập vào.
# Ví dụ: Nếu n=100 được nhập vào thì đầu ra của chương trình là: 0,35,70.
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i
values = []
n = 100
for i in NumGenerator(n):
    values.append(str(i))
print ("69 Các số chia hết cho 5 và 7 trong khoảng 0 và n là: ",",".join(values))

# bai 70
# Viết các lệnh assert để xác minh rằng tất cả các số trong list [2,4,6,8] là chẵn.
li = [2,4,6,8,10]
for i in li:
 assert i%2==0

# bai 71
# Viết chương trình chấp nhận biểu thức toán học cơ bản do người
# dùng nhập vào từ bảng điều khiển và in kết quả ước lượng ra ngoài màn hình.
# Ví dụ: Nếu chuỗi sau là đầu vào của chương trình:
# 35 + 3
expression = '34+3-15'
print('bai 71:', expression, '=', eval(expression))

# bai 72
# tim kiem nhi phan
def bin_search(li, element):
    print('Danh sach la:', li)
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1
    if (index == -1):
        return 'Khong tim thay ', element
    else:
        return element, ' nam o vi tri la:', index
li=[2,5,7,19,111,27,222]
print (bin_search(li,11))
print (bin_search(li,222))

# Bài 73:
# Yêu cầu:
# Tạo một số thập phân ngẫu nhiên, có giá trị nằm trong khoảng từ 10 đến 100 bằng cách sử dụng module math của Python.
# Sử dụng random.random() để tạo float ngẫu nhiên trong [0,1].
import random
print ('Bai 73:', random.random()*100)

# bai 74
# random so trong khoang tu 5-95
def bai74():
    result = 0
    rand = random.random()*100
    if rand < 5:
        result = rand + 5
    elif rand > 95:
        result = rand - 5
    else:
        result = rand
    return result
print('bai 74:', bai74())

# bai 75:
# Viết chương trình xuất ra một
# số chẵn/le ngẫu nhiên trong khoảng 0 đến 15 (bao gồm cả 0 và 15), sử dụng module random và list comprehension.
print (random.choice([i for i in range(16) if i%2==0]))
print (random.choice([i for i in range(16) if i%2==1]))

# bai 76
# Vui lòng viết chương trình để xuất một số ngẫu nhiên,
# chia hết cho 5 và 7, từ 0 đến 200 (gồm cả 0 và 200), sử dụng module random và list comprehension.
print (random.choice([i for i in range(201) if i%5==0 and i%7==0]))

# bai 77
# Vui lòng viết chương trình để tạo một list với 3 số ngẫu nhiên từ 100 đến 150.
print (random.sample(range(100,151), 3))

# bai 78
# Viết chương trình tạo ngẫu nhiên list gồm 5 số chẵn nằm trong đoạn [100;150].
print (random.sample([i for i in range(100,151) if i%2==0], 5))

# bai 79
# Viết chương trình để tạo ngẫu nhiên một list gồm 5 số, chia hết cho 5 và 7, nằm trong đoạn [1;1000].
print (random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))

# bai 80
# Viết chương trình để in một số nguyên ngẫu nhiên từ 7 đến 15
print(random.randint(7,16))
print(random.randrange(7,16))

# bai 81
# compress decompress py2
# encode decode p3
import zlib
s = "hello world!hello world!hello world!hello world!"
t = zlib.compress(s.encode("utf-8"))
print (t)
print (zlib.decompress(t))

# bai 82
# Bạn hãy viết một chương trình để in thời gian thực thi (running time of execution) phép tính "1+1" 100 lần.
from timeit import Timer
t = Timer("for i in range(10):1+1")
print (t.timeit())

# bai 83
# Viết chương trình để trộn và in list [3,6,7,8].
# Sử dụng shuffle() để trộn list.
from random import shuffle
li = [3,16,27,38,49]
shuffle(li)
print('bai 83:',li)

# bai 84
# Viết một chương trình để tạo
# tất cả các câu có chủ ngữ nằm trong ["Anh","Em"], động từ nằm trong ["Chơi","Yêu"]
# và tân ngữ là ["Bóng đá","Xếp hình"].
chu_ngu=["Anh","Em"]
dong_tu=["Chơi","Yêu"]
tan_ngu=["Bóng đá","Xếp hình"]
# Code by Quantrimang.com
for i in range(len(chu_ngu)):
    for j in range(len(dong_tu)):
        for k in range(len(tan_ngu)):
            cau = "%s %s %s." % (chu_ngu[i], dong_tu[j], tan_ngu[k])
            print (cau)

# bai 85
# Viết chương trình in list sau khi xóa các số chẵn trong [5,6,77,45,22,12,24].
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2==1]
print(li)

# bai 86
# Sử dụng list comprehension để viết chương trình in list
# sau khi đã loại bỏ các số chia hết cho 5 và 7 trong [12,24,35,70,88,120,155].
li = [12,24,35,70,88,120,155]
li = [x for x in li if not (x%5==0 and x%7==0) ]
print('bai 86:', li)

# bai 87
# Viết chương trình in list sau khi đã xóa số thứ 0, thứ 2, thứ 4, thứ 6 trong [12,24,35,70,88,120,155]
li = [12,24,35,70,88,120,155]
a= [x for i,x in enumerate(li) if i%2!=0]
b= [x for i,x in enumerate(li) if i%2==0]
print ('bai 87a:', a)
print ('bai 87b:', b)

# bai 88
# Viết chương trình tạo mảng 3D 2*3*4 có mỗi phần tử là 1.
bai88 = [[ [1 for col in range(4)] for col in range(3)] for row in range(2)]
print ('bai 88:', bai88)

# bai 89
# Viết chương trình in list sau khi đã xóa số ở vị trí thứ 0, thứ 5,
# trong [12,24,35,70,88,120,155].
li = [12,24,35,70,88,120,155]
a= [x for i,x in enumerate(li) if not (i%5==0)]
print ('bai 89:', a)

# bai 90
# Viết chương trình in list sau khi đã xóa giá trị 24 trong [12,24,35,24,88,120,155].
li = [12,24,35,24,88,24,155]
a= [x for x in li if (x!=24)]
print ('bai 90:', a)

# bai 91
# Với 2 list cho trước: [1,3,6,78,35,55] và [12,24,35,24,88,120,155],
# viết chương trình để tạo list có phần tử là giao của 2 list đã cho.
list1=set([12,3,6,78,35,55,120,1])
list2=set([12,24,35,24,88,120,155,1])
list1 &= list2
li=list(list1)
print ('bai 91:', li)

# bai 92
# Viết chương trình in list từ list [12,24,35,24,88,120,155,88,120,155], sau khi đã xóa hết các giá trị trùng nhau.
def xoaTrung( li ):
    list_moi=[]
    xem = set()
    for i in li:
        if i not in xem:
            xem.add( i )
            list_moi.append(i)
    return list_moi
li=[12,12,15,24,35,35,24,88,120,155,88,120,155]
print ("Bai 92: List sau khi xóa giá trị trùng là:",xoaTrung(li))

# bai 93
# Định nghĩa class Nguoi và 2 class con của nó: Nam, Nu.
# Tất cả các class có method "getGender" có thể in "Nam" cho class Nam và "Nữ" cho class Nu.
class Nguoi(object):
    def getGender(self):
        return "Unknown"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
aNam = Nam()
aNu= Nu()
print (aNam.getGender())
print (aNu.getGender())

# bai 94
# Viết chương trình đếm và in số ký tự của chuỗi do người dùng nhập vào.
dic = {}
chuoi="chuoi la gi"
for c in chuoi:
    dic[c] = dic.get(c,0)+1
print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

# bai 95
# Viết chương trình nhận chuỗi đầu vào từ giao diện điều khiển và in nó theo thứ tự ngược lại.
# Ví dụ nếu chuỗi nhập vào là:
# i love you
# Thì kết quả đầu ra là:
# uoy evol i
chuoi = "baba yeu me va lila nhat tren doi"
chuoi = chuoi[::-1]
print (chuoi)

# bai 96
# Viết chương trình nhận chuỗi do người dùng nhập vào và in các ký tự có chỉ số chẵn.
# Ví dụ: Nếu chuỗi sau được nhập vào: q1u2a3n4t5r6i7m8a9n4g5.6c7o8m, thì đầu ra sẽ là: quantrimang.com.
# Sử dụng list[::2] để lặp list cách 2 vị trí.
chuoi = "q1u2a3n4t5r6i7m8a9n4g5.6c7o8mabcd"
chuoi = chuoi[::2]
print (chuoi)

# bai 97
# Viết chương trình in tất cả các hoán vị của [1,2,3].
import itertools
print (list(itertools.permutations([1,2,3])))

# bai 98
# Viết chương trình để giải 1 câu đố cổ của Trung Quốc:
# Một trang trại thỏ và gà có 35 đầu, 94 chân, hỏi số thỏ và gà là bao nhiêu?
# pp vet can
def giai(dau,chan):
    klg='Không có dáp án phù hợp!'
    for i in range(dau+1):
        tho=dau-i
        if 2*i+4*tho==chan:
            return i,tho
    return klg,klg
dau=35
chan=94
dap_an=giai(dau,chan)
print (dap_an)

# 101 time, 104
# Trả về ngày giờ hiện tại với format dd-mm-yyyy
from datetime import datetime
toda = datetime.today()
tod = toda.strftime('%d-%m-%Y')
year1 = toda.year
month1 = toda.month
day1 = toda.day
print('101 toda:', toda)
print('101 tod:', tod)
# co gi ben trong datetime
print(dir(datetime))

# cap nhat date
from datetime import date
a = date(2022, 4, 30)
print('102 date:', a)

# date from timestamp
timestamp = date.fromtimestamp(1551916800)
print("103 Date =", timestamp)

# 105 in gio phut giay
from datetime import time
a = time(11, 34, 56)
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)
from datetime import datetime
#datetime được truyền ở dạng 'year, month, day'.
a = datetime(2019, 3, 7)
print(a)
# datetime được truyền ở dạng 'year, month, day, hour, minute, second, microsecond'
b = datetime(2019, 3, 7, 23, 55, 59, 342380)
print(b)

# bai 106 2May2022
# Khoảng thời gian chênh lệch giữa 2 đối tượng timedelta
from datetime import timedelta
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("bai 106 t3 =", t3)

# 107 Xử lý timedelta mang giá trị âm
t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2
print("t3 =", t3)
print("t3 =", abs(t3))

# chuyen doi theo giay 108
t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("tong so giay =", t.total_seconds())

# dinh dang datetime 109
from datetime import datetime
# ngày giờ hiện tại
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# định dạng mm/dd/YY H:M:S
print("s1:", s1)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# định dạng dd/mm/YY H:M:S
print("s2:", s2)

# strptime() - phân tích một string thành thời gian 110
from datetime import datetime
date_string = "30 MAy, 2022"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# 111 4May2022
# mui gio
from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

# xu ly bo qua loi bang lenh pass 112
def add(a, b):
    try:
        print('bai 112: ',a + b)
    except Exception as e:
        pass
        print("bai 112: co loi nhung bo qua")
add(11, 1)
add("x", 1)

# list comprehension
# code dai chuyen thanh 1 dong code
letters = ['a', 'b', 'c', 'd']
print(letters)
upper_letters = []
for letter in letters:
    result = letter.upper()
    upper_letters.append(result)
print('112 dai: ', upper_letters)

upper_letters = [x.upper() for x in letters]
print('112 ngan hon:', upper_letters)

# List Comprehension rất tuyệt nhưng không phải
# trường hợp nào cũng có thể sử dụng nó. Bạn không nên sử dụng nó khi có nhiều hơn một điều kiện.

# letters = ['a', 'b', 'c', 'd', 2]
# print(letters)
# upper_letters = [x.upper() for x in letters]
# print(upper_letters)

# se bao loi
# day la cach chuyen thanh code work ko loi
letters = ['a', 'b', 'c', 'd', 1]
print(letters)
upper_letters = []
for letter in letters:
    try:
        result = letter.upper()
        upper_letters.append(result)
    except AttributeError:
        pass # do nothing
print(upper_letters)





























