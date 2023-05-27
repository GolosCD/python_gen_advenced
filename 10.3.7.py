import string
import random

LETTER = list((set(string.printable[: string.printable.rindex('!')])) - set('lI1oO0'))

print(LETTER)

# generate_str: str = string.printable[: string.printable.rindex('!')]


# for i in '1Ilo0O':
#     generate_str = generate_str.replace(i,'')

# generate_str = list(generate_str)

# def generate_password(length):
#     return length

# def generate_passwords(count:int, length:int):
    
#     for _ in range(count):
#         random.shuffle(generate_str)
#         password = random.sample(generate_str,length)
#         print(''.join(password))



# if __name__ == '__main__':
#               n, m = int(input()), int(input())
              
#               generate_passwords(n,generate_password(m))