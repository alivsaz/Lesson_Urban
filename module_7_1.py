# Задача "Учёт товаров"

import os.path

class Product:

    def __init__(self, name, weigt, category):
        self.name = name
        self.weight = weigt
        self.category = category

    def __str__(self):
        string = self.name + ', ' + str(self.weight) + ', ' + self.category
        return string

class Shop():
    __file_name = 'products.txt'

    def check_file(self):
        if not os.path.exists(self.__file_name):    # проверка наличия файла
            file = open(self.__file_name, 'w')
            file.close()

    def get_products(self):
        self.check_file()
        file = open(self.__file_name, 'r')
        str_name = file.read()
        file.close()
        return str_name

    def add(self, *products):
        file_string = self.get_products()
        file = open(self.__file_name, 'a+')
        for product in products:
            if file_string.find(str(product)) == -1:
                file.write(f'{product}\n')
            else:
                print(f'Продукт {product} уже есть в магазине' )
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())
