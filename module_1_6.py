# Словари
my_dict = {'Юрий' : 29, 'Маша' : 17, 'Константин' : 37 }
print('Словарь: ' + str(my_dict))
print('Возраст: ' + str(my_dict['Маша']))
print('Отсутствующий возраст: ' + str(my_dict.get('Николай', 'Значение возраста отсутствует')))
my_dict.update({'Ирина' : 22, 'Юлия' : 33 })
print('Удаленный элемент: ' + str(my_dict.pop('Константин')))
print('Измененный словарь: ' + str(my_dict))
print() # Пустая строка для разделения заданий
# Множества
my_set = {88, 'Овощи', 25.12, 1, 3, 5, (1, 3, 5, 7), 5, 3}
print('Множество: ' + str(my_set))
my_set.update('4', '7')
my_set.discard(5)
print('Новое множество: ' + str(my_set))
