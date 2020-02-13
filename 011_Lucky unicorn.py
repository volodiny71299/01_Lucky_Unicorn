#v1 Lucky Unicorn
#Yara Volodin 3/2/2020


def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Please enter an integer between {} and {} ".format(low, high)
        try:
            response = int(input("Enter an integer between {} and {} ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


how_much = intcheck("How much money do you want to play with ", 1, 10)

num_1 = intcheck("Enter a number between 1 and 15  ", 1, 15)
num_2 = intcheck("Enter a number between 5 and 10", 5, 10)
