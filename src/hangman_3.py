# # Australiaのように同じ文字が二回以上ある場合に対応。
# import random
# words = "apple banana mango australia grape".split()


# def getRandomWord(wordList):
#     wordIndex = random.randint(0,len(wordList)-1)
#     return wordList[wordIndex].upper()

# HANGMAN_PICS = [
#         "",
#         "---------           ",
#         "|                   ",
#         "|        |          ",
#         "|        0          ",
#         "|       /|\         ",
#         "|       / \  ヤバい！ ",
#         "| ==== DEAD ======"     
#     ]

# LOGO = ''' 
#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/    '''

# def hangman():
#     secretWord = getRandomWord(words)
#     wrong =0
  
#     rletters = list(secretWord)
#     board = ["_"]*len(secretWord)
#     win = False
#     print(LOGO)
#     print("""
# Let's play Hangman!
# これは英単語を当てるゲームです。
# 首吊りを阻止してください！
# quitとタイプすれば終了できます。
#           """)
#     while wrong < len(HANGMAN_PICS) -1:
#         print("\n")
#         msg="Please enter a LETTER: "
#         char = input(msg).upper()
#         if char == "QUIT":
#             break
#         # checks if our guess is only 1 char long
#         if len(char) != 1:
#             print("\nOops! Please enter a single letter(ﾟДﾟ; ≡ ;ﾟДﾟ)")
#             continue
#         elif char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#             print('\nOops! Please enter a LETTER(ﾟДﾟ; ≡ ;ﾟДﾟ)')
#             continue
#         elif char in board:
#             print('\nYou have already guessed that letter. Choose again.')
#             continue
        
#         if char in rletters:
#             cind = rletters.index(char)
#             board[cind] = char
#             rletters[cind] = "$"
#         else:
#             wrong += 1
#         print(" ".join(board))
#         e = wrong + 1
#         print("\n".join(HANGMAN_PICS[0:e]))
#         if "_" not in board:
#             print("成功です!")
#             print(" ".join(board))
#             win = True
#             # break
#             q = input("\nDo you want to play again? (yes or no): " )
#             if q == "yes":
#                 print("\nいぇい！ゲーム再開！")
#                 hangman()
#             elif q == "no":
#                 break
#             else:
#                 q = input("\n Please type yes or no: " )
#     if not win:
#         print("\n".join(HANGMAN_PICS[0:wrong+1]))
#         print("残念！正解は {} でした。".format(secretWord))
#         q = input("\nDo you want to play again? (yes or no): " )
#         if q == "yes":
#             print("\nいぇい！ゲーム再開！")
#             hangman()
#         elif q == "no":
#             pass
#         else:
#             print("yesかnoで答えてください")
            
        
# hangman()