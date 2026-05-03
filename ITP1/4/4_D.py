# 1. 最初の行（整数の数 n）を読み込む
# ※Pythonではリストの組み込み関数を使う場合、nを使わなくても解けますが、
# 入力の順番を守るために必ず読み込む必要があります。
n = int(input())

# 2. 2行目の n個の整数をリストとして一括で読み込む
# split() で空白区切りの文字列を分割し、map で整数に変換、最後に list にまとめます。
a = list(map(int, input().split()))

# 3. 組み込み関数を使って最小値、最大値、合計値を計算
min_val = min(a)
max_val = max(a)
sum_val = sum(a)

# 4. 空白区切りで出力
print(min_val, max_val, sum_val)