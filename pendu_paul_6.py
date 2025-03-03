import random as rd
import pygame
import os

# Path to the main project directory
BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/Pendu/pendu"

# Paths to specific resource directories
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

# Initialize Pygame
pygame.init()

# Main screen resolution
screen_resolution = (800, 600)

# Create screen object and set window title
screen = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption("Hangman Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (200, 220, 240)

# Load font
ubuntu_font = pygame.font.Font(os.path.join(BASE_DIR, "Ubuntu-Regular.ttf"), 36)

# Load game images
game_steps = []
for num in range(2, 13):
    try:
        game_steps.append(pygame.image.load(os.path.join(IMAGE_DIR, f"p{num}.png")))
    except pygame.error as e:
        print(f"Error loading image p{num}.png: {e}")

# Initialize Pygame mixer for sound
pygame.mixer.init()

# Load sounds
try:
    loose_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "loose.wav"))
except pygame.error as e:
    print(f"Error loading sound: {e}")
    loose_sound = None

try:
    win_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "win_1.wav"))
except pygame.error as e:
    print(f"Error loading sound: {e}")
    win_sound = None

# Function to display the game title
def display_title():
    title_text = ubuntu_font.render("HANGMAN", True, black)
    title_rect = title_text.get_rect(center=(screen_resolution[0] // 2, 30))
    screen.blit(title_text, title_rect)

# Function to get the player's name for the scoreboard
def get_player_name():
    input_box = pygame.Rect(250, 200, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
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

        prompt_text = ubuntu_font.render("Enter your name:", True, black)
        screen.blit(prompt_text, (250, 150))

        txt_surface = ubuntu_font.render(text, True, black)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

# Function to insert a new word into the game
def insert_word_interface():
    input_box = pygame.Rect(250, 200, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    success_message = ''
    error_message = ''
    word_saved = False

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
                        if text.isalpha():
                            try:
                                with open("mots.txt", "r", encoding="utf-8") as file:
                                    words = file.read().splitlines()
                                if text in words:
                                    error_message = "Word already exists."
                                else:
                                    with open("mots.txt", "a", encoding="utf-8") as file:
                                        file.write(text + "\n")
                                    success_message = "Word added successfully!"
                                    text = ''
                                    error_message = ''
                                    word_saved = True
                            except FileNotFoundError:
                                error_message = "File 'mots.txt' not found."
                        else:
                            error_message = "Please enter a valid word (letters only)."
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        if word_saved:
            screen.fill(white)
            display_title()

            instruction_text = ubuntu_font.render("Enter a word:", True, black)
            instruction_rect = instruction_text.get_rect(center=(screen_resolution[0] // 2, 150))
            screen.blit(instruction_text, instruction_rect)

            success_text = ubuntu_font.render(success_message, True, (0, 128, 0))  # Green for success
            screen.blit(success_text, (250, 300))

            pygame.display.flip()
            pygame.time.wait(1500)  # Wait 1.5 seconds before returning to the menu
            return

        screen.fill(white)
        display_title()

        instruction_text = ubuntu_font.render("Enter a word:", True, black)
        instruction_rect = instruction_text.get_rect(center=(screen_resolution[0] // 2, 150))
        screen.blit(instruction_text, instruction_rect)

        if error_message:
            error_text = ubuntu_font.render(error_message, True, (255, 0, 0))  # Red for error
            screen.blit(error_text, (250, 350))

        txt_surface = ubuntu_font.render(text, True, black)
        input_box.w = max(300, txt_surface.get_width() + 10)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

# Function to choose game difficulty
def choose_difficulty():
    options = ["Easy", "Hard"]
    selected = 0
    running = True

    while running:
        screen.fill(white)
        display_title()

        for i, option in enumerate(options):
            color = black if i == selected else (100, 100, 100)
            text = ubuntu_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_resolution[0] // 2, 300 + 50 * i))
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
                    if selected == 0:  # Easy
                        count = 10
                        start_image = 2  # p2.png
                    else:  # Hard
                        count = 5
                        start_image = 6  # p6.png

                    screen.fill(white)
                    display_title()
                    screen.blit(game_steps[start_image - 2], [180, 60])

                    random_word = load_word()
                    word_guess = ['_' for _ in random_word]

                    display_word(word_guess)
                    pygame.display.flip()
                    return count, start_image, random_word, word_guess

# Function to display the scoreboard interface
def show_scoreboard_interface():
    font = pygame.font.Font(os.path.join(BASE_DIR, "Ubuntu-Regular.ttf"), 16)
    back_button = pygame.Rect(20, 20, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return

        try:
            with open("score.txt", "r", encoding="utf-8") as file:
                scores = file.readlines()
        except FileNotFoundError:
            scores = ["No scores available."]

        screen.fill(white)
        display_title()

        title_text = font.render("Scoreboard", True, black)
        title_rect = title_text.get_rect(center=(screen_resolution[0] // 2, 75))
        screen.blit(title_text, title_rect)

        scores_per_column = 13
        columns = [scores[i:i + scores_per_column] for i in range(0, len(scores), scores_per_column)]

        x_offset = 100
        y_offset = 100

        for col_idx, column in enumerate(columns):
            for idx, score in enumerate(column):
                score_text = font.render(f"{idx + 1 + col_idx * scores_per_column}. {score.strip()}", True, black)
                screen.blit(score_text, (x_offset, y_offset))
                y_offset += 40
            x_offset += 200

        pygame.draw.rect(screen, (200, 200, 200), back_button)
        back_text = font.render("Back", True, black)
        back_rect = back_text.get_rect(center=back_button.center)
        screen.blit(back_text, back_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

# Function to load words from a file
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
    random_word = rd.choice(words).lower()
    return random_word

# Function to display the secret word
def display_word(word_guess):
    word_display = " ".join(word_guess)
    text = ubuntu_font.render(word_display, True, black)
    screen.fill(white)
    display_title()
    screen.blit(text, (350, 500))
    pygame.display.flip()

# Function to save the score to a file
def save_score(name, score):
    with open("score.txt", "a") as file:
        file.write(f"{name} : {score} pts\n")

# Function to display the scoreboard
def display_scores():
    try:
        with open("score.txt", "r") as file:
            scores = file.read().splitlines()
            if scores:
                print("\nScoreboard:")
                for score in scores:
                    print(score)
            else:
                print("\nScoreboard empty.")
    except FileNotFoundError:
        print("File 'score.txt' does not exist. Create it before playing.")

# Function to get letter input from the user
def get_letter_input():
    input_box = pygame.Rect(50, 90, 50, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(os.path.join(BASE_DIR, "Ubuntu-Regular.ttf"), 36)
    border_width = 3

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
                        return text.lower()
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 1:
                            text += event.unicode

        txt_surface = font.render(text, True, black)
        input_box.w = max(50, txt_surface.get_width() + 10)

        text_x = input_box.x + (input_box.width - txt_surface.get_width()) // 2
        text_y = input_box.y + 5 + 3
        screen.blit(txt_surface, (text_x, text_y))

        pygame.draw.rect(screen, black, input_box, border_width, border_radius=12)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

# Function to display the history of used letters
def display_history(history):
    history_text = "Used letters: " + ", ".join(history)
    font = pygame.font.Font(os.path.join(BASE_DIR, "Ubuntu-Regular.ttf"), 30)

    history_surface = font.render(history_text, True, black)

    history_rect = pygame.Rect(640, 55, 150, 450)
    pygame.draw.rect(screen, blue, history_rect)
    border_radius = 10
    border_rect = history_rect.inflate(2, 2)
    pygame.draw.rect(screen, black, border_rect, 1, border_radius)

    title_font = pygame.font.Font(os.path.join(BASE_DIR, "Ubuntu-Regular.ttf"), 20)
    title_surface = title_font.render("Wrong letters:", True, black)
    screen.blit(title_surface, (history_rect.x + 5, history_rect.y + 5))

    available_height = history_rect.height - 40
    max_letters_height = available_height // 35

    history_lines = []
    current_line = []
    for letter in history:
        if len(", ".join(current_line + [letter])) < 3:
            current_line.append(letter)
        else:
            history_lines.append(", ".join(current_line))
            current_line = [letter]

    if current_line:
        history_lines.append(", ".join(current_line))

    text_height = len(history_lines) * 35
    y_offset = history_rect.y + 40
    for line in history_lines[:max_letters_height]:
        letter_surface = font.render(line, True, black)
        screen.blit(letter_surface, (history_rect.x + (history_rect.width - letter_surface.get_width()) // 2, y_offset))
        y_offset += 35

    pygame.display.flip()

# Function to display the end screen with a message
def display_end_screen(message, color, button_text, back_action):
    lose_message = ubuntu_font.render(message, True, color)
    back_button = pygame.Rect(30, 40, 150, 50)
    reduced_font = pygame.font.Font(None, 30)
    back_text = reduced_font.render(button_text, True, black)
    back_rect = back_text.get_rect(center=back_button.center)
    screen.blit(lose_message, (200, 500))
    screen.blit(back_text, back_rect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    back_action()
                    return

# Function to check the game state
def check_game_state(word_guess, random_word, count):
    if "_" not in word_guess:
        return "win"
    elif count <= 0:
        return "lose"
    return "playing"

# Function to validate the input letter
def valid_letter(letter, word_guess, history):
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single alphabetic letter.")
        return False

    if letter in word_guess or letter in history:
        print("You have already guessed this letter.")
        return False

    return True

# Main game function
def main():
    name = get_player_name()
    count, start_image, random_word, word_guess = choose_difficulty()

    history = []
    letters = list(random_word)
    word_guess = ['_' for _ in letters]

    running = True

    while running:
        screen.fill(white)
        display_word(word_guess)
        display_history(history)

        if 0 <= (10 - count) < len(game_steps):
            screen.blit(game_steps[10 - count], [180, 60])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

        if count > 0:
            letter = get_letter_input()

            if not valid_letter(letter, word_guess, history):
                continue

            if letter in letters:
                update_word_guess(letter, letters, word_guess)
            else:
                count -= 1
                history.append(letter)

        game_state = check_game_state(word_guess, random_word, count)
        if game_state == "win":
            display_end_screen(f"Congratulations! The word was: {random_word}", (0, 128, 0), "Menu", menu)
            return
        elif game_state == "lose":
            display_end_screen(f"Game Over! The word was: {random_word}", (255, 0, 0), "Menu", menu)
            return

# Main menu function
def menu():
    menu_options = ["Play now", "Enter a word", "Scoreboard", "Exit"]
    selected_index = 0
    running = True
    game_running = False
    while running:
        screen.fill(white)
        display_title()

        for i, option in enumerate(menu_options):
            if i == selected_index:
                text = ubuntu_font.render(option, True, black)
            else:
                text = ubuntu_font.render(option, True, (100, 100, 100))
            text_rect = text.get_rect(center=(screen_resolution[0] // 2, 200 + 50 * i))
            screen.blit(text, text_rect)

        pygame.display.flip()

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
                        game_running = True
                    elif menu_options[selected_index] == "Enter a word":
                        insert_word_interface()
                    elif menu_options[selected_index] == "Scoreboard":
                        show_scoreboard_interface()
                    elif menu_options[selected_index] == "Exit":
                        running = False

        if game_running:
            random_word = load_word()
            word_guess = ['_' for _ in random_word]
            main()
            game_running = False

    pygame.quit()
    exit()

if __name__ == "__main__":
    menu()
