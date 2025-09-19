import random

def number_guessing_game():
    """
    Number Guessing Game
    Python picks a random number between 1 and 50.
    User keeps guessing until they get it right.
    Provides hints if the guess is too high or too low.
    """
    # Generate random number between 1 and 50
    secret_number = random.randint(1, 50)
    attempts = 0
    
    print("🎯 Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 50.")
    print("Try to guess it!\n")
    
    while True:
        try:
            # Get user input
            guess = input("Enter your guess (1-50): ")
            
            # Convert to integer
            guess = int(guess)
            attempts += 1
            
            # Check if guess is within valid range
            if guess < 1 or guess > 50:
                print("Please enter a number between 1 and 50.")
                continue
            
            # Check the guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You got it right!")
                print(f"The number was {secret_number}")
                print(f"It took you {attempts} attempts.")
                break
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
                
        except ValueError:
            print("❌ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for playing! Goodbye!")
            break

def main():
    """Main function to run the game"""
    while True:
        number_guessing_game()
        
        # Ask if user wants to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again not in ['y', 'yes']:
            print("👋 Thanks for playing! Goodbye!")
            break
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()