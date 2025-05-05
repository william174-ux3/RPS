# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # checks for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
               print(error)
            else:
                return response

        except ValueError:
           print(error)


# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0


print(" Rock / Paper / Scissors Game")
print()

# instructions

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played <= num_rounds:
    input("Choose: ")
    rounds_played += 1


# game loop starts here

# game history / statistics area