#Задание 1

def delenie(arg1, arg2):
    try:
        formula = arg1 // arg2
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    print(arg1)
    print(arg2)

    return formula

print(delenie(arg1 = int(input("Введите делимое:")), arg2 = int(input("Введите делитель:"))))

#Задание 2

def info (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(info(surname = 'Bondarenko', name = 'Anna', year = '1996', city = 'Moscow', email = 'aaaaa@mail.ru', telephone = '89009999999'))

#Задание 3

def my_func(arg1 , arg2, arg3):
    a = [arg1, arg2, arg3]
    a.remove(min(a))
    return sum(a)

print(my_func(int(input("arg1 = ")), int(input("arg2 = ")), int(input("arg3 = "))))

#Задание 4
#1 способ

def my_func(x, y):
    return x ** abs(y)
#2 способ

def my_func(x,y):
    y = abs(y)
    res = pow(x,y)
    return res

print(my_func(float(input("Первое значение - ")), int(input("Второе значение - "))))

#Задание 5
def summa ():
    summa_res = 0
    a = False
    while a == False:
        numb = input('введите числа через пробел или * - для выхода ').split()
        res = 0
        for el in range(len(numb)):
            if numb[el] == '*':
                a = True
                break
            else:
                res = res + int(numb[el])
        summa_res = summa_res + res
        print(f'сумма = {summa_res}')
    print(f'общая сумма = {summa_res}')
summa()

#Задание 6
def func(text):
    return text.title()

print(func("lalala lalal"))
