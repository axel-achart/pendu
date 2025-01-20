

words_list = []
word_chain = []

# Menu pendu
def hanged_menu():
    
    while True :

        print("=================")
        print("    Hangman      ")
        print("=================")
        print("1️.  Play")
        print("2️.  Insert a word")
        print("=================")
        
        menu_choice  = input( "Votre choix : ")
        
        match menu_choice:
                    case "1":
                    
                        print(game_list)
                        entry = input("veuillez renseigner une lettre: ").upper
                        
                        print(count)
                        if entry in word_chain:
                                letter_index=word_chain.index(entry)
                                game_list[letter_index] = entry
                                print(game_list)
                                count = count -1
                                if count ==0:
                                     print("Vous avez gagné")
                                     break
                                else:
                                    continue
                    case "2" : 
                        word = input("Veuillez renseigner le mot à insérer: ").strip().upper()
                        word_chain = list(word)
                        count = len(word_chain)
                        print(word_chain)
                        game_list = ['_' for _ in word_chain]
                        continue
hanged_menu()