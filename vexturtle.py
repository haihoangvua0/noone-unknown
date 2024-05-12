a = (input("Nhập vào một số: "))

n = 0
b = a[0]

c = a[-1]

c = int(c)
b = int(b)
if c < b:
    print('Số kết thúc CẦN phải lớn hơn số ban đầu')
elif c >= b:
    for i in range(1, 50 + 1):
        if int(a) % 3 == 0 and int(a) % 3 ==0 and int(a) % 5 == 0 and int(a) % 5 == 0:
            print("FizzBuzz")
        elif int(a) % 3 != 0 or int(a) % 3 != 0:
            print("Fizz")
        elif int(a) % 5 != 0 or int(a) % 5 != 0:
            print("Buzz")
        break
else:
    print(a)






