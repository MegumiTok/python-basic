# Gameのオブジェクトを作ると、 Pythonは__init__メソッドを呼びます
# するとinput関数が実行されて、プレーヤーの名前を聞いてきます。

from random import shuffle # Random shuffle() Method

class Card:
    marks =["spades", "hearts","diamonds", "clubs"]
    
    values =[None, None, "2","3","4","5","6","7","8","9","10","Jack", "Queen", "King", "Ace"]
    
    def __init__(self, v, m):
        """markも値も整数値です"""
        self.value = v
        self.mark = m
        
    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.mark < c2.mark:
                return True
            else:
                return False
        return False
    
    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.mark > c2.mark:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v = self.values[self.value] + " of " + self.marks[self.mark]
        return v
    
class Deck:
    def __init__(self):
        self.cards =[]
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
        
    def rm_card(self):
        if len(self.cards) ==0:
            return
        return self.cards.pop()
        
    
class Player:
    def __init__(self, name):
        self.wins =0
        self.card = None
        self.name = name
        
class Game:
    def __init__(self):
        name1 = input("プレーヤー1の名前: ")
        name2 = input("プレーヤー2の名前: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        
    def wins(self, winner):
        print(f"このラウンドは {winner} が勝ちました。")
        
    def draw(self,p1n,p1c,p2n,p2c):
        
        print(f"{p1n} drew {p1c}, {p2n} drew {p2c}")
        
    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます！")
        while len(cards) >= 2:
            response = input("qで終了。それ以外のキーでPlay: ")
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1    
                self.wins(self.p2.name)
                
        print(f"ゲーム終了、{self.winner(self.p1, self.p2)} の勝利です！")
            
    def winner(self, p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！"
    
game= Game()
game.play_game()