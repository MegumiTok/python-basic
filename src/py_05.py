# break文に到達するとすぐにループを終了します。

qs =["What is your name?","Where are you living?","Do you like AUS?"]

n =0

while True:
    print("Type q to quit: ")
    a = input(qs[n])
    if a =="q":
        break
        
    n =(n+1)%3
    