#Найти в промежутке от «а» до «в» среднее арифметическое простых чисел.

a = int(input())
b = int(input())

summa = 0
kolvo = 0

for number in range(a, b + 1): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0: 
                break 
        else: 
            summa += number
            kolvo += 1		
print(summa/kolvo)