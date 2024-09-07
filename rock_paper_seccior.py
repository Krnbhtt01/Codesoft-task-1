import random

def game():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    user = input("Enter your choice (rock/paper/scissors): ").lower()
    while user not in choices:
        user = input("Invalid input. Enter your choice (rock/paper/scissors): ").lower()

    print(f"\nComputer chose {computer}!")

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

def main():
    play_again = "yes"
    while play_again.lower() == "yes":
        game()
        play_again = input("\nPlay again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Play again? (yes/no): ").lower()

if __name__ == "__main__":
    main()