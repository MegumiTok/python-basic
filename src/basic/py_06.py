# continue文は、実行中の反復処理を途中で終了して、次の反復処理を開始 します。

for i in range(1,6):
    if i ==3:
        continue
    print(i)
    
# 別の書き方
# i = 1
# while i<=5:
#     if i ==3:
#         i +=1
#         continue
#     print(i)
#     i +=1