# 継承

class Shape:
    def __init__(self, w, l):
        self.width =w
        self.len =l
        
    def print_size(self):
        print("{} by {}".format(self.width, self.len))
        
# my_shape = Shape(20,25)
# my_shape.print_size()

class Square(Shape):
    pass

a_square = Square(20,20)
a_square.print_size()

# Squareクラスの定義でパラメータにShapeクラスを指定したので、 SquareクラスはShapeクラスの変数とメソッドを継承しました。
# 子クラスには、ほかのクラス定義のようにメソッドや変数を定義できます。 これらは親クラスには影響しません。