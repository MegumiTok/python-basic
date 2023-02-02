import re

l = "Beautiful is better than ugly."
r1 = re.findall("Beautiful", l)

# 大文字小文字の違いを無視して検索したい場合は、
# re.IGNORECASEフラグを渡します。
r2 = re.findall("Beautiful", l, re.IGNORECASE)

print(r1)
print(r2)