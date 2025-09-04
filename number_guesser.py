import random 
import time
def number_guesser():
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

