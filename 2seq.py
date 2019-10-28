indicator = 1
while indicator > 0:
    indicator = 0
    str_element = input('Введите элементы (цифры) списка, используя один из 3-х разделителей - \nзапятую, точку с запятой, слэш (но только какой то один 1,2;3/4 - так нельзя): ')
    if (',' in str_element and  '/' in str_element and ';' in str_element) or ('/' in str_element and ';' in str_element) or (',' in str_element and  ';' in str_element) or (',' in str_element and  '/' in str_element):
        print('Ипользуйте только один разделитель!')
        indicator = 1
    str_element = str_element.replace('/',',')
    str_element = str_element.replace(';',',')
    if not(str_element.replace(',','').isnumeric()):
        print('Вводите цифры, а в качестве разделителей вводите только запятую, точку с запятой или слэш!')
        indicator = 1
list_elements = str_element.split(',')
dict_elements = set (list_elements)
print('Результат: ',','.join(dict_elements))