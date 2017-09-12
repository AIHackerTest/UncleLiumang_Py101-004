from random import randint
from sys import exit

def guess_number(correct_number,current_number):
    if correct_number > current_number:
        print ('Too small, %r chances left.' % (10 - guesses))
    elif correct_number < current_number:
        print ('Too big, %r chances left.' % (10 - guesses))
    elif correct_number == current_number:
        print ('Yes! You are correct, the number is excactly %r. ' % correct_number)
        exit(1)


correct_number = randint(0,20)
guesses = 0
#print (correct_number)

while guesses < 10 :
    guesses += 1
    my_guess = input ('Try a number under 20:\n')
    try:
        current_number = int(my_guess)
        print ('your guess is %r,and it\'s:' % current_number)
        guess_number(correct_number,int(current_number))
    except ValueError:
        print ('Sorry, try a number please. %r chances left.' % (10 - guesses))
