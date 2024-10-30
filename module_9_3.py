# Генераторные сборки

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(s1) - len(s2) for s1, s2 in zip(first, second) if len(s1) != len(s2)]
second_result = [len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j]

print(list(first_result))
print(list(second_result))