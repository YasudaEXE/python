#Найти в промежутке от «а» до «в» количество простых чисел
a = int(input())
b = int(input())

s = 0 #кол-во

for number in range(a, b + 1): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0: 
                break 
        else: 
            s += 1 
print(s)