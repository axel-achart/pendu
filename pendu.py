# Importing Libraries
import pygame as pg


# Function to play with words in 'mots.txt'
def play_now():
    with open('mots.txt', 'r') as file:
        search = file.read()
        print(search)


# Function to enter a word to play with it
def enter_word_play():
    print("No define yet")


# Function Main
def main():

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
                play_now()

            case '2':
                enter_word_play()

            case '3':
                print("\nLeaving Hanged game...")
                running = False

    print() 
    exit()      # When running is False


# For PyGame
def menu():
    pg.init()       # Initialisation of PyGame
    main()


# Program execute condition
if __name__ == '__main__':
    print("\nLaunching Hanged game...")
    menu()