import random

choices = ["stone", "paper", "scissor"]

choice_to_number = {"stone": 0, "paper": 1, "scissor": 2}
number_to_choice = {0: "stone", 1: "paper", 2: "scissor"}

# 0: stone, 1: paper, 2: scissors
# stone beats scissor, paper beats stone, scissor beat paper
rules = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

while True:
    # Get user input
    user_choice = input("Enter your choice (stone, paper, scissor) or 'exit' to quit: ").lower()
    
    if user_choice == 'exit':
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    # Generate computer's choice
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice}")
    
    # Determine the result
    user_number = choice_to_number[user_choice]
    computer_number = choice_to_number[computer_choice]
    result = rules[user_number][computer_number]
    
    if result == 1:
        print(f"You win! {user_choice} beats {computer_choice}.")
    elif result == -1:
        print(f"You lose! {computer_choice} beats {user_choice}.")
    else:
        print("It's a tie!")

    print()  # Add a blank line for better readability