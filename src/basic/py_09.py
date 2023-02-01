# 次のコードは、Orangeオブジェクトに腐る性質を追加した例です。

class Orange:
    def __init__(self, w, c):
        """weightはグラム"""
        self.weight = w
        self.color =c
        self.mold =0
        print("Created!")
        
    def rot(self, days, temp):
        """tempは摂氏"""
        self.mold = days * temp
        
orange1 = Orange(200, "blue")
print(orange1.mold)
orange1.rot(10, 37)
print(orange1.mold)