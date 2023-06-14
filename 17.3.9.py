Вам доступен CSV-файл data.csv, содержащий информацию в csv формате.
 Напишите функцию read_csv для чтения данных из этого файла. 
 Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, 
 а каждую последующую строку как значения этих ключей.


def read_csv():
    file_name = 'data.csv'
    
    t = list()    

    with open (file_name,'rt', encoding='utf8') as name_open:
        key = name_open.readline().strip().split(',')
        line = [name.strip().split(',') for name in name_open.readlines()]

    for lin in line:
        t.append(dict(zip(key, lin)))

    #return t
    print(t)
    

read_csv()


