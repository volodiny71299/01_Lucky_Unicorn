# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

import random

# Integer checking function below


def intcheck(question, low, high):
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

# Main routine

# Ask User how much they want to play with (min $1, max $10)
balance = intcheck("How much money would you like to play with? $", 1, 10)

keep_going = ""
while keep_going == "":

    # tokens list includes 10 times to prevent too many unicorns being chosen
    tokens = ["horse", "zebra",
              "horse", "zebra",
              "horse", "zebra",
              "donkey", "donkey",
              "donkey", "unicorn"]

    # Randomly choose a token from out list above
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

    # Adjust total correctly for a given token
    if token == "unicorn":
        balance += 5        # Win $5
        feedback = "Congratulations! You won $5.00!"

    elif token == "donkey":
        balance -= 1        # doesn't win anything
        feedback = "Sorry, you did not win anything this round"

    else:
        balance -= 0.5      # Win $0.50
        feedback = "Yay! You won $0.50"

    print()

    print(feedback)
    print("You have ${:.2f} on your balance".format(balance))

    if balance >= 1:
        keep_going = keep_going = input("Press <ENTER> to keep going or any other key to exit")
    else:
        keep_going = "End"
        print("You are unable to continue")
print()
print(":)")
