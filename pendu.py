# Import Libraries
import random as rd

# Add a word in the file
def insert_word():
    while True:
        try:
            new_word = str(input("\nEnter a new word (without spaces and in lowercase) : ")).strip().lower()
            if new_word.isalpha():      # Check if it is in 'a-z'
                with open("mots.txt", "a", encoding="utf-8") as file:
                    file.write(new_word + "\n")
                print("Word added successfully.")
                break
            else:
                print("Error, entry invalid please retry")
        except ValueError:
            print("Please enter only letters.")

# Function to read the file
def load_words():
# Try to open, read and verify if the file exist and if it is not empty
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

# Function to show the secret word
def display_word():
    random_word = load_word()
    letters = list(random_word)        # Separated each letters from the word
    
    print("modele test : ","".join(letters))      # TEST TEST TEST TEST TEST

    word_guess = ['_' for _ in letters]
    print("Guess : ", " ".join(word_guess))     # '_' of the word to guess
    return word_guess, letters

# Funtion main for every check and win condition
def main():
    print("\n--- START ---")
    load_words()        # Reading file...

    word_guess, letters = display_word()
    random_word = load_word()
    
    count = len(letters) + 2        # Number of chances
    print(f"You have {count} moves to guess the word.")

    while count > 0:        # While the user has chances
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
        
        # Check if the word is find == WIN
        if "_" not in word_guess:
             print("Congratulations ! You find the word", "".join(word_guess))
             break
        
    else:       # If every chances are used
        print("\nYou loose. The word was :", random_word)


# Function main to call functions and show Menu
def menu():

    running = True      # To keep the game open, or possibility to leave if 'False'

    while running:
        print("\n------ MENU ------")
        print("1. Play now")
        print("2. Enter a word")
        print("3. Exit")
        print("------------------\n")

        menu_choice = input("Your choice : ")

        match menu_choice:

            case '1':
                main()

            case '2':
                insert_word()
                main()

            case '3':
                print("\nLeaving Hanged game...")
                running = False     # Stop the loop

    print() 
    exit()      # When running is False


# Program execute by ourself only
if __name__ == '__main__':
    menu()