#name = str(input("Họ và tên:"))
#age = int(input("Tuổi:"))
#school = str(input("Trường:"))
#print("Xin chào, tôi là",name,"năm nay tôi", age, "tuổi, đang học tại",school )


#1
name = "Ngô Xuân Chiến"
age = 17
school = "PTIT"
print(f"Xin chào, tôi là {name}, năm nay tôi {age} tuổi, đang học tại {school}.")

#2
chieu_dai = 67
chieu_rong = 36
Chu_vi = 2*(chieu_dai + chieu_rong)
Dien_tich = chieu_dai * chieu_rong
print(Chu_vi)
print(Dien_tich)

#3
C = 36
F = C * 1,8 + 32
print(F)

#4
Toan = 10
Van = 9
Tieng_anh = 9
Avrg = (Toan + Van + Tieng_anh)//3
print(Avrg)

#5
print(f"Tôi tên là {name}, tôi {age} tuổi.")
print(f"Sang năm tôi sẽ {age + 1} tuổi.")

#6
num = 67
if num % 2 == 0:
    print("số chẵn")
else:
    print("số lẻ")

#7
a = 36
b= 18
if a > b:
    print(a)
else:
    print(b)

#8
scr = [0,1,2,3,4,5,6,7,8,9,10]
for num in scr:
    if num >= 8:
        print("Giỏi")
    if 6.5 <= num <= 7.9:
        print("Khá")
    elif 5 <= num <= 6.4:
        print("Trung bình")
    else:
        print("Yếu")

#9
kWh = 150
if 0 <= kWh <= 50:
    print(kWh * 1800)
elif 51 <= kWh <= 100:
    print(kWh * 2000)
else:
    print(kWh * 2500)

#10
year = 2026
if year %4==0 and year %100!=0 or year %400 ==0:
    print("Năm Nhuận")
else:
    print("Không phải năm nhuận")

#11
num = 6
for i in range(1,9):
    print (f"6 * {i} = {num*i}")

#12
n = 367
total=0
for i in range (1,368):
    total= total + i
print(total)

#13
count = 0
for i in range (1,101):
    if i %2 == 0:
        count = count + 1
print(count)

#14
count = 0
while count < 10:
    print("sít rịt =", count)
    count +=1

#15
print ("*")
print("*"*2)
print("*"*3)
print("*"*4)





















