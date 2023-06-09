'''
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". 
Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить 
честный жребий и определить, кто будет делать очередной модуль нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" 
или "бумага". На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, 
Руслан или же они сыграют вничью.

Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает 
бумаге, а ножницы побеждают бумагу.
'''
inp = {'камень': 1, 'ножницы': 2, 'бумага': 3}

comb = {12: 1, 21: 2, 13: 2, 31: 1, 32: 2, 23: 1}

winer = {1: 'Тимур', 2: 'Руслан'}

k = ''


for i in range(2):
    k += str(inp.get(input()))


if int(k) in comb.keys():
    print(winer.get(comb.get(int(k))))
else:
    print('ничья')
