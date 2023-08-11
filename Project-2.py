# ROCK PAPER SCISSORS GAME AGAINST YOUR OPPONENT/COMPUTER :

import random # Generates random values/numbers from given lists : 
    
def user(): # This function helps the user to choose the value between rock, paper and scissors : 
    while True:
        print("Are you ready to play Rock/Paper/Scissors?")
        input("Press any key to began playing : ")
        user_input = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else: # Below will find out whether the user has inputed the right or wrong value :
            print("Invalid choice. Please choose rock, paper, or scissors.")


def determine_winner(user_choice, computer_choice): # This function helps to determine who the winner is :
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main(): # This is the main function : 
    print("Welcome to Rock-Paper-Scissors!")
    while True: # Below will tell us what we chose : 
        user_choice = user()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer chose : ", computer_choice) # prints between rock, paper and scissors :
        print("You chose : ", user_choice) # prints between rock, paper and scissors : 
        result = determine_winner(user_choice, computer_choice) # This will call out the winner function :
        print(result)

        continue_playing = input("Do you want to play again? (yes/no): ") # This helps us to continue playing the game or not : 
        if continue_playing.lower() != "yes":
            print("Thank you for playing Rock-Paper-Scissors!")
            break

if __name__ == "__main__":
    main()
