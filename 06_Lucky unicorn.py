# Lucky Unicorn
# Payment mechanics

# To do
# Assume starting amount is $10
# Allow manual token input for testing purposes
# Adjust total correctly for a given token
#   - if it's a unicorn, add $5
#   - if it's a horse / zebra, add $0.5
#   - if it's a donkey, subtract 1
# Give user feedback based on winnings...
# State new total

# Assume starting amount is $10
total = int(input("How much money would you like to play with? "))

keep_going = ""
while keep_going == "":

    # Allow manual token input for testing purposes
    token = input("enter a token: ")

    # Adjust total correctly for a given token
    if token == "Unicorn":
        total += 5
        feedback = "Congratulations! You won $5.00!"

    elif token == "Donkey":
        total -= 1
        feedback = "Sorry, you did not win anything this round"

    else:
        total += 0.5
        feedback = "Yay! You gained $0.50"

    print()

    print(feedback)
    print("You have ${:.2f} to play with".format(total))

    if total < 1:
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "End"
    else:
        keep_going = input("Press <ENTER> to play again or any key to quit")

print("Thank you for playing :)")
