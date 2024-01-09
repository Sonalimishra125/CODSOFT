import random

print("Welcome to the Game Rock Paper & Scissors")
print("**************Menu****************")
print("press")
print("0 for Rock")
print("1 for paper")
print("2 for scissors")

max_attempts = 5
user_wins = 0
computer_wins = 0

for attempt in range(max_attempts):
    print(f"\nAttempt {attempt + 1}/{max_attempts}")
    print("Enter your choice:")
    user_choice = int(input())

    if user_choice > 2 or user_choice < 0:
        print("Invalid choice!")
    else:
        computer_choice = random.randint(0, 2)
        print("Computer choice:", computer_choice)

        if user_choice == computer_choice:
            print("It's a Draw!")
        elif (user_choice == 0 and computer_choice == 2) or (user_choice > computer_choice):
            print("You win!")
            user_wins += 1
        else:
            print("You lose!")
            computer_wins += 1

# Display overall result after max attempts
print("\nGame Over!")
print("Your total wins:", user_wins)
print("Computer's total wins:", computer_wins)

if user_wins > computer_wins:
    print("Congratulations! You are the overall winner.")
elif user_wins < computer_wins:
    print("Better luck next time. The computer is the overall winner.")
else:
    print("It's a tie overall.")


