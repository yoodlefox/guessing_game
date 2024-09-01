# Unleashing the Fun: Building a Number Guessing Game in Python

## Introduction
Ever found yourself yearning for a classic guessing game to sharpen your logical thinking and coding skills? Well, you're in for a treat! In this blog post, I'm excited to introduce you to a fun and engaging number guessing game I developed using Python. Whether you're a coding newbie or an experienced developer, this project showcases fundamental Python concepts while providing an interactive experience that you can enjoy.

## Exploring the Code
### The Player Class
The `Player` class is designed to represent a participant in the game, either the human player or the computer. It keeps track of the player’s name and score, allowing for a simple yet effective way to manage game participants.

```
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

    def __repr__(self):
        return f"{self.name} has {self.score} point(s)."
```

This class features methods to update and display the player’s score, ensuring that the competition remains exciting and fair.

### The GuessingGame Class
The `GuessingGame` class is the heart of our game, where most of the action happens. It handles everything from managing the game state to interacting with the player.

```
class GuessingGame:
    def __init__(self):
        self.player = Player("User")
        self.computer = Player("Computer")
        self.number_to_guess = random.randint(1, 100)
        self.max_attempts = 7
        self.remaining_attempts = self.max_attempts
        self.history = []
        self.lower_bound = 1
        self.upper_bound = 100

    def play(self):
        print("Welcome to the guessing game!")
        print("You need to guess a number between 1 and 100.")
        print(f"You have {self.max_attempts} attempts.\n")

        while self.remaining_attempts > 0:
            print(f"Remaining attempts: {self.remaining_attempts}")
            print(f"Current range: {self.lower_bound} - {self.upper_bound}")
            print(f"Already guessed numbers: {self.history}")

            try:
                guess = int(input("Enter a number: "))
            except ValueError:
                print("Please enter a valid number.\n")
                continue

            if guess in self.history:
                print("You have already guessed this number. Try another.\n")
                continue

            if guess < self.lower_bound or guess > self.upper_bound:
                print(f"Please enter a number between {self.lower_bound} and {self.upper_bound}.\n")
                continue

            self.history.append(guess)
            self.remaining_attempts -= 1

            if guess < self.number_to_guess:
                self.lower_bound = guess + 1
                print("It's higher!\n")
            elif guess > self.number_to_guess:
                self.upper_bound = guess - 1
                print("It's lower!\n")
            else:
                print("Congratulations! You guessed the correct number!")
                self.player.add_point()
                break

        if self.remaining_attempts == 0 and guess != self.number_to_guess:
            print(f"You lost! The correct number was {self.number_to_guess}.")
            self.computer.add_point()

        self.display_scores()
        self.play_again()

    def display_scores(self):
        print(f"\nScores:\n{self.player}\n{self.computer}\n")

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            self.reset()
            self.play()
        else:
            print("Thank you for playing!")

    def reset(self):
        self.number_to_guess = random.randint(1, 100)
        self.remaining_attempts = self.max_attempts
        self.history = []
        self.lower_bound = 1
        self.upper_bound = 100
```

The `GuessingGame` class orchestrates the entire game flow, from accepting guesses to updating the game state and checking win conditions. It also manages game replays and scorekeeping, making sure the game is both challenging and enjoyable.

## Conclusion
Building a number guessing game in Python has been a fantastic exercise in programming and game design. This project demonstrates essential Python skills while offering a fun and interactive way to practice coding. Whether you're a beginner looking for a new challenge or an experienced coder seeking a simple project, this game has something for everyone. Dive into the code, play the game, and let me know what you think!
