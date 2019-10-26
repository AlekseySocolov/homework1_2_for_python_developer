list_elements = []
str_element = ''
amount_of_elements = input('Введите количество элементов: ')
while amount_of_elements.isdigit() != True:
    amount_of_elements = input('Введите количество элементов: ')
for i in range(int(amount_of_elements)):
    str_element = input(f'Введите {i+1}-й элемент (цифру): ')
    while (str_element.isdigit() != True) or int(str_element) // 10 >0:
        str_element = input(f'Введите {i + 1}-й элемент (цифру): ')
    else:
        list_elements.append(str_element)
print('Вывод: ', sorted(list_elements))