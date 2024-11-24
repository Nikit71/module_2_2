# Домашняя работа по уроку "Условная конструкцияю Оператор if, elif, else"
print()
first = input("Введите первое целое число\n")
second = input("Введите второе целое число\n")
third = input("Введите третье целое число\n")
print('\nКоличество равных чисел')
# При записи условия на несколько строк ставятся круглые скобки
if (first == second and
    first == third):
    print(3)
elif (first == second or
      first == third or
      second == third):
    print(2)
else:
    print(0)
# Задание выполнено