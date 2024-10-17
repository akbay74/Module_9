# Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = map(lambda x, y: x == y, first, second)
print(list(result))

# Замыкание

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for element in data_set:
                file.write(str(element) + '\n')

    return write_everything

name = 'example.txt'
write = get_advanced_writer(name)
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
with open(name, 'r') as file:
    for i in file:
        print(i, end = '')

# Метод __call__

from random import choice

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
