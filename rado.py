import random
n = random.randint(1, 30)

a = input("bạn nghĩ mình nói số gì?")
if int(a)== n:
    print("Đúng rồi")
b = 0
while a != n:
    if float(a) < n:
        a = input("Nhỏ quá  ")
    if float(a) > n:
        a = input("Lớn quá  ")
    b += 1
    if b > 9:
        break
