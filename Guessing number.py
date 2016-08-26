#Guess number game

import random

number = random.randint(1, 20) #random number what you have to guess between 1 ~ 20

t_num = 0 #trial number

print('Welcome, This is Guessing the number game between 1 ~ 20')
print('You can get trial number you want')
print('So, input number and start the game!!')

want_num = input() #trial number you want
want_num = int(want_num)

while t_num < want_num :

    print('Take a guess')

    mynum = input() #the number what you guess
    mynum = int(mynum)

    t_num = t_num+1

    if mynum == number:
        t_num = str(t_num)
        print('Great!, You guessed my number in ' + t_num + ' guesses!')
        break
    if mynum > number:
        print('Your guess is too high')
        print('')

    if mynum < number:
        print('Your guess is too low')
        print('')


if mynum != number:
    number = str(number)
    print('You failed... I am sorry about that, well my number is ' + number + '...')
    print('Cheer up!')
