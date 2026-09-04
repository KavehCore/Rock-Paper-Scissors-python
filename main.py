#import and global variables
import random
USER_CHOICES = ("rock", "paper", "scissor")

# Create a function to get user input
def get_user_input():
    choice = input("pick yor choise [rock, paper, scissor]: ").lower()
    while choice not in USER_CHOICES:
        choice = input("pick yor choise [rock, paper, scissor]: ").lower()
    return choice
# create a function to get pc input
def get_pc_input():
    pc_choice = random.choice(USER_CHOICES)
    print(f"pc choice was: {pc_choice}")
    return pc_choice

# compare and determine which one is the winner
def determine_winner(user_input, pc_input):
    if user_input == pc_input:
        print("DRAW!!")
    elif (user_input == "rock" and pc_input == "scissor") \
    or (user_input == "scissor" and pc_input == "paper") \
    or (user_input == "paper" and pc_input == "rock"):
        print("user won!")
    else:
        print("computer won!")


# Create a main function as the runner
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()

    determine_winner(user_input, pc_input)
    print("end of game!")

# make an iteration for doing the game as much as we need
answer = "y"
if __name__ == "__main__":
    while answer != "n":
        if answer == "y":
            main()
        answer = input("do you want to continue? (y/n)").lower()