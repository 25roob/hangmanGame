import random
import os

def game(wordGame):
    hiddenWord = ["_" for i in wordGame]
    
    while True:
        print(hiddenWord)
        leterInput = input('Elige una letra').upper()
        for item in wordGame:
            if leterInput == item[1]:
                hiddenWord[item[0]] = item[1]
        
        if hiddenWord == wordGame[][1]

        os.system("clear")


def selectWord():
    astate = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            astate.append(line)

    chosenWord = list(random.choice(astate).upper()[0:-1])

    nChosenWord = [leter for leter in enumerate(chosenWord)]
    return nChosenWord



def run():
    wordGame = selectWord()
    print(wordGame)
    print(wordGame[1][1])

    game(wordGame)

    # os.system("clear")


if __name__ == "__main__":
    run()
