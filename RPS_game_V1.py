import random

# Check that the users have entered a valid
# option based on a list def string_checker(question, valid_ans=('yes', 'no')):
def string_checker(question, valid_ans=("yes", "no")):
    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        return "invalid"


# displays instructions
def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

To begin, choose the number of rounds (or press <enter> for infinite mode).

The play against the computer. You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follows:
o   Paper beats rock
o   Rock beats scissors
o   Scissors beats paper

Press <enter> to end the game at anytime.


Good Luck!
    """)

# checks for an integer more than 0 (allows <enter>)
from string_checker_V3 import user_choice, rps_list
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


# compares user / computer choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):

    # if the user and the computer choice is the same, it's a tie
    if user == comp:
        result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"
    # if it's not a win / tie, then it's a loss
    else:
        result = "lose"

    return result


# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print(" Rock / Paper / Scissors Game")
print()

# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to see the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\nRound {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\nRound {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history / statistics area