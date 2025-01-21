# Importer la bibliothèque
import random as rd

# Funtion main
def main():
    print("\n--- Début du jeu ---")

    # Essaie de lire le fichier, et retourne des erreurs si fichier vide ou inexistant
    try:
        with open("mots.txt", "r", encoding="utf-8") as file:
            words = file.read().splitlines()
            if not words:
                print("Le fichier est vide. Ajoutez des mots avant de jouer.")
                return
    except FileNotFoundError:
        print("Le fichier 'mots.txt' est introuvable. Créer le avant de jouer.")
        return
    
    # Récupère aléatoirement un mot du fichier
    word = rd.choice(words).lower()
    letters = list(word)        # Sépare chaques lettres du mot

    print("modele : ","".join(letters))      # TEST TEST TEST TEST TEST

    word_guess = ['_' for _ in letters]
    print("Mot à deviner : ", " ".join(word_guess))     # Affiche les '_' à deviner

    count = len(letters) + 3        # Nombre de chances
    print(f"Vous avez {count} coups pour deviner le mot.")

    while count > 0:        # Tant que le joueur n'a pas utilisé tous ses coups
        letter = input("\nVeuillez renseigner une lettre: ").lower()

        # Vérif si c'est bien une lettre
        if len(letter) != 1 or not letter.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue
        
        # Vérif si c'est déjà donnée
        elif letter in word_guess:
            print("Vous avez déjà trouvé cette lettre.")
            continue

        # Vérif si la lettre est une bonne réponse
        elif letter in letters:
            for i, charactere in enumerate(letters):
                if letter == charactere :
                    word_guess[i] = letter      # Va remplacer le '_' par la lettre
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
    if new_word.isalpha():      # Vérifie si c'est bien entre a-z
        with open("mots.txt", "a", encoding="utf-8") as file:
            file.write(new_word + "\n")
        print("Mot ajouté avec succès.")
    else:
        print("Veuillez entrer un mot valide.")


# Fonction principale
def menu():

    running = True      # Initialisation pour que la boucle marche jusqu'à changement par Exit

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