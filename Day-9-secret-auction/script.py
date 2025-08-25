from art import logo

print(logo)

def find_highest_bidder(bidding_dict):

    highest_amount = 0
    winner = ""

    for bidder in bidding_dict:
        if bidding_dict[bidder] > highest_amount:
            highest_amount = bidding_dict[bidder]
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_amount}")

bidders_info = {}

continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bidders_info[name] = bid_amount
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bidders_info)
    else:
        print("\n" * 20)