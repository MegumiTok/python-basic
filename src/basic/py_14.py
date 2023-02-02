# __str__メソッド

class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


mike = Person('Mike', 20)
print(mike) # <__main__.Person object at 0x1054d8810>

# これでオブジェクトが持っている値を出力することができますが、
# 値を確認するために毎回上記のようなprint関数を記述するのはとてもめんどくさい。
print(f'name: {mike.name}, age: {mike.age}') # name: Mike, age: 20


# そこで！
# 下記のように__str__メソッドを定義しておくと楽です。
class PersonTwo:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # ここ
    def __str__(self) -> str:
        return f'name: {self.name}, age: {self.age}'


alisa = PersonTwo('Alisa', 18)
print(alisa)

# ちなみに、
# __str__が定義されていない場合に文字列が要求されたら__repr__の値が返されます。
class PersonThree:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # ここ
    def __repr__(self) -> str:
        return f"nam:{self.name}, age:{self.age}"


sean = PersonThree('Sean', 32)
print(sean)
