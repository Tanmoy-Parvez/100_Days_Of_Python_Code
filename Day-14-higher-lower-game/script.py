from art import logo, vs
import random
from game_data import data

print(logo)

def format_account(account):
    """Return a formatted string with account details."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def is_guess_correct(user_guess, a_followers, b_followers):
    """Check if the user guessed the higher follower count correctly."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Start with a random account for B
account_b = random.choice(data)
score = 0
game_active = True

while game_active:
    account_a = account_b
    account_b = random.choice(data)

    # Avoid comparing the same account
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"🔥 Compare A: {format_account(account_a)}")
    print(vs)
    print(f"⚡ Against B: {format_account(account_b)}")

    guess = input("👉 Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    correct = is_guess_correct(guess, followers_a, followers_b)

    if correct:
        score += 1
        print(f"✅ You're right! Current score: {score} 🎉\n")
    else:
        print(f"❌ Oops, that's wrong! Final score: {score} 💀")
        game_active = False
