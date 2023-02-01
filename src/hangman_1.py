# The Hangman program randomly selects a secret word for the player to guess from a list of words.
# 慣れないうちは必要な情報を紙に書き出したら必要なデータが整理できて比較的簡単になる。

import random
words = "apple banana mango australia grape".split()

def getRandomWord(wordList):
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex]

def hangman():
    secretWord = getRandomWord(words)
    wrong =0
    stages =[
        "",
        "---------           ",
        "|                   ",
        "|        |          ",
        "|        0          ",
        "|       /|\         ",
        "|       / \  ヤバい！ ",
        "| ==== DEAD ======"     
    ]
    rletters = list(secretWord)
    board = ["_"]*len(secretWord)
    win = False
    print("""
          ハングマンへようこそ！
          これは英単語を当てるゲームです。
          首吊りを阻止してください！
          """)
    while wrong < len(stages) -1:
        print("\n")
        msg="Please enter a LETTER: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("成功です!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {} でした。".format(secretWord))
        
hangman()