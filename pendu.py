import random 
def load_words():
        with open("mots.txt", "r") as file:
            words = file.read().splitlines()  # Lire toutes les lignes et enlever les retours à la ligne
        return words
     
def load_word():
     words=load_words()
     random_word= random.choice(words)
     
     return random_word
def display_word():
      random_word = load_word()
      letters=list(random_word)
      word_guess=["_" for _ in letters]
      print(word_guess)
      return word_guess, letters


def main():
       print("\n--- Début du jeu ---")
       word_guess, letters =display_word()
       count=len(word_guess)
       print(count)
       while count > 0:
        

        letter = input("Devinez une lettre : ").lower()

        if letter in letters and "_" in word_guess :
            for i in range(len(word_guess)):
                if letters[i] == letter:
                    word_guess[i] = letter
            print(f"Bonne réponse! La lettre '{letter}' est dans le mot.")
            print(word_guess)
            print(f"il vous reste,{count} tentative")
        else:
            count -= 1
            print(f"Incorrect! Il vous reste {count} tentatives.")
        if "_" not in word_guess:
             print(f"Félicitations Vous avez trouvé le mot '{word_guess}'!")
             


 
main()
