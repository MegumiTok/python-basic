# クラス変数　vs インスタンス変数
# このコード例では、 クラスRectangleにクラス変数recsを追加しました。
# クラス変数の定義は、 init メソッドの外で行います。 
# __init__が呼ばれるのは、 クラスのインスタンスを作成したときだけで す。
# クラスオブジェクトを通してクラス変数にアクセスできますが、そのときには __init__メソッドは呼ばれません。 

# クラス定義のあとに、Rectangleクラスのオブジェクト (=インスタンス)を3つ作っています。
# それぞれのRectangleのインスタンスが作られ るたびに __init__ メソッドが呼ばれ、幅と長さを含むダブルをrecsリ ストに追加しています。
# つまり、ReCtangleのインスタンスが作られるた びにrecsリストに幅と長さのダブルが追加されます。
# クラス変数を使うと、 グローバル変数を使わずに、クラスのインスタンス間でデータを共有できます

class Rectangle:
    recs =[]
    
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))
        
r1 = Rectangle(10, 24)
r2 = Rectangle(20, 2)
r3 = Rectangle(30, 204)

print(Rectangle.recs)