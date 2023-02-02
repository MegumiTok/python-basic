import re

text ="""キリンは大昔から __複数名詞__ の興味の対象でした。キリンは
__複数名詞__ の中で一番背が高いですが、科学者たちはそのような長い __体の一部__ をどうやって獲得したのか説明できません。
キリンの身長は__数値__ __単位__ 近くあり、その高さのほとんどは足と__体の一部__ によるものです
"""

def mad_libs(mls):

    blanks = re.findall("__.*?__", mls)
    if blanks is not None:
        for word in blanks:
            new = input(f"{word} を入力: ")
            mls = mls.replace(word, new, 1)
        print("\n")
        # print(mls.replace("\n",""))
    else:
        print("引数mlsが無効です")
        
mad_libs(text)