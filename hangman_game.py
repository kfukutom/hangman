import sys
import random

wordList = ["dream", "fathom", "painful", "react", "object", 
            "happy", "statistics", "daily", "eulogize", "venerable"]

#hangman board
row1 = ["  ", "  ", "  ", "  ", "  "]
row2 = ["  ", "  ", "  ", "  ", "  "]
row3 = ["  ", "  ", "  ", "  ", "  "]
row4 = ["  ", "  ", "  ", "  ", "  "]
row5 = ["  ", "  ", "  ", "  ", "  "]
row6 = ["  ", "  ", "  ", "  ", "  "]
row7 = ["  ", "  ", "  ", "  ", "  "]
row8 = ["  ", "  ", "  ", "  ", "  "]
row9 = ["  ", "  ", "  ", "  ", "  "]
row10 = ["  ", "  ", "  ", "  ", "  "]
row11 = ["  ", "  ", "  ", "  ", "  "]
row12 = ["  ", "  ", "  ", "  ", "  "]
row13 = ["  ", "  ", "  ", "  ", "  "]


def intialize():
    global row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13
    listRow = [row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12]
    for i in range(len(row1)):
        if(i == 1):
            row1[0] = "=="
        if(i == 4):
            row1[i] = "++"
        elif(i == 1 or i == 2 or i == 3):
            row1[i] = "--"
    for j in range(11):
        current = listRow[j]
        for i in range(len(current)):
            if(i == 4):
                current[i] = " |"
    for i in range(len(row13)):
        if(i == 4):
            row13[i] = "=="
            row13[3] = " ="


def showcase():
    global row1, row2, row3, row4, row5, row6, row7, row8, row9, row10
    print("\n", row1, "\n", row2, "\n", row3, "\n", row4, "\n", row5, "\n", row6, "\n", row7, "\n", row8, "\n", row9, "\n", row10, "\n", row11, "\n", row12, "\n", row13)


def end():
    response = input("Would you like to leave this environment? >> ")
    while True:
        if(response.lower() == "yes" or response.lower() == "y"):
            print("Goodbye. . .")
            sys.exit()
            # EXIT TRUE
        else:
            return False

def getWord():
    global wordList
    return(str(random.choice(wordList)))


def drawBoard(i):
    global row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13
    if(i == 1):
        row2[2] = ("O ")



def beginGame():
    global wordList
    global row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13
    global getWord
    index = 0
    incorrect = 0
    wordChoice = getWord()
    guess = []
    usedGuesses = []
    print(wordChoice)
    for i in range(len(wordChoice)):
        guess.append("_ ")
    while(True):
        charGuess = input("Enter a guess for a letter: \n")
        if(wordChoice.__contains__(charGuess) == True):
            usedGuesses.append(wordChoice)
            index = index + 0
            for j in range(len(wordChoice)):
                if(wordChoice[j] == charGuess):
                    index = index + 1
                    guess[j] = charGuess
                    print(guess)
                    print(index)
                if(index == (len(wordChoice))):
                    print("CORRECT!")
                    sys.exit()
        elif(wordChoice.__contains__(charGuess) == False):
            incorrect = incorrect + 1
            print("Not true, try again")
            drawBoard(incorrect)
            showcase()


intialize()
showcase()
beginGame()
