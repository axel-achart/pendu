# Importer la bibliothèque
import random as rd

# Funtion main
def main():
    print("\n--- Début du jeu ---")

    try:
        with open("mots.txt", "r", encoding="utf-8") as file:
            words = file.read().splitlines()
            if not words:
                print("Le fichier est vide. Ajoutez des mots avant de jouer.")
                return
    except FileNotFoundError:
        print("Le fichier 'mots.txt' est introuvable. Créer le avant de jouer.")
        return
    
    word = rd.choice(words).lower()
    letters = list(word)
    print("modele : ","".join(letters))      # TEST
    word_guess = ['_' for _ in letters]
    print("Mot à deviner : ", " ".join(word_guess))

    count = len(letters) + 2
    print(f"Vous avez {count} coups pour deviner le mot.")

    while count > 0:
        letter = input("\nVeuillez renseigner une lettre: ").lower()

        # Vérif si c'est une lettre
        if len(letter) != 1 or not letter.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue
        
        # Vérif si c'est déjà donnée
        if letter in word_guess:
            print("Vous avez déjà trouvé cette lettre.")
            continue

        # Vérif si la lettre est une bonne réponse
        if letter in letters:
            for i, char in enumerate(letters):
                if letter == char:
                    word_guess[i] = letter
            print("Bonne lettre !\n")
            print(" ".join(word_guess))
        else:
            print("\nCette lettre n'est pas dans le mot.")
            count -= 1
            print(f"Il vous reste {count} coups pour deviner le mot.")
        
    else:
        print("\nVous avez perdu. Le mot était :", word)


# Ajout d'un mot dans la liste
def insert_word():
    new_word = input("\nEntrez un nouveau mot (en minuscules, sans espace) : ").strip().lower()
    if new_word.isalpha():
        with open("mots.txt", "a", encoding="utf-8") as file:
            file.write(new_word + "\n")
        print("Mot ajouté avec succès.")
    else:
        print("Veuillez entrer un mot valide.")


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