n = int(input())
k = int(input())

#Потратил много времени на решение, больше такое не решаю. 

for i in range(1,n+1):
    print(a)
    a=(a+k)%i
    print(f'a:={a}',f'a+k:={a+k}',f'i:={i}',f'(a+k)%i={(a+k)%i}',end='\n')
print(a+1)    

