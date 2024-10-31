# Генераторы

def all_variants(text):
    string = ''
    for s in text:
        if string == '':
            i = 0
            for i in range(len(text) - i):
                j = 0
                for j in range(len(text) - i - j):
                    string = (text[j:i+j+1])
                    yield string
                    j += 1
                i += 1


a = all_variants("abc")
for i in a:
    print(i)