
random_word = 
letters = list(random_word)
print (letters)

word_gess = ['_' for _ in letters]
print(word_gess)

letter = input("veuillez renseigner votre première lettre: ")

for i,  charactere in enumerate(letters):
                if letter == charactere:
                        word_gess[i] = letter
                        
                print(f"Index: {i}, Caractère: {charactère}")
            
print(game_list)