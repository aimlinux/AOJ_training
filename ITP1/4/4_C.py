while True:
    # 1行読み込んで、空白で分割
    line = input().split()
    
    # リストの要素をそれぞれの型に変換して代入
    a = int(line[0])
    op = line[1]
    b = int(line[2])

    # 演算子が '?' なら終了
    if op == '?':
        break

    # 条件分岐
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        # // は小数点以下を切り捨てた商を求める
        print(a // b)