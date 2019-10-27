indicator = 1
while indicator > 0:
    indicator = 0
    str_element = input('Введите элементы (цифры) списка, используя один из 3-х разделителей - \nзапятую, точку с запятой, слэш (но только какой то один 1,2;3/4 - так нельзя): ')
    if (str_element.find(',') >= 0 and str_element.find('/') >= 0 and str_element.find(';') >= 0) or (str_element.find('/') >= 0 and str_element.find(';') >= 0) or (str_element.find(',') >= 0 and str_element.find(';') >= 0) or (str_element.find(',') >= 0 and str_element.find('/') >= 0):
        print('Ипользуйте только один разделитель!')
        indicator = 1
    str_element = str_element.replace('/',',')
    str_element = str_element.replace(';',',')
    if not(str_element.replace(',','').isnumeric()):
        print('Вводите цифры, а в качестве разделителей вводите олько запятую, точку с запятой, слэш!')
        indicator = 1
list_elements = []
list_elements = str_element.split(',')
dict_elements = ()
dict_elements = set (list_elements)
print(dict_elements)