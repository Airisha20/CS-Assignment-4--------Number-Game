import random

def play_game():
    print("\nWELCOME TO THE NUMBER GUESSING GAME!")
    print("I'm thinking of a number between 1 and 100.")
    
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.\n")
            elif guess > number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Correct! You guessed the number {number} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.\n")

    return attempts

while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! Goodbye!")
        break
