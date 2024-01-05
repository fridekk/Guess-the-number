import random

print('Давай сыграем в игру')
tries = 0

num = random.randint(1, 10)

while tries <= 8:
    user_ans = int(input('Введи число от 1 до 10:  \n'))
    if user_ans == num:
        print('Ты угадал')
        break
    else:
        tries += 1
        print('Ты не угадал')
