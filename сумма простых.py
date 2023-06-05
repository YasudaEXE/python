# Найти в промежутке от «а» до «в» сумму простых чисел.1

a = int(input())
b = int(input())

s = 0 #кол-во

for number in range(a, b + 1): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0: 
                break 
        else: 
            print(number)
            s += number
print(s)


			