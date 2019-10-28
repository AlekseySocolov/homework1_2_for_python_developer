set_elements_1 = set()
str_element = ''
amount_of_elements_1 = input('Введите количество элементов первого списка: ')
while amount_of_elements_1.isdigit() != True:
    amount_of_elements_1 = input('Введите количество элементов первого списка: ')
for i in range(int(amount_of_elements_1)):
    str_element = input(f'Введите {i+1}-й элемент (цифру): ')
    while (str_element.isdigit() != True) or int(str_element) // 10 >0:
        str_element = input(f'Введите {i + 1}-й элемент (цифру): ')
    else:
        set_elements_1.add(str_element)
set_elements_2 = set()
amount_of_elements_2 = input('Введите количество элементов второго списка: ')
while amount_of_elements_2.isdigit() != True:
    amount_of_elements_2 = input('Введите количество элементов второго списка: ')
for i in range(int(amount_of_elements_2)):
    str_element = input(f'Введите {i+1}-й элемент (цифру): ')
    while (str_element.isdigit() != True) or int(str_element) // 10 >0:
        str_element = input(f'Введите {i + 1}-й элемент (цифру): ')
    else:
        set_elements_2.add(str_element)
print('Результат: ',','.join(set_elements_1-set_elements_2))