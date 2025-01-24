# Import Libraries
import random as rd
import pygame
import os

# way to project main file
BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/Pendu/pendu"

# way to spécific files
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

# PYGAME ADDING PART
pygame.init()
# main screen size
screen_résolution = (800, 600)
# screen object and name
screen = pygame.display.set_mode(screen_résolution)
pygame.display.set_caption("Hangman Game")

# colors used
black = (0, 0, 0)
white = (255, 255, 255)

# font used
ubuntu_font = pygame.font.Font(os.path.join(BASE_DIR, "Ubuntu-Regular.ttf"), 36)

# images list in order 0 -> 12
game_steps = []
for num in range(2, 13):
    try:
        game_steps.append(pygame.image.load(os.path.join(IMAGE_DIR, f"p{num}.png")))
    except pygame.error as e:
        print(f"Erreur lors du chargement de l'image p{num}.png : {e}")

# mixer for sound
pygame.mixer.init()

# sounds call
try:
    loose_sound = pygame.mixer.Sound(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\sounds\loose.wav")
except pygame.error as e:
    print(f"Error loading sound: {e}")
    loose_sound = None

# Title
def display_title():
    title_text = ubuntu_font.render("HANGMAN", True, black)
    title_rect = title_text.get_rect(center=(screen_résolution[0] // 2, 30))
    screen.blit(title_text, title_rect)

def get_player_name():
    input_box = pygame.Rect(250, 200, 300, 50)  # Position de la zone de texte pour le nom
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 36)
    user_name = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        user_name = text
                        return user_name
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(white)
        display_title()

        txt_surface = font.render(text, True, black)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

def choose_difficulty():
    font = pygame.font.Font(None, 36)
    options = ["Easy", "Hard"]
    selected = 0
    running = True
    while running:
        screen.fill(white)
        display_title()

        for i, option in enumerate(options):
            color = black if i == selected else (100, 100, 100)
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_résolution[0] // 2, 300 + 50 * i))
            screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        return 10, 2  # Easy mode
                    else:
                        return 5, 3  # Hard mode

# Insert a new word in the file
def insert_word():
    while True:
        try:
            new_word = str(input("\nEnter a new word (without spaces and in lowercase) : ")).strip().lower()
            if new_word.isalpha():      # Check if it is in 'a-z'
                with open("mots.txt", "r", encoding="utf-8") as file:
                    words = file.read().splitlines()
                    if new_word in words:
                        print("\nWord already exists.")
                    else:
                        with open("mots.txt", "a", encoding="utf-8") as file:
                            file.write(new_word + "\n")
                        print("Word added successfully.")
                        break
            else:
                print("Please enter only letters.")
        except ValueError:
            print("Error, invalid entry. Please retry")

# Function to read the file
def load_words():
    while True:
        try:
            with open("mots.txt", "r", encoding="utf-8") as file:
                words = file.read().splitlines()
                if not words:
                    print("File is empty. Add words before playing.")
                    return []
                return words
        except FileNotFoundError:
            print("File 'mots.txt' does not exist. Create it before playing.")
            return

# Function to load a random word from the file
def load_word():
    words = load_words()
    # random.choice to pick a random value
    random_word = rd.choice(words).lower()
    return random_word


# PYGAME ADDING
# Function to show the secret word
def display_word(word_guess):
    word_display = " ".join(word_guess)  # Joins the letters with spaces
    text = ubuntu_font.render(word_display, True, black)
    screen.fill(white)  # Clear the screen
    display_title()
    screen.blit(text, (350, 500))  # Draw the word at the specified position
    pygame.display.flip()  # Update the display

# Function to set the score in the file score.txt
def save_score(name, score):
    with open("score.txt", "a") as file:
        file.write(f"{name} : {score} pts\n")

# Function to show the scoreboard
def display_scores():
    try:
        with open("score.txt", "r") as file:
            scores = file.read().splitlines()
            if scores:
                print("\nScoreboard :")
                for score in scores:
                    print(score)
            else:
                print("\nScoreboard empty.")
    except FileNotFoundError:
        print("File 'score.txt' does not exist. Create it before playing.")

# Funtion main for every check and win condition
# Main function for gameplay
def main():
    name = get_player_name()  # Get the player's name from input box
    count, start_image = choose_difficulty()  # Difficulty selection

    print(f"Player: {name}")
    print(f"You have {count} moves to guess the word.")

    history = []  # List for letters already tapped
    print("\n--- START ---")
    words = load_words()  # Reading file...

    random_word = load_word()
    letters = list(random_word)
    word_guess = ['_' for _ in letters]

    running = True  # for Pygame
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

        if count > 0:  # While the user has chances
            letter = input("\nEnter a letter : ").lower()

            # Check if it is a good entry
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter one letter only, and only letters.")
                continue

            # Check if the letter is already found
            elif letter in word_guess or letter in history:
                print("You already guessed this letter.")
                continue

            # Check if it is correct or not
            if letter in letters:
                for i, charactere in enumerate(letters):
                    if letter == charactere:
                        word_guess[i] = letter  # Replace '_' with the correct letter
                print("Good answer!\n")
                print(" ".join(word_guess))
            else:  # Incorrect letter
                print("\nThis letter is not in the word.")
                count -= 1
                print(f"You have {count} moves left to guess the word.")
                history.append(letter)  # Incorrect letter added to history

            display_word(word_guess)  # Update the display with the current word guess

            # Update the hangman image
            if 0 <= (10 - count) < len(game_steps):
                screen.blit(game_steps[10 - count], [180, 60])
            pygame.display.flip()

            # Check if the word is found == WIN
            if "_" not in word_guess:
                print(f"Congratulations! You found the word: {random_word}")
                score = len(word_guess) * count  # Calculate the score
                print(f"Your score is {score} pts")
                save_score(name, score)  # Write in the score file
                return  # Exit the game loop after a win
        else:
            if start_image == 1:  # Easy mode
                screen.blit(game_steps[11], [180, 60])  # Display p12.png
            # Play the losing sound
            if loose_sound:
                loose_sound.play()
            print("\n--- GAME OVER ---")
            print(f"You couldn't guess the word: {random_word}")
            return

# Function main to call functions and show Menu
def menu():
    menu_options = ["Play now", "Enter a word", "Scoreboard", "Exit"]
    selected_index = 0
    running = True
    game_running = False  # Flag to control when the game is running

    while running:
        screen.fill(white)
        display_title()

        # Display menu options
        for i, option in enumerate(menu_options):
            if i == selected_index:
                text = ubuntu_font.render(option, True, black)
            else:
                text = ubuntu_font.render(option, True, (100, 100, 100))
            text_rect = text.get_rect(center=(screen_résolution[0] // 2, 200 + 50 * i))
            screen.blit(text, text_rect)

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_index] == "Play now":
                        game_running = True  # Start the game
                    elif menu_options[selected_index] == "Enter a word":
                        insert_word()
                    elif menu_options[selected_index] == "Scoreboard":
                        display_scores()
                    elif menu_options[selected_index] == "Exit":
                        running = False

        if game_running:  # Game logic begins when this flag is True
            random_word = load_word()
            word_guess = ['_' for _ in random_word]
            main()
            game_running = False  # Reset the game flag after the game ends

    pygame.quit()
    exit()


if __name__ == "__main__":
    menu()  # Start the game

