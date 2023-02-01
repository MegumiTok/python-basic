# コンポジション
# 別クラスのオブジェクトを変数として持たせます。
# たとえば、犬とその飼い主という関係を表すのにコンポジションを使い、犬は1人の飼い主を持つ、 と表現します。 

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
class Person:
    def __init__(self, name):
        self.name = name
        
mick = Person("Meg Tokui")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)