# 🎮 Pendu Game

**Pendu** is a **word-guessing game** developed using **Python** and **Pygame**. In this game, the player has to guess the hidden word by suggesting letters within a limited number of attempts. The game follows the classic rules of Hangman, where each incorrect guess results in part of a stick figure being drawn. The game also tracks player scores and saves them in a score file.

## 📂 Repository Contents

The repository contains the following files:

- **`pendu.py`** – The main Python script that contains the game logic, graphical interface, and handles user input through Pygame.
- **`mots.txt`** – A text file containing a list of possible words for the player to guess. The game randomly selects one of these words as the secret word.
- **`score.txt`** – A text file that stores the scores of players. The file keeps track of the best scores.
- **`README.md`** – Project documentation.
- **`.gitignore`** – Specifies files and directories to be ignored by Git.
- **`assets/`** – A folder containing images used for the game (e.g., the hangman figure and background).

## 🛠️ Technologies Used

- **Python** – The primary programming language used for this game.
- **Pygame** – A library used to handle the game window, user input, and graphical rendering.
- **Text Files**:
  - **`mots.txt`** – Stores the list of possible words for the game.
  - **`score.txt`** – Stores the scores of the players (can be updated each time the game ends).
