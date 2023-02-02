# https://www.tutorialspoint.com/python/python_reg_expressions.htm

import re

zen ="""Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


string = "Two too. 478 h"
# Pythonの正規表現では、複数行のテキストを複数行として扱うために
# re.MULTILINEフラグが必要

m = re.findall("^If", zen, re.MULTILINE)
print(m)

# 複数文字との一致
# [abc]のように角カッコの中に、一致させたい文字を並べる
# [abc]というパターンは、a、b、cのどれかl文字に一致します。

m2 = re.findall("t[ow]o", string, re.IGNORECASE)
print(m2)

# 数値との一致
m3 = re.findall("\d", string, re.IGNORECASE)
print(m3) # ['4', '7', '8']

# 繰り返し
# アスタリスクを使うと「直前のパターンが0回以上一致」します。
# このアスタリスクは實欲なので、できるだけ長い文字列に一致 します。
# 負欲な一致は、常にしてほしいわけではありません。
# Pythonでは非貧欲な正規表現が使えます(はてなをつける)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)

for match in found:
    print(match)
    
# これと比較。
found2 = re.findall("__.*__", t)
for match in found2:
    print(match)
    
    
