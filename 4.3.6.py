#На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.

#Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

n = input().split()

ch = int(input())
ln = list()
def chanked(n, ch, ln):
    if ch <= len(n):
        for i in range(0, len(n) - 1, ch):
            tmp_l = list()
            for j in range(ch):
                tmp_l.append(n[i + j])
            ln.append(tmp_l)
    else:
        ln.append(n)
    if (len(n) % 2 != 0 and ch % 2 == 0) or ch == 1:
        ln.append([n[-1]])
    
if __name__ == '__main__':
    chanked(n, ch, ln)
    print(ln)    

