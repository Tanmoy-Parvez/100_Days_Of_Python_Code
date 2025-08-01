import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors:\n"))
computer_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
    print("You choose an invalid option!")
else:
    print(game_options[user_choice])

    print("Computer Chose:")
    print(game_options[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose")
    else:
        print("It's a draw! Play Again!")
