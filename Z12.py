# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a=[2, 3, 4, 5, 6]

def mult_p(a):
    mult=[]
    if len(a)%2!=0: #проверяем условие нечетности количества элементов в списке
        l=len(a)//2+1 # выборка чисел будет происходить  из длинны нечетного списка
    else:
        l=len(a)//2 # выборка чисел будет происходить  из длинны четного списка

    
    for i in range(l):
        m=a[i]*a[len(a)-i-1] #находим произведение пар чисел 
        mult.append(m) # добавляем их в новый список.

    return mult

print(mult_p(a))