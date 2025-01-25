import pygame
def display_alphabet(used_letters):
    """
    Affiche l'alphabet à l'écran. Les lettres déjà utilisées sont grisées.
    """
    font = pygame.font.Font(None, 36)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x_start = 50
    y_start = 450
    spacing = 40
    for i, letter in enumerate(alphabet):
        color = (100, 100, 100) if letter.lower() in used_letters else black
        text = font.render(letter, True, color)
        screen.blit(text, (x_start + (i % 13) * spacing, y_start + (i // 13) * 50))

def handle_letter_click(used_letters):
    """
    Gère les clics sur les lettres de l'alphabet.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x_start = 50
    y_start = 450
    spacing = 40
    for i, letter in enumerate(alphabet):
        rect = pygame.Rect(x_start + (i % 13) * spacing, y_start + (i // 13) * 50, 30, 30)
        if rect.collidepoint(pygame.mouse.get_pos()) and letter.lower() not in used_letters:
            return letter.lower()  # Renvoie la lettre cliquée
    return None
def main():
    name = get_player_name()
    count, start_image, random_word, word_guess = choose_difficulty()

    history = []  # Liste des lettres déjà tapées
    letters = list(random_word)

    running = True
    while running:
        screen.fill(white)
        display_title()
        display_word(word_guess)
        screen.blit(game_steps[10 - count], [180, 60])  # Afficher l'image actuelle
        display_alphabet(history)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                letter = handle_letter_click(history)
                if letter:  # Une lettre a été cliquée
                    history.append(letter)

                    if letter in letters:
                        for i, charactere in enumerate(letters):
                            if letter == charactere:
                                word_guess[i] = letter  # Remplace '_' par la lettre correcte
                    else:  # Lettre incorrecte
                        count -= 1

        # Vérifier si le mot est trouvé
        if "_" not in word_guess:
            print(f"Congratulations! You found the word: {random_word}")
            score = len(word_guess) * count
            save_score(name, score)
            return