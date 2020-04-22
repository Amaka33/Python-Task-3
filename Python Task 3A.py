from random import randint
print('''Guessing game''')

print()
E =''
M =''
H =''
YES =''
NO =''


def easy():
    set_number = randint(1,10)
    print('''you have 6 gueses''')
    guess= input('your guess number(1-10): ')
    for guess_count in range(5):
            while guess != set_number:
                    print('that was wrong, you have', 5-guess_count,' guesses left')
                    guess= int(input('your guess number{1-10}: '))
                    break
            else:
                 print('You got it right')
                 break
                 
    else:
        print('game over')





def medium():
    set_number = randint(1,20)
    print('''you have 4 gueses''') 
    guess= input('your guess number(1-20): ')
    for guess_count in range(3):
            while guess != set_number:
                    print('that was wrong, you have', 3-guess_count,' guesses left')
                    guess= int(input('your guess number{1-20}: '))
                    break
            else:
                 print('You got it right')
                 break
                 
    else:
        print('game over')





def hard():
    set_number = randint(1,50)
    print('''you have 3 gueses''')
    guess= input('your guess number(1-50): ')
    for guess_count in range(2):
            while guess != set_number:
                    print('that was wrong, you have', 2-guess_count,' guesses left')
                    guess= int(input('your guess number{1-50}: '))
                    break
            else:
                 print('You got it right')
                 break
                 
    else:
        print('game over')



start = True
while start:

    difficulty_level = str(input('what level of difficulty;e= easy, m=medium, h=hard? ')).upper()
    print('')

    if difficulty_level=="E":
        easy()

    elif difficulty_level=="M":
        medium()

    elif difficulty_level=="H":
        hard()
    continuation = str(input('do you want to continue the game?{yes or no}' )).upper()

    if continuation == 'YES':
        start = True
    else:
        start = False



            
