# String Formatting

#=============
# what = input("what: ")
# when = input("when: ")
# where = input("where: ")
# do = input("What you did: ")

# str = "{} {} {} {}.".format(what, do, where, when)
# print(str)

#=============

# Python3.6からf文字列（f-strings、フォーマット文字列、フォーマット済み文字列リテラル）という仕組みが導入され、
# 冗長だった文字列メソッドformat()をより簡単に書けるようになった。
a = 123
b = 'abc'

print(f"{a} and {b}")

# f文字列でも置換フィールド{}でコロン:のあとに書式指定文字列を指定することで様々な書式を指定できる。
s = "apple"
print(f'right : {s:*>8}') # right : ***apple
print(f'center: {s:@^8}') # center: @apple@@
print(f'left  : {s:*<8}') # left  : apple***

# ゼロ埋め
i = 1234

print(f'zero padding: {i:08}') # zero padding: 00001234

# 桁区切り
n = 1234567890

print(f'comma: {n:,}') # comma: 1,234,567,890

# 日時（datetime）
import datetime

dt = datetime.datetime(2020, 1, 5, 20, 15, 30)

print(f'datetime: {dt}') # datetime: 2020-01-05 20:15:30
print(f'datetime: {dt:%A, %m/%d/%Y %I:%M:%S %p}') # datetime: Sunday, 01/05/2020 08:15:30 PM
print(f'datetime: {dt.isoformat()}') # datetime: 2020-01-05T20:15:30

# 参考
# 右寄せ、中央寄せ、左寄せ: rjust(), center(), ljust()
t = '1234'
print(t.rjust(8, '0'))
# 00001234

print(t.center(8, '0'))
# 00123400

print(t.ljust(8, '0'))
# 12340000