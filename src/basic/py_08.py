class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color =c
        print("Created!")
        
orange1 = Orange(10, "pink")
orange1.weight = 100 #インスタンス変数の値を変更
# print(orange1)


print(orange1.weight) #100
print(orange1.color)  #pink

# 出力
# Created!
# <__main__.Orange object at 0x1048348d0>
# 100
# pink

# Oranqeオブジェクト自体を画面に出力すると、 PythonはそれがOrangeクラスのオブジェクトであることと、コンピューターのメモリー上の位置を表示します(メモリーの位置は実行するごと に異なります)。