from random import randint
from sys import exit

def check_guess(current_number):
    right_num = 0 #完全正确个数
    correct_position = 0 #数对位置不对个数
    for i in range(0,4):
        try:
            if  correct_number[i] == int(current_number[i]):
                right_num += 1
            elif int(current_number[i]) in correct_number:
                correct_position += 1
        except ValueError:
            print('%r is not a number,try a number next time.'%current_number[i])
    print ('%dA%dB, %r chances left.' %(right_num, correct_position, (10 - guesses)))
    if right_num ==4:
        print('Great! You got the right answer!')
        exit(1)

#生成随机数，首位不为0，互相不重复
correct_number = [randint(1,9)]
for i in range(0,3):
    next_num = randint(0,9)
    while next_num in correct_number:
        next_num = randint(0,9)
    correct_number.append(next_num)

guesses = 0 #猜的次数

while guesses < 10:
    guesses += 1
    my_guess = input('guess four numbers with \',\' to split each one another:\n')
    current_number = my_guess.split(',')
    check_guess(current_number)
