# put your python code here
n = [int(j) for j in input().split()]
numbers = set()
for i in n:
    if i not in numbers:
        print('NO')
        numbers.add(i)
    else:
        print('YES')