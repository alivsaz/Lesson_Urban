# Файлы в операционной системе

import os, time

def main_init():
    """
    Создание директории и файлов для модуля
    """
    file_dir = {'first.txt' : 'Первый', 'second.txt' : 'Второй', 'third.txt' : 'Третий'}
    if os.path.exists('module75'):
        os.chdir('module75')
    else:
        os.mkdir('module75')
        os.chdir('module75')

    for key, item in file_dir.items():
        with open(key, 'w', encoding='utf-8') as f:
            f.write(item)


main_init()
directory = os.getcwd()
root, dirs, files = [], [], []

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join('.', file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = root
        print(f'\nОбнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
