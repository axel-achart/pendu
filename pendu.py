import random 
#from spellchecker import SpellChecker
#fonction qui recupère les mots dans le fichier text
def load_words():
        try:
            with open("mots.txt", "r") as file:
             words = file.read().splitlines()  # Lire toutes les lignes et enlever les retours à la ligne
             return words
        except FileNotFoundError:
            print("Le fichier mots.txt n'a pas été trouvé")

#fonction pour ajouter un mot au fichier mots.txt
def insert_world():
    word_to_insert=input("Entrez le mot à ajouter").lower()#gestion erreur à+
    with open("mots.txt","a") as file:
        file.write(word_to_insert + "\n")
    print(f"Le mot '{word_to_insert}' a été ajouté au fichier.")

#fonction pour afficher le score
def display_scores():
    try:
        with open("score.txt", "r") as file:
            scores = file.read().splitlines()
            if scores:
                print("\nTableau des scores :")
                for score in scores:
                    print(score)
            else:
                print("\nAucun score enregistré.")
    except FileNotFoundError:
        print("Le fichier score.txt n'a pas été trouvé.")  

#fonction choisit un mot au hasard parmis les mots du fichier 
def load_word():
     words=load_words()
     random_word= random.choice(words)
     
     return random_word
#foction pour afficher le mot à deviner sous forme de list avec des _ à la place de chaque lettre
def display_word():
      random_word = load_word()
      letters = list(random_word)
      word_guess = ["_" for _ in letters]
      print(word_guess)
      return word_guess, letters

#fonction principale du jeu
def play(count):
       print("\n--- Début du jeu ---")
       
       word_guess, letters =display_word()
       print(count)
       while count > 0:
        

        letter = input("Devinez une lettre : ").lower()

        if letter in letters and "_" in word_guess :
            for i in range(len(word_guess)):
                if letters[i] == letter:
                    word_guess[i] = letter
            print(f"Bonne réponse! La lettre '{letter}' est dans le mot.")
            print(word_guess)
            print(f"il vous reste,{count} vies")
        else:
            count -= 1
            print(f"Incorrect! Il vous reste {count} tentatives.")
        if "_" not in word_guess:
             print(f"Félicitations Vous avez trouvé le mot '{word_guess}'!")
             
             break 

def main():
    while True:
        print("\nMenu :")
        print("1. Jouer")
        print("2. Ajouter un mot")
        print("3. Afficher les scores")
        print("4. Quitter")

        choice = input("Votre choix : ")

        if choice == "1":
             # Choisir le niveau de difficulté
            print("\nChoisissez un niveau de difficulté :")
            print("1. Facile")
            print("2. Difficile")
            difficulty_choice = input("Entrz votre choix (1 ou 2) : ")
            if difficulty_choice == "1":
               play(10)
               replay = input("\nSouhaitez-vous rejouer ? (o/n) : ").lower()
               if replay == "o":
                continue
               else:
                break
            elif difficulty_choice=="2":
                play(6)  
                replay = input("\nSouhaitez-vous rejouer ? (o/n) : ").lower()
                if replay == "o":
                    continue
                else:
                    break
            
                     
            
        elif choice == "2":
            insert_world()
        elif choice == "3":
            display_scores()
        elif choice == "4":
            print("Merci d'avoir joué ! À bientôt.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
    
 
main()
