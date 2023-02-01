# 以下の文を追加してよりゲーム体験を向上させたい
# You have already guessed that letter. Choose again.
# Please enter a single letter.
# Please enter a LETTER.
# Do you want to play again? (yes or no)

import random
words = "apple banana mango australia grape".split()

def getRandomWord(wordList):
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex].upper()

HANGMAN_PICS = [
        "",
        "---------           ",
        "|                   ",
        "|        |          ",
        "|        0          ",
        "|       /|\         ",
        "|       / \  ヤバい！ ",
        "| ==== DEAD ======"     
    ]

def hangman():
    secretWord = getRandomWord(words)
    wrong =0
  
    rletters = list(secretWord)
    board = ["_"]*len(secretWord)
    win = False
    print("""
          Let's play Hangman!
          これは英単語を当てるゲームです。
          首吊りを阻止してください！
          quitとタイプすれば終了できます。
          """)
    while wrong < len(HANGMAN_PICS) -1:
        print("\n")
        msg="Please enter a LETTER: "
        char = input(msg).upper()
        if char == "QUIT":
            break
        # checks if our guess is only 1 char long
        if len(char) != 1:
            print("\n In this game, please enter a Character.")
            continue
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(HANGMAN_PICS[0:e]))
        if "_" not in board:
            print("成功です!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(HANGMAN_PICS[0:wrong+1]))
        print("残念！正解は {} でした。".format(secretWord))
        
hangman()