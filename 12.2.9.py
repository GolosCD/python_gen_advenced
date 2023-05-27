""" Генератор паролей 2 🌶️
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.

Формат входных данных
На вход программе подаются два числа nn и mm, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.

Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.
Примечание 3. Приведенные ниже тесты – это лишь образцы возможного ответа. Возможны и другие способы генерации паролей. """

import string
import random

generate_str: list = list((set(string.printable[: string.printable.rindex('!')])) - set('lI1oO0'))
random_dig = list(set(string.digits[2:]))
random_ABC = list(set(string.ascii_uppercase) - set('lI1oO0') )
random_abc = list(set(string.ascii_lowercase) - set('lI1oO0') )

def generate_password(length: int):
    step_1 = ''.join(random.sample(generate_str,length))
    step_2 = step_1[1:]+random.choice(random_dig)
    step_3 = step_2[1:]+random.choice(random_abc)
    step_4 = step_3[1:]+random.choice(random_ABC)
    return step_4

def generate_passwords(count:int, length:int):
    for _ in range(count):        
        print(generate_password(length))



if __name__ == '__main__':
              n, m = int(input()), int(input())
              generate_passwords(n,m)