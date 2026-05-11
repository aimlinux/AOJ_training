import sys

# 標準入力からすべての行を一度に読み込む方法がAOJでは確実です
for line in sys.stdin:
    # スペース区切りで H と W を取得
    h, w = map(int, line.split())
    
    # H と W がともに 0 のときは終了
    if h == 0 and w == 0:
        break
    
    # 描画処理
    for i in range(h):
        row = []
        for j in range(w):
            # 行番号 i と 列番号 j の和が偶数なら '#'
            if (i + j) % 2 == 0:
                row.append("#")
            else:
                row.append(".")
        # 最後にスペースが入らないよう、joinで結合して出力
        print("".join(row))
    
    # データセットの後に必ず「1つだけ」空行を入れる
    print()