
random_word = "SOS"
letters = list(random_word)

word_guess = ['_' for _ in letters]

count =len(letters)

while True:
    print(word_guess)
    letter = input("Veuillez entrer votre lettre : ")
    for i, charactere in enumerate(letters):
        if letter == charactere:
            word_guess[i] = letter  
            count = count -1
            if count ==0:
                print("Vous avez gagné")
                break

    



         


        
                                    
