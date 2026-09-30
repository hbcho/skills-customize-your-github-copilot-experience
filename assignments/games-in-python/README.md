
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, conditionals, random selection, and user input. The completed program should let a player guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Hidden Word

#### Description
Create the word-selection and display logic for a Hangman game. The program should choose a word from a predefined list and show the player's progress as letters are revealed.

#### Requirements
Completed program should:

- Store multiple words in a predefined list.
- Randomly select one word at the start of each game.
- Accept letter guesses from the player.
- Display the current progress using an underscore format such as `_ _ _`.
- Reveal correctly guessed letters in their matching positions.

### 🛠️ Implement the Guessing Game

#### Description
Add the game loop and result handling so the player can continue guessing until the hidden word is completed or no attempts remain.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining.
- Update the remaining attempts after an incorrect guess.
- End when the player guesses the entire word or exhausts the available attempts.
- Display a clear win message when the word is guessed.
- Display a clear lose message and reveal the word when the attempts are exhausted.
