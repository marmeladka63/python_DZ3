#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number=int(input("Введите число: "))

def bins(number):
    bnum=''
    while number > 0:
        bnum=str(number%2)+bnum
        number=number//2
    return bnum
print(bins(number))

#Получение с помощью встроеной функции
print(bin(number))