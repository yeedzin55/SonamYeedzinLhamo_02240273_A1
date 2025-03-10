import random

# Guessing the number game
def guess_number_game():
    print("\n--- Guess the Number Game ---")
    print("I have selected a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    guesses_taken = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Guess a number: "))
            guesses_taken += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {guesses_taken} attempts!")
                guessed_correctly = True
        except ValueError:
            print("Please enter a valid number.")

# Rock paper scissors game
def rock_paper_scissors_game():
    print("\n--- Rock, Paper, Scissors Game ---")
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        
        if user_choice not in choices:
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")

def main():
    while True:
        print("\nSelect a function (1-3):")
        print("1. Guess Number game")
        print("2. Rock Paper Scissors game")
        print("3. Exit program")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                guess_number_game()
            elif choice == 2:
                rock_paper_scissors_game()
            elif choice == 3:
                print("Exiting program")
                break
            else:
                print("Invalid choice. Please select between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
