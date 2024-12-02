# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15




first_element= int(input("Введите первый элемент прогрессии: "))
difference = int(input("ведите разность прогрессии: "))
count_elements = int(input("Введите количество элеметов: "))

progression = []

for i in range(count_elements):
    progression.append(first_element + i * difference)

print(progression)