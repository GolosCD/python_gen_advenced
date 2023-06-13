from string import ascii_lowercase as az
file_name = 'nums.txt'

my_range = range(0,999)

total=0
tmp_dig=''

with open (file_name, 'rt', encoding = 'utf8') as file_open:
    file = [i.strip(az) for i in file_open.read()]


for i in range(len(file)):
    if file[i].isdigit() and file[i+1].isdigit():
        tmp_dig+=file[i]
        print(f'Шаг_1, число:{file[i]}, уже в под итоге: {tmp_dig}')
    elif file[i].isdigit() and not file[i+1].isdigit():
        tmp_dig+=file[i]
        total+=int(tmp_dig)
        tmp_dig=''
        print(f'Шаг_2, число:{file[i]}, уже в под итоге: {tmp_dig}, а в итоге: {total}')
        
print(total)        


with open('nums.txt', encoding='utf-8') as file:
    print(list(map(int, ''.join(list(map(lambda x: x if x.isdigit() else ' ', file.read()))).split())))
    
    print(sum(map(int, ''.join(list(map(lambda x: x if x.isdigit() else ' ', file.read()))).split())))