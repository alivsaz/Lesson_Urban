# Некорректность

class Car:

    def __init__(self, model, vin, number):
        self.model = model
        self.__vin = vin
        self.__numbers = number
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        self.__vin = vin_number
        if not isinstance(self.__vin, int):
            raise IncorrectVinNumber(Exception('Некорректный тип vin номер'))
        if not 1000000 <= self.__vin <= 9999999:
            raise IncorrectVinNumber(Exception('Неверный диапазон для vin номера'))
        return True

    def __is_valid_numbers(self, number):
        self.__numbers = number
        if not isinstance(self.__numbers, str):
            raise IncorrectCarNumbers(Exception('Некорректный тип данных для номеров'))
        if len(self.__numbers) != 6:
            raise IncorrectCarNumbers(Exception('Неверная длина номера'))
        return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')