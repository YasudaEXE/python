#Найти в промежутке от «а» до «в» сумму, произведение чисел, кратных «с».
print("Введите а")
a = int(input())
print("Введите b")
b = int(input())
print("Введите c")
c = int(input())

s = 1 # произведение
k = 0 # сумма

for number in range(a, b + 1):
    if number % c == 0:
        s *= number
        k += 1
print("Произведение: ",s, "Сумма: ",k)
