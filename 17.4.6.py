# пример одновременной записи и чтения
def minutes(x):
    res=[int(i) for i in x.split(':')]
    return res[0]*60+res[1]

file_name_read = 'logfile.txt'

file_name_write = 'output.txt'

with open (file_name_read, 'r', encoding = 'utf8') as file_read,\
     open (file_name_write, 'w', encoding = 'utf8') as file_write:
     for line in file_read:
        name,st,end, = line.split(',')
        if minutes(end)-minutes(st)>=60:
            file_write.write(name+'\n')
