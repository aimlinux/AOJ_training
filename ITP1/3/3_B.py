# ケース番号を管理する変数
case_num = 1

while True:
    # 1行読み込んで整数に変換
    x = int(input())
    
    # xが0なら、ループを終了してプログラムを止める
    if x == 0:
        break
    
    # 指定されたフォーマットで出力
    # f-string（f"..."）を使うと直感的に書けます
    print(f"Case {case_num}: {x}")
    
    # ケース番号を次に進める
    case_num += 1