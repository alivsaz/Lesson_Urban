# Файлы в операционной системе

import os, time

directory = os.getcwd()
root, dirs, files = [], [], []

for root, dirs, files in os.walk(directory):
    for file in files:
        if os.path.isfile(file):
            filepath = os.path.join('.', file)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(file)
            parent_dir = root
            print(f'\nОбнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')  
    #  используем "break" если нужны файлы только из текущей директории
    break
