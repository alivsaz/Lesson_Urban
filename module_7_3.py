# Задача "Найдёт везде"
from pprint import pprint

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = (file_names)

    def get_all_words(self):
        all_words ={}
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            words = ''
            with open(file, encoding='utf-8') as f:
                for line in f:
                    line = line.lower()
                    for k in line:
                        if k in punc:
                            line = line.replace(k, '')
                    words += line
                all_words.update({file:words.split()})
        return all_words

    def find(self, word):
        dict_word = {}
        for name, words in self.get_all_words().items():
            for i in range(len(self.get_all_words()[name])):
                if words[i].find(word.lower()) != -1:
                    dict_word.update({name: i+1})
                    break
                else:
                    dict_word.update({name: 0})
        return dict_word

    def count(self, word):
        dict_count = {}
        for name, words in self.get_all_words().items():
            i = words.count(word.lower())
            dict_count.update({name: i})
        return dict_count

print(f'\nТест для нескольких файлов:')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
pprint(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

print(f'\nТест для одного файла:')
finder2 = WordsFinder('test_file.txt')
pprint(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего