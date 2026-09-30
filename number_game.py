import random

def play_game():
    print("--- Welcome to the Guessing Game! ---")
    print("I am thinking of a number between 1 and 20.")
    
    # Generate target number
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ")
        attempts += 1
        
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            return
        elif guess < secret_number:
            print("📈 Too low! Try a higher number.")
        else:
            print("📉 Too high! Try a lower number.")
            
    print(f"💀 Game over! The correct number was {secret_number}.")

if __name__ == "__main__":
    play_game()