# Import Libraries
import random as rd
import pygame
import os

#PYGAME ADDING PART
pygame.init()
# main screen size
screen_résolution = (800, 600)
#screen object and name
screen = pygame.display.set_mode(screen_résolution)
pygame.display.set_caption("Hangman Game") 

# colors used
black = (0,0,0)
white = (255, 255, 255)

# font used
ubuntu_font = pygame.font.Font("desktop/Ubuntu-Regular.ttf", 36)

# images list in order 0 -> 13
game_steps = [
    pygame.image.load(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\images\p5.png"),
    pygame.image.load(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\images\p6.png"),
    pygame.image.load(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\images\p7.png"),
    pygame.image.load(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\images\p8.png"),
    pygame.image.load(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\images\p9.png"),
    pygame.image.load(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\images\p10.png"),
    pygame.image.load(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\images\p11.png"),
    pygame.image.load(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\images\p12.png"),
    pygame.image.load(r"C:\Users\Windows\Desktop\projets\1a\Pendu\pendu\images\p12.png")]

# mixer for sound
pygame.mixer.init()

# sounds call
loose_sound = pygame.mixer.Sound(r"Desktop\projets\1a\Pendu\pendu\sounds\loose.wav")

# Function Difficulty
def choose_difficulty():

    while True:

        try:
            level = int(input("Choose the difficulty (easy '1' / hard '2'): "))
            if level == 1:
                count = 10      # Level Easy : 10 moves
                return count
            elif level == 2:
                count = 5       # Level Hard : 5 moves
                return count
                
        except ValueError:
            print("\nInvalid entry, please choose between 1 and 2")


# Insert a new word in the file
def insert_word():

    while True:

        try:
            new_word = str(input("\nEnter a new word (without spaces and in lowercase) : ")).strip().lower()
            if new_word.isalpha():      # Check if it is in 'a-z'
                with open("mots.txt", "r", encoding="utf-8") as file:
                    words = file.read().splitlines()
                    if new_word in words:
                        print("\nWord already exist.")
                    else:
                        with open("mots.txt", "a", encoding="utf-8") as file:
                            file.write(new_word + "\n")
                        print("Word added successfully.")
                        break

            else:
                print("Please enter only letters.")

        except ValueError:
            print("Error, entry invalid please retry")

# Function to read the file
def load_words():
# Try to open, read and verify if the file exist and if it is not empty
    while True:
        try:
            with open("mots.txt", "r", encoding="utf-8") as file:
                words = file.read().splitlines()
                if not words:
                    print("File is empty. Add words before playing.")
                    return
                return words

        except FileNotFoundError:
            print("File 'mots.txt' does not exist. Create it before playing.")
            return
# Function to load a random word from variable from file
def load_word():
    words = load_words()
    # random.choice to pick a random value
    random_word = rd.choice(words).lower()
    return random_word        

# PYGAME ADDING
# Function to show the secret word
def display_word(word_guess,letters):
    random_word = load_word()
    letters = list(random_word)        # Separated each letters from the word
    word_guess = ['_' for _ in letters]
    word_display = " ".join(word_guess)
    text = ubuntu_font.render(word_display, True, black)
    screen.fill(white)
    screen.blit(text, (3,500))
    pygame.display.flip()


# Funtion main for every check and win condition
def main():
    name = input("\nEnter your name : ")
    history = []        # List for letter already tap
    print("\n--- START ---")
    words = load_words()        # Reading file...

    count = choose_difficulty()    # Ask difficulty
    ramdom_word = load_word()
    letters = list(ramdom_word)
    word_guess = ['_' for _ in letters]
    
    print(f"You have {count} moves to guess the word.")

    running = True # for Pygame
 
    while running:

#ADDING PYGAME    
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return
      
      if count > 0:        # While the user has chances
        letter = input("\nEnter a letter : ").lower()

        # Check if it is a good entry
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter one letter only, and only letters.")
            continue
        
        # Check if the letter is already find
        elif letter in word_guess:
            print("You already find this letter.")
            continue

        # Check if it is correct or not
        elif letter in letters:
            for i, charactere in enumerate(letters):
                if letter == charactere :
                    word_guess[i] = letter      # Replace '_' with the good letter
            print("Good answer !\n")
            print(" ".join(word_guess))

        else:       # Not correct word
            print("\nThis letter is not in the word.")
            count -= 1
            print(f"You have {count} moves left to guess the word.")
            print()
            print(" ".join(word_guess))
            history.append(letter)      # No correct letter add in history list
            print("History :", history)

#Adding PYGAME  
        display_word(word_guess,letters) # screen update    
        if count < 10: 
            if count < 10 and 0 <= (10 - count) < len(game_steps):
              screen.blit(game_steps[10 - count], [180,60])
        pygame.display.flip()

            # Check if the word is find == WIN
        if "_" not in word_guess:
             print("Congratulations ! You find the word", "".join(word_guess))
             score=len(word_guess)*count        # Calculate the score
             print(f"Your score is {score} pts")
             save_score(name,score)     # Write in the file score.txt
             break
        
    else:       # If every chances are used
        print("\nYou loose. The word was :", random_word)

#playing loose sound
        loose_sound.play()
    

        pygame.time.wait(2000)
        score = 0
        print(score)

# Function main to call functions and show Menu
def menu():

    running = True      # To keep the game open, or possibility to leave if 'False'

    while running:
        print("\n------ MENU ------")
        print("1. Play now")
        print("2. Enter a word")
        print("3. Scoreboard")
        print("4. Exit")
        print("------------------\n")
        menu_choice = input("Your choice : ")

        match menu_choice:
            case '1':
              random_word = load_word()  
              word_guess = ['_' for _ in random_word]  
              main()  
            case '2':
                insert_word()
            case '3':
                display_scores()
            case '4':
                print("\nLeaving Hanged game...")
                running = False     # Stop the loop

    print() 
    pygame.quit()
    exit()      # When running is False


# Program execute by ourself only
if __name__ == '__main__':
    menu()
  
