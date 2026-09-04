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



# Create a main function as the runner


# make an iteration for doing the game as much as we need
