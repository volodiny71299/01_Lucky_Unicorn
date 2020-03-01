# Lucky Unicorn Fully Working Program

import random

# Integer checking function below


def check(question, low, high):
    valid = False
    error = "Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)


def token_statement(fdbck, balance, char):
    if len(fdbck) > len(balance):
        use_length = len(fdbck)
    else:
        use_length = len(balance)
    print()
    print(char * use_length)
    print(fdbck)
    print()
    print(balance)
    print(char * use_length)
    print()

# Values of each variable

COST = 1        # Cost per round
UNICORN = 5     # unicorn wins $5
ZEB_HOR = 0.5   # zebra/horse wins $0.50
DONKEY = 0      # donkey doesn't win anything

# Introduction to the game
print("Welcome to the Lucky Unicorn Game\n"
      "To play, enter an amount of money between $1 and $10 (whole dollars).\n"
      "$1 cost entry Per round\n"
      "Follow the instructions given\n"
      "Let me know if the program misbehaves\n"
      "Good luck!")

# Lets you input how much money you'd like to start with (from $1 - $10)
balance = check("\nHow much money would you like to play with? $", 1, 10)
round_count = 0

# Start of loop
keep_going = ""
while keep_going == "":

    # Token list
    tokens = ["horse", "zebra",
              "horse", "zebra",
              "horse", "zebra",
              "horse", "zebra",
              "horse", "zebra",
              "donkey", "donkey",
              "donkey", "donkey",
              "donkey", "unicorn"]

    # Gives a statement to the randomly generated token
    token = random.choice(tokens)
    round_count += 1

    # Adjust balance based on the chosen token and gives feedback
    if token == "unicorn":
        balance += UNICORN
        feedback = "* Congratulations! It's A ${:.2f} {} *".format(UNICORN, token)
        decoration = "*"

    elif token == "donkey":
        balance -= COST
        feedback = "- Sorry. It's a {}. You don't win anything this round -".format(token)
        decoration = "-"

    else:
        balance -= ZEB_HOR
        feedback = "^ You got a {}. You only lose 50c ^".format(token)
        decoration = "^"

    print()
    token_statement(feedback,
    "Rounds Played: {}    Balance: ${:.2f}".format(round_count, balance),
    decoration)
    print()

    # Continue or exit loop
    if balance > COST:
        keep_going = input("\nPress <ENTER> to keep going or any other key to exit")
    else:
        keep_going = "End"
        print("You need $1.00 in your balance in order to continue playing. Your balance = ${:.2f}".format(balance))

# Prints final results
print()
print("You're going home with ${:.2f}\n".format(balance))
