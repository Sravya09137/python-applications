# Pig Dice Game

A command-line Python implementation of the classic Pig Dice Game for 2–4 players.

## Features

* Supports 2–4 players
* Interactive command-line gameplay
* Random dice rolls
* Turn-based scoring
* Players can choose when to stop rolling and keep their points
* Rolling a 1 ends the current turn and resets the turn score
* Tracks each player's total score
* Declares the winner when the game reaches the target score

## How It Works

1. The application asks the user whether they are ready to play.
2. The number of players is entered, with support for 2–4 players.
3. Each player takes a turn and chooses whether to roll the die.
4. Each successful roll adds to the player's current turn score.
5. Rolling a 1 resets the current turn score to zero and ends the turn.
6. A player can choose to stop rolling and add their current turn score to their total score.
7. The game continues until a player reaches the target score of 50 points.
8. The player with the highest score is declared the winner.

## Concepts Practiced

* Python functions
* Random number generation
* Lists
* Loops
* Conditional statements
* User input
* Input validation
* Turn-based game logic
* Score tracking

## Technology

* Python 3

## How to Run

Run the following command from the project directory:

```bash
python PigDiceGame.py
```

## Project Structure

```text
Pig-Dice-Game/
├── README.md
└── PigDiceGame.py
```

## Purpose

This project was developed to practice Python programming fundamentals by implementing a multiplayer dice game with randomization, input validation, turn management, and score tracking.
