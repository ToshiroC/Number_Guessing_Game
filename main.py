import random
def number_guessing_game():
    print("\nThis is a number guessing game. The computer will think of a random number between 1 and 100 and you have to guess what it is.")

    #Generates a random integer between 1 and 100
    number = random.randint(1, 100)

    #Initialising the guess variable
    guess = 0

    #While loop to define what happens while the guess is incorrect. If it's lower than the number, then it'll say "Too low" and vice versa
    while guess != number:
        guess = int(input("\nEnter your guess here: "))
        if guess < number:
            print("\nToo low")
        elif guess > number:
            print("\nToo high")

    print("\nCongratulations! You have guessed the number.")

    #Allows the user to repeat the game by running the function again or to end the game with a thank you message
    again = input("\nDo you want to play again? (Y/N) ").upper()

    if again == "Y":
        number_guessing_game()
    else:
        print("\nThank you for playing. I hope you enjoyed the game.")

#Calling the function for the game to start the game for the first time
number_guessing_game()