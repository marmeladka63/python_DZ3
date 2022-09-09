#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number=int(input("Введите число: "))

def bins(number):
    bnum=''
    while number > 0:
        bnum=str(number%2)+bnum #записывает отстаток от деления в строку
        number=number//2
    return bnum
print(bins(number))

#Получение с помощью встроеной функции
print(bin(number))