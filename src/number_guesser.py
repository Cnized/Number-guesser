''' Author: Cnized (Kian Kheiri N.)
    Date: 2025-09-03
    description: A simple Number Guesser game implementation in Python.
    '''
import random 
import time
def number_guesser():
    ''' A simple number guessing game where the user has to guess a randomly selected number between 1 and 100.
        The user can type 'quit' to exit the game or 'score' to see their current score
        1. If the user guesses the correct number, they win and can choose to play again.
        2. If the guess is too high or too low, they are informed and their score decreases slightly.
        3. The game continues until the user decides to quit.
        :return: None
        :rtype: None
    '''
    score = 0
    selected_num = random.randrange(1,100,1)
    while True:
        user_input = input(('Guess a number between 1 and 100 \n (Type \'quit\' to exit the game) \n (You can see your score by typing \'score\') '))
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'score':
            print(f'Your Score is', score)
            continue
        try:
            guess = int(user_input)
        except ValueError:
            print('Invalid Input! Please enter a number between 1 and 100')
            time.sleep(1)
            continue
        else:
            if guess == selected_num:
                print('You Won!!')
                score += 1
                cont = input('Do you want to play again? (Y/N) ')
                if cont.lower() == 'y':
                    selected_num = random.randrange(1,100,1)
                    continue
                elif cont.lower() == 'n':
                    break
            if guess > selected_num :
                print('Number too high\n Try Again!')
                score -= 0.1
            if guess < selected_num :
                print('Number too low\n Try Again!')
                score -= 0.1
                
    print('Thanks for playing! Your final score is', score)
number_guesser()

