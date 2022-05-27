#  1. ++++++++
print('Задача 1 => Найти сумму чисел списка стоящих на нечетной позиции')

print ('Пример:  [1,2,3,4] -> 6')

print ('Пример:  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12')
print()
print ('ПЕРВЫЙ ВАРИАНТ') 
rosters =  list(map(int, input("Введите список состоящий из чисел через пробел:\n").split()))

def Sum_Index(l1st):
    s = 0
    for i in range(len(l1st)):
        if i % 2 != 0:
            s += l1st[i]
    return s

print(f'Сумма чисел списка стоящих на нечетных позициях = {Sum_Index(rosters)}')
print()
print ('ВТОРОЙ ВАРИАНТ') 

A =  int(input("Введите число A для создания списка (от A до N):\n"))
N =  int(input("Введите число N для создания списка (от A до N):\n"))
B =  int(input("Введите число шага в списке (от A до N):\n"))

rosters = list(range(A, N+1, B))

print(rosters) 
print()
def sum_odd_position(mylist):
    return sum(mylist[1::2])

print(f'Сумма чисел списка стоящих на нечетных позициях = {sum_odd_position(rosters)}') 
print()
# # #================================ Для справки ================
# # text = '0123456789'
# # print(text[1::2]) # 13579
# # print(text[2::2]) # 2468  # ==================
# # ====================================================

# 2. ++++++++
print('Задача 2 => Найти произведение пар чисел в списке. ') 
print('Парой считаем первый и последний элемент, второй и предпоследний и т.д.') 

print('Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; ') 
print(' [2, 3, 5, 6] => [12, 15] ')      
print()
print('Первый способ: ')

def Product_Pairs_Numbers(L1st): 
    new_L1st = len(L1st)//2 + 1 if len(L1st) % 2 != 0 else len(L1st)//2
    product_L1st = [L1st[i]*L1st[len(L1st)-i-1] for i in range(new_L1st)]
    return product_L1st

rosters1 = list(map(int, input("Введите числа через пробел:\n").split()))
print (f'Произведение пар чисел в списке равно => {Product_Pairs_Numbers(rosters1)}')
print()
# # ========================= 

print('Второй способ:') 

def Product_Pairs_Numbers2(L1st):
    result = []
    while len(L1st) > 1:
        result.append(L1st[0]*L1st[-1])
        del L1st[0] 
        del L1st[-1] 
    if len(L1st) ==1: result.append(L1st[0]**2)       
    return result

rosters2 = list(map(int, input("Введите числа через пробел:\n").split()))

print(f'Произведение пар чисел в списке равно => {Product_Pairs_Numbers2(rosters2)}')               
print()
# ===================================================

# 3. +++++

print('Задача 3 => В заданном списке вещественных чисел найдите разницу ') 
print('между максимальным и минимальным значением дробной части элементов.') 

print('Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19')
print()

rosters3 = list(map(float, input("Введите числа через пробел:\n").split()))
# print(rosters3)

def Difference_Max_Min(my_list): 
    a = []
    for i in my_list:
        if i%1 != 0:
            j = round(i%1,2)
            a.append(j)
    return a

# print(funcial(rosters3))

my_list1 = Difference_Max_Min(rosters3)
# print(min(my_list1))
# print(max(my_list1))

print(f'Разница между максимальным и минимальным значением дробной части элементов равно => {max(my_list1) - min(my_list1)}')


# # ======================================================

# 4.
print('Написать программу преобразования десятичного числа в двоичное') 
print('Пример: 45 -> 101101 ') 
print('         3 -> 11')
print('         2 -> 10')

print()


# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)

# # ================================  

# n = int(input('Введите число: '))

# def conv_dec_to_bin(n):
#     bin_num = ''
#     while n > 1:
#         bin_num += str(n % 2)
#         n = n // 2
#     return bin_num[::-1]

# print(conv_dec_to_bin(n))

# # Другие решения

# def convert_dec_to_bin(n):
#     bin_num = []
#     while n > 1:
#         bin_num.insert(0, n % 2)
#         n = n // 2
#     return bin_num

# print(convert_dec_to_bin(n))

# print(bin(n).replace('0b1',''))                    # ================

# =====================================================
