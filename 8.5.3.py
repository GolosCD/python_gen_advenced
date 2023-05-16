w =input()
y=w.lower()
n= set(w.split())
h=n

for i in range(len(w)):
    if ord(w[i]) not in range(ord('a'),ord('z')) and w[i]!=' ':
            y=y.replace(w[i],'')


print(len(set(y.split()))   )