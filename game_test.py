import random

computer_choice = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])
user_choice = input()

print('I chose ', computer_choice, '.')

if user_choice == computer_choice:
    print('Tie Game')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win!')
elif user_choice == 'rock' and computer_choice == 'lizard':
    print('You win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win!')
elif user_choice == 'paper' and computer_choice == 'spock':
    print('You win!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win!')
elif user_choice == 'scissors' and computer_choice == 'lizard':
    print('You win!')
elif user_choice == 'lizard' and computer_choice == 'paper':
    print('You win!')
elif user_choice == 'lizard' and computer_choice == 'spock':
    print('You win!')
elif user_choice == 'spock' and computer_choice == 'scissors':
    print('You win!')
elif user_choice == 'spock' and computer_choice == 'rock':
    print('You win!')
else:
    print('You lose!')
