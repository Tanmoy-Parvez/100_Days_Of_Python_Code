import random
from art import logo

def check_answer(user_guess, answer, turns):
    if user_guess == answer:
        print(f"You got it! The answer was {answer}")
        return turns
    elif user_guess < answer:
        print("Too Low. \nGuess again.")
        return turns - 1
    else:
        print("Too High. \nGuess again.")
        return turns - 1

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        return 5
    elif difficulty == "easy":
        return 10
    else:
        print("Invalid input, defaulting to 'easy'.")
        return 10

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)

    turns = set_difficulty()
    guessed_number = 0

    while guessed_number != random_number and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))

        turns = check_answer(guessed_number, random_number, turns)

    if turns == 0 and guessed_number != random_number:
        print(f"You've run out of guesses. The number was {random_number}.")

play_game()
