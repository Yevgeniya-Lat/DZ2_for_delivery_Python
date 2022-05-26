print('Задача 3 => В заданном списке вещественных чисел найдите разницу ') 
print('между максимальным и минимальным значением дробной части элементов.') 

print('Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19')
print()

rosters3 = list(map(float, input("Введите числа через пробел:\n").split()))
print(rosters3)


# def fractional_part(L1st):
#     a = []
#     for i in rosters3:
#         j = round(i%1,3)
#         a.append(j)
#     return a

# print(fractional_part(rosters3))
# my_list = fractional_part(rosters3)
# print(min(my_list))
# print(max(my_list))

my_rosters = [round(i%1,2) for i in rosters3 if i%1 != 0]
print(max(my_rosters) - min(my_rosters))