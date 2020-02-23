# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

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

# Rules + code gives rules
print("#####\n"
      "Follow the instructions given\n"
      "Let me know if program misbehaves\n"
      "Test your luck!\n"
      "#####\n")

# Main routine

# Ask User how much they want to play with (min $1, max $10)
balance = check("How much money would you like to play with? $", 1, 10)

keep_going = ""
while keep_going == "":

    # tokens list includes 10 times to prevent too many unicorns being chosen
    tokens = ["horse", "zebra",
              "horse", "zebra",
              "horse", "zebra",
              "horse", "zebra",
              "horse", "zebra",
              "donkey", "donkey",
              "donkey", "donkey",
              "donkey", "unicorn"]

    # Randomly choose a token from out list above
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

    # Adjust total correctly for a given token

    # Unicorn Statement (Wins $5)
    if token == "unicorn":
        balance += 5        # Win $5
        print()
        print("***")
        print("*** Congratulations! It's a {} ".format(token))
        print("***")

    # Donkey statement (Loses $1)
    elif token == "donkey":
        balance -= 1        # doesn't win anything
        print()
        print("---")
        print("| Sorry. It's a {}. You did not win anything this round |.".format(token))
        print("---")

    # Zebra + Horse statement (Loses 50c because paid $1 and won 50c)
    else:
        balance -= 0.5      # Win $0.50
        print("^^^")
        print("< Good try. It's a {}. You won back $0.50 >".format(token))
        print("^^^")

    print()

    # print(feedback)
    print("You have ${:.2f} on your balance".format(balance))

    if balance >= 1:
        keep_going = keep_going = input("Press <ENTER> to keep going or any other key to exit")
    else:
        keep_going = "End"
        print("You need $1.00 in your balance in order to continue playing")
print()
print("Your final balance is ${:.2f}\n".format(balance))
print(":)")
