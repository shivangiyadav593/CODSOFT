import random

# Initialize scores
user_score = 0
computer_score = 0

# Display instructions
print("=====================================")
print("Welcome to Rock-Paper-Scissors...!")
print("=====================================")
print("Instructions:")
print("i)Type 'rock', 'paper', or 'scissors' to make your choice.")
print("                                                            ")
print("ii)The computer will randomly choose one of the three options.")
print("                                                            ")
print("iii)Rock smashes scissors, scissors smashes paper, and paper smashes rock.")
print("                                                            ")
print("iv)Your score and the computer's score will be displayed after each round.")
print("                                                            ")
print("v)Type 'exit' to end the game.")

# Game loop
while True:
    # Get user's choice
    print("=========================================================================")
    user_choice = input("Enter your choice: ").lower()
    
    if user_choice == 'exit':
        break
    
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("\nEnter your choice: ").lower()
    
    # Get computer's choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    # Display results
    print(f"\nYou choice: {user_choice}")
    print(f"The computer choice: {computer_choice}")
    print(result)
    print("=========================================================================")
    print(f"Score :- You: {user_score}, Computer: {computer_score}")
    
    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("\nThanks for playing...Have a great day!")
