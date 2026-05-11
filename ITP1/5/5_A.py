while True:
    H, W = map(int, input().split())
    
    # 終了条件
    if H == 0 and W == 0:
        break
    
    for i in range(H):
        if i == 0 or i == H - 1:
            # 最初と最後の行はすべて #
            print("#" * W)
        else:
            # 中間の行は # + . が (W-2)個 + #
            print("#" + "." * (W - 2) + "#")
    
    # 各データセットの後に空行を入れる
    print()