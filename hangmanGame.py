import random
import os

def game(wordGame):
    # Creates an string of '_' with the same number of components as the hidden word.
    hiddenWord = ["_" for i in wordGame]
    accents = [(0, 'Á'), (1, 'É'), (2, 'Í'), (3, 'Ó'), (4, 'Ú')]
    noAccents = ['A', 'E', 'I', 'O', 'U']
    noAccentsWordGame = [list(tup) for tup in wordGame] #changes a list of tupples to a list of lists

    # Code to temporary eliminate accents
    for element in wordGame:
        for char in accents:
            if char[1] == element[1]:
                noAccentsWordGame[element[0]][1] = noAccents[char[0]]
    
    # Main bucle of the game while the correct word is not fully guessed
    while hiddenWord != [i[1] for i in noAccentsWordGame]:

        # print hiddenWord in a fashionable way "_ _ _ _"
        for leter in hiddenWord:
            print(leter + ' ', end='')

                # The user should write a single leter per turn.
        leterInput = input('\nElige una letra: ').upper()

        # Cicle that compares every input with all the elements in the chosen word
        for item in noAccentsWordGame:
            if leterInput == item[1]:
                hiddenWord[item[0]] = item[1]
                
        os.system("clear")

        if hiddenWord == [i[1] for i in noAccentsWordGame]:
            for leter in [i[1] for i in wordGame]:
                print(leter, end='')
            print('\n¡Felicidadez! \n¡Has Ganado!')


def selectWord(): #funtion that selects a random word from a database
    astate = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            astate.append(line)

    #Selects a random word changes it to uppercase format and cuts the '\n' at the end.
    chosenWord = list(random.choice(astate).upper()[0:-1]) 

    #Enumerates every leter in the chosen word. 
    nChosenWord = [leter for leter in enumerate(chosenWord)]
    return nChosenWord


def run(): #Global function
    os.system("clear")
    wordGame = selectWord() #Call to select a word from a database
    print(wordGame)
    print([i[1] for i in wordGame])

    game(wordGame)

    
if __name__ == "__main__":
    run()