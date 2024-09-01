import random

# Class representing a player
class Player:
    def __init__(self, name):
        self.name = name  # Initialize the player's name
        self.score = 0     # Initialize the player's score to 0

    def add_point(self):
        self.score += 1   # Increment the player's score by 1

    def __repr__(self):
        return f"{self.name} has {self.score} point(s)."  # Representation of the player's score


# Class representing the guessing game
class GuessingGame:
    def __init__(self):
        self.player = Player("User")  # Initialize the player with the name "User"
        self.computer = Player("Computer")  # Initialize the computer as a player
        self.number_to_guess = random.randint(1, 100)  # Randomly generate the number to guess between 1 and 100
        self.max_attempts = 7  # Set the maximum number of attempts to 7
        self.remaining_attempts = self.max_attempts  # Initialize remaining attempts
        self.history = []  # List to store the player's previous guesses
        self.lower_bound = 1  # Set the initial lower bound of the guessing range
        self.upper_bound = 100  # Set the initial upper bound of the guessing range

    def play(self):
        print("Welcome to the guessing game!")
        print("You need to guess a number between 1 and 100.")
        print(f"You have {self.max_attempts} attempts.\n")

        # Main game loop
        while self.remaining_attempts > 0:
            print(f"Remaining attempts: {self.remaining_attempts}")
            print(f"Current range: {self.lower_bound} - {self.upper_bound}")
            print(f"Already guessed numbers: {self.history}")

            try:
                guess = int(input("Enter a number: "))  # Ask the user to enter a number
            except ValueError:
                print("Please enter a valid number.\n")
                continue  # If input is not a valid number, ask again

            if guess in self.history:
                print("You have already guessed this number. Try another.\n")
                continue  # If the number was already guessed, ask again

            if guess < self.lower_bound or guess > self.upper_bound:
                print(f"Please enter a number between {self.lower_bound} and {self.upper_bound}.\n")
                continue  # If the guess is outside the current range, ask again

            self.history.append(guess)  # Add the guess to the history
            self.remaining_attempts -= 1  # Decrement the remaining attempts

            # Adjust the guessing range or end the game if the guess is correct
            if guess < self.number_to_guess:
                self.lower_bound = guess + 1
                print("It's higher!\n")
            elif guess > self.number_to_guess:
                self.upper_bound = guess - 1
                print("It's lower!\n")
            else:
                print("Congratulations! You guessed the correct number!")
                self.player.add_point()  # Add a point to the player's score
                break  # Exit the loop if the guess is correct

        # If no attempts are left and the number wasn't guessed, the computer wins
        if self.remaining_attempts == 0 and guess != self.number_to_guess:
            print(f"You lost! The correct number was {self.number_to_guess}.")
            self.computer.add_point()  # Add a point to the computer's score

        self.display_scores()  # Display the current scores
        self.play_again()  # Ask the user if they want to play again

    def display_scores(self):
        print(f"\nScores:\n{self.player}\n{self.computer}\n")  # Display both player and computer scores

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            self.reset()  # Reset the game if the user wants to play again
            self.play()  # Start a new game
        else:
            print("Thank you for playing!")  # End the game if the user doesn't want to play again

    def reset(self):
        self.number_to_guess = random.randint(1, 100)  # Generate a new number to guess
        self.remaining_attempts = self.max_attempts  # Reset the remaining attempts
        self.history = []  # Clear the guess history
        self.lower_bound = 1  # Reset the lower bound
        self.upper_bound = 100  # Reset the upper bound


# Start the game
game = GuessingGame()
game.play()
