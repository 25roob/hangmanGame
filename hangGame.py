import random
import os

def game(wordGame):
    #Creates an string of '_' with tha same number of components as the hidden word.
    hiddenWord = ["_" for i in wordGame]
    
    while hiddenWord != [i[1] for i in wordGame]:
        print(hiddenWord)
        leterInput = input('Choose a leter').upper()
        for item in wordGame:
            if leterInput == item[1]:
                hiddenWord[item[0]] = item[1]
        
        
        os.system("clear")

        if hiddenWord == [i[1] for i in wordGame]:
            print('Congratulations! \n You Won!')



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
    wordGame = selectWord() #Call to select a word from a database
    print(wordGame)
    print([i[1] for i in wordGame])

    game(wordGame)

    # os.system("clear")


if __name__ == "__main__":
    run()
