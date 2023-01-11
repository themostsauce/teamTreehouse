import random

def welcome_message():
    welcome_message = "Welcome to the number guessing game!"
    print("-"*len(welcome_message) + "\n"+ welcome_message + "\n" + "-"*len(welcome_message) )

def start_game():
    welcome_message()
    random_number = random.randint(1,10)
    guess_counter = 1
    high_score = 0
    play_game = (input("Would you like to play? y/n: "))

    while play_game.lower() == "y" or play_game.lower() == "yes":
        try:
            user_guess = int(input("\nPlease input a number between 1-10: "))
            if user_guess > 10 or user_guess < 1:
                raise ValueError("Sorry, that's an invalid input.")
        except ValueError as err:
            print(("{}".format(err)))
        else:
            while user_guess != random_number:
                guess_counter += 1
                if user_guess > random_number:
                    print("Close! Go lower")
                    user_guess = int(input("Please input a number between 1-10: "))
                elif user_guess < random_number:
                    print("Close! Go higher")
                    user_guess = int(input("Please input a number between 1-10: "))
            print("You got it! Your score: {} ".format(guess_counter))
            if high_score == 0:
                high_score = guess_counter
                print("Congrats! You currently have the highest score!")
            elif guess_counter < high_score:
                high_score = guess_counter
                print("Congrats! You now have the highest score")
            else:
                print("You didn't beat the high score. Better luck next time!")  
            print("Current High Score: {}".format(high_score))
            guess_counter = 1
            play_game = input("Do you wanna play again? y/n: ")
    print("Thanks for playing! See you again soon :)")
    
if __name__ == '__main__':
    start_game()