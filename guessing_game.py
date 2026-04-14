import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")
    print("-" * 40)
    
    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You got it in {attempts} attempts!")
                print(f"The number was {secret_number}")
                return True
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
                
            # Give hint for remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"💡 Hint: {remaining} attempts remaining!\n")
                
        except ValueError:
            print("❌ Please enter a valid number!")
            continue
    
    # Game over
    print(f"\n💥 Game Over! The number was {secret_number}")
    return False

# Play the game
if __name__ == "__main__":
    while True:
        number_guessing_game()
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break
        print("\n" + "="*50 + "\n")