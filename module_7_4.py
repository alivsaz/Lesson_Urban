# Форматирование строк

class Team:

    def __init__(self, num, score, time):

        self.num = num
        self.score = score
        self.time = time

def challenge_result():
    if (team1.score > team2.score) or (team1.score == team2.score) and (team1.time > team2.time):
        result = "Победа команды Мастера кода!"
    elif (team1.score < team2.score) or (team1.score == team2.score) and (team1.time < team2.time):
        result = "Победа команды Волшебники Данных!"
    else:
        result = "Ничья!"
    return result

team1 = Team(5, 40, 1552.512)
team2 = Team(6, 42, 2153.31451)
tasks_total = int(team1.score) + int(team2.score)   # количество задач
time_avg = (team1.time + team2.time) / (team1.score + team2.score)  # среднее время решения

print(f'\nИспользование %:')
print('В команде Мастера кода участников: %s !' % (team1.num))
print('Итого сегодня в командах участников: %s и %s !' % (team1.num, team2.num))
print(f'\nИспользование format():')
print('Команда Волшебники данных решила задач: {} !'.format(team2.score))
print('Волшебники данных решили задачи за {:.1f} с !'.format(team1.time * team1.num))

print(f'\nИспользование f-строк:')
print(f'Команды решили {team1.score} и {team2.score} задач.')
print('Результат битвы: {}'.format(challenge_result()))
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!.')