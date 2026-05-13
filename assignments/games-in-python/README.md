# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. By completing this assignment, you will practice game logic, state tracking, and writing clear terminal output.

## 📝 Tasks

### 🛠️	Set Up Core Game Logic

#### Description
Create the base Hangman workflow. Your program should choose a secret word from a predefined list, accept one-letter guesses from the player, and track game progress after each guess.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list.
- Display the word progress using underscores for unguessed letters (example: `_ _ _ _ _`).
- Accept a single letter guess from the user each turn.
- Reveal all matching letter positions when a correct guess is entered.
- Keep track of guessed letters to avoid duplicate processing.


### 🛠️	Handle Win/Loss Conditions and Feedback

#### Description
Finish the game experience by handling incorrect guesses, ending conditions, and player feedback messages.

#### Requirements
Completed program should:

- Start with a fixed number of incorrect attempts (for example, 6).
- Decrease remaining attempts only for incorrect new guesses.
- End the game with a win message when all letters in the word are revealed.
- End the game with a lose message when attempts reach 0, and show the secret word.
- Display helpful turn-by-turn feedback, including remaining attempts and letters guessed.
