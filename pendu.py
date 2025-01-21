# Importer la bibliothèque
import random as rd


def main():
    print("\n--- Début du jeu ---")
    with open("mots.txt", "r") as file:
        words = file.read().splitlines()
    word = rd.choice(words)
    letters = list(word)
    print("modele : ", letters)      # TEST
    word_guess = ['_' for _ in letters]
    print(word_guess)

    count = len(letters)
    print("Coups : ", count)

    while True:
        letter = input("Veuillez renseigner une lettre: ")
        for i, charactere in enumerate(letters):
            if letter == charactere:
                word_guess[i] = letter
                count -= 1
                print("Coups restants : ", count)
        if letter != charactere:                        # A REVOIR CAR CETTE CONDITION SE LANCE A CHAQUE FOIS
            print("\nLettre non correct")

        print("\n", word_guess)
        print()
        



# Ajout d'un mot dans la liste
def insert_word():
    new_word = str(input("\nEnter a new word : "))
    file = open("mots.txt", "w")
    file.write(new_word)
    file.close()
    print("\nFile update")
    print()


# Fonction principale
def menu():

    running = True

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
                running = False

    print() 
    exit()      # When running is False



if __name__ == '__main__':
    menu()