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
    loose_sound = loose_sound = pygame.mixer.Sound(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\sounds\loose.wav")
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

        # Ajout du texte "Enter your name:" au-dessus de la boîte de texte
        prompt_text = font.render("Enter your name:", True, black)
        screen.blit(prompt_text, (250, 150))  # Position au-dessus de l'input box

        txt_surface = font.render(text, True, black)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        pygame.time.Clock().tick(30)


def insert_word_interface():
    input_box = pygame.Rect(250, 200, 300, 50)  # Zone de texte pour entrer un mot
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 36)
    success_message = ''
    error_message = ''
    word_saved = False  # Drapeau pour détecter si le mot a été enregistré

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
                        if text.isalpha():  # Vérifie que le mot contient uniquement des lettres
                            try:
                                with open("mots.txt", "r", encoding="utf-8") as file:
                                    words = file.read().splitlines()
                                if text in words:
                                    error_message = "Word already exists."
                                else:
                                    with open("mots.txt", "a", encoding="utf-8") as file:
                                        file.write(text + "\n")
                                    success_message = "Word added successfully!"
                                    text = ''  # Réinitialiser la zone de texte
                                    error_message = ''
                                    word_saved = True  # Le mot est enregistré
                            except FileNotFoundError:
                                error_message = "File 'mots.txt' not found."
                        else:
                            error_message = "Please enter a valid word (letters only)."
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Si le mot est enregistré, afficher le message et attendre
        if word_saved:
            screen.fill(white)
            display_title()

            # Instructions pour l'utilisateur
            instruction_text = font.render("Enter a word:", True, black)
            instruction_rect = instruction_text.get_rect(center=(screen_résolution[0] // 2, 150))
            screen.blit(instruction_text, instruction_rect)

            # Afficher le message de succès
            success_text = font.render(success_message, True, (0, 128, 0))  # Vert pour le succès
            screen.blit(success_text, (250, 300))

            pygame.display.flip()  # Mettre à jour l'affichage
            pygame.time.wait(2000)  # Attendre 2 secondes avant de revenir au menu
            return  # Quitte la fonction pour revenir au menu principal

        screen.fill(white)
        display_title()

        # Instructions pour l'utilisateur
        instruction_text = font.render("Enter a word:", True, black)
        instruction_rect = instruction_text.get_rect(center=(screen_résolution[0] // 2, 150))
        screen.blit(instruction_text, instruction_rect)

        # Afficher les messages d'erreur
        if error_message:
            error_text = font.render(error_message, True, (255, 0, 0))  # Rouge pour les erreurs
            screen.blit(error_text, (250, 350))

        # Afficher la zone de texte
        txt_surface = font.render(text, True, black)
        input_box.w = max(300, txt_surface.get_width() + 10)
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

        # Show option easy/hard
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
                    if selected == 0:  # Easy
                        count = 10
                        start_image = 2  # p2.png
                    else:  # Hard
                        count = 5
                        start_image = 6  # p6.png

                    # Charger l'image de départ
                    screen.fill(white)
                    display_title()
                    screen.blit(game_steps[start_image - 2], [180, 60])  # Afficher l'image p{start_image}.png

                    # Charger le mot secret
                    random_word = load_word()
                    word_guess = ['_' for _ in random_word]

                    # Afficher le mot avec '_'
                    display_word(word_guess)
                    pygame.display.flip()

                    # Retourner les valeurs nécessaires pour le jeu
                    return count, start_image, random_word, word_guess
                
def show_scoreboard_interface():
    font = pygame.font.Font(None, 36)
    back_button = pygame.Rect(20, 20, 100, 50)  # Bouton pour retourner au menu

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return  # Retourne au menu principal

        # Lire les scores du fichier
        try:
            with open("score.txt", "r", encoding="utf-8") as file:
                scores = file.readlines()
        except FileNotFoundError:
            scores = ["No scores available."]

        # Affichage de l'interface
        screen.fill(white)
        display_title()

        # Afficher le titre du scoreboard
        title_text = font.render("Scoreboard", True, black)
        title_rect = title_text.get_rect(center=(screen_résolution[0] // 2, 50))
        screen.blit(title_text, title_rect)

        # Afficher les scores
        y_offset = 100
        for idx, score in enumerate(scores):
            score_text = font.render(f"{idx + 1}. {score.strip()}", True, black)
            screen.blit(score_text, (100, y_offset))
            y_offset += 40  # Espacement entre les scores

        # Afficher le bouton "Back"
        pygame.draw.rect(screen, (200, 200, 200), back_button)
        back_text = font.render("Back", True, black)
        back_rect = back_text.get_rect(center=back_button.center)
        screen.blit(back_text, back_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(30)



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

# Function to show the scoreboard (removed terminal printing)
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

# Function main for gameplay
import pygame

def main():
    name = get_player_name()  # Get the player's name from input box
    count, start_image, random_word, word_guess = choose_difficulty()  # Difficulty selection

    history = []  # List for letters already tapped
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
                
                # Show the win message on screen
                win_message = ubuntu_font.render(f"Congratulations! You found the word: {random_word}", True, (0, 128, 0))
                score_message = ubuntu_font.render(f"Your score: {score} pts", True, (0, 128, 0))
                screen.blit(win_message, (200, 500))
                screen.blit(score_message, (200, 550))

                # Display the "Return to Menu" button
                back_button = pygame.Rect(350, 600, 150, 50)
                pygame.draw.rect(screen, (200, 200, 200), back_button)
                back_text = ubuntu_font.render("Return to Menu", True, black)
                back_rect = back_text.get_rect(center=back_button.center)
                screen.blit(back_text, back_rect)

                pygame.display.flip()

                # Wait for the player to click the "Return to Menu" button
                menu_return = False
                while not menu_return:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if back_button.collidepoint(event.pos):
                                menu_return = True

                menu()  # Return to the menu
                return

        else:
            if start_image == 1:  # Easy mode
                screen.blit(game_steps[11], [180, 60])  # Display p12.png
            # Play the losing sound
            if loose_sound:
                loose_sound.play()
            print("\n--- GAME OVER ---")
            print(f"You couldn't guess the word: {random_word}")
            
            # Show the game over message on screen
            game_over_message = ubuntu_font.render(f"Game Over! The word was: {random_word}", True, (255, 0, 0))
            screen.blit(game_over_message, (200, 500))

            # Display the "Return to Menu" button
            back_button = pygame.Rect(30, 40, 150, 50)
            reduced_font = pygame.font.Font(None, 30)
            back_text = reduced_font.render("Return to Menu", True, black)
            back_rect = back_text.get_rect(center=(80, 60))
            screen.blit(back_text, back_rect)
            pygame.display.flip()

            # Wait for the player to click the "Return to Menu" button
            menu_return = False
            while not menu_return:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back_button.collidepoint(event.pos):
                            menu_return = True

            menu()  # Return to the menu
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
                        insert_word_interface()
                    elif menu_options[selected_index] == "Scoreboard":
                        show_scoreboard_interface()
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