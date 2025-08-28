import random
from art import logo

def deal_card():
    """Return a random card from the list/deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calc_score(cards):
    """Return the sum of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare (u_score, c_score):
    """Compares user score & computer score"""
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    com_cards = []
    com_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        com_cards.append(deal_card())

    while not is_game_over:
        user_score = calc_score(user_cards)
        com_score = calc_score(com_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {com_cards[0]}")

        if user_score == 0 or com_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while com_score != 0 and com_score < 17:
        com_cards.append(deal_card())
        com_score = calc_score(com_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {com_cards}, final score: {com_score}")
    print(compare(user_score, com_score))

restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while restart == "y":
    print("\n" * 20)
    play_game()

