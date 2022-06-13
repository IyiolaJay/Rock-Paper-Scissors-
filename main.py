import random

possible_actions = ['Rock', 'Paper', 'Scissors']
user_selection = input('Please make your selection: Rock, Paper or scissors: \n')
computer = random.choice(possible_actions)

print(f'You selected {user_selection},\n Computer Selected {computer}')
if user_selection == computer:
    print(f"Both players selected {user_selection}. It's a tie!")
elif user_selection == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_selection == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_selection == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
