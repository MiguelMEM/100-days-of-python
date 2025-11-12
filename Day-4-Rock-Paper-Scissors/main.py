import random

game_choices=['Rock', 'Paper', 'Scissors']

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

computer_choice = random.randint(0,2)

if user_choice >= 0 and user_choice <= 2:
    print(game_choices[user_choice])

print("Computer choice:")
print(game_choices[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You loose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You loose!")
elif user_choice < computer_choice:
    print("You loose!")
elif user_choice == computer_choice:
    print("It's a draw!")
