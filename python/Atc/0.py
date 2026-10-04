# 【1つの整数】例: 5
N = int(input())

# 【複数の整数（空白区切り）】例: 3 5
A, B = map(int, input().split())

# 【リストとして受け取る（空白区切り）】例: 1 2 3 4 5
L = list(map(int, input().split()))

# 【1つの文字列】例: teamlab
S = input()

# 【複数の文字列（空白区切り）】例: hello world
S1, S2 = input().split()

S = "teamlab"

# 文字列の反転（後ろから読む） -> "balmaet"
rev_S = S[::-1]

# 特定の文字の出現回数を数える -> 'a'は2回
count_a = S.count('a')

# 文字の置換（'a'を'A'に変える） -> "teAmlAb"
rep_S = S.replace('a', 'A')

# 大文字・小文字の変換
upper_S = S.upper() # "TEAMLAB"
lower_S = S.lower()

# 文字列の長さを取得
length = len(S)

# N文字目を取得（※プログラミングは0番目から始まることに注意！）
first_char = S[0] # 't'

A = [3, 1, 4, 1, 5]

# 昇順に並び替え（小さい順） -> [1, 1, 3, 4, 5]
A.sort()

# 降順に並び替え（大きい順） -> [5, 4, 3, 1, 1]
A.sort(reverse=True)

# リストの合計、最大値、最小値
total = sum(A) # 14
max_val = max(A) # 5
min_val = min(A) # 1

# 重複を削除する -> [1, 3, 4, 5] (順序はバラバラになるので注意)
unique_A = list(set(A))

# リストの中に特定の数字があるか判定
if 4 in A:
    print("Yes")

import math

# 割り算の切り上げ（例: 10/3=3.33... を 4 にする）
ans = math.ceil(10 / 3)

# 割り算の切り捨て（例: 10/3=3.33... を 3 にする。 `10 // 3` と同じ）
ans = math.floor(10 / 3)

# 2つの数の最大公約数（GCD）
gcd_val = math.gcd(12, 18) # 6

# 偶数・奇数の判定
if N % 2 == 0:
    print("偶数")
else:
    print("奇数")

# 絶対値（マイナスをプラスにする）
abs_val = abs(-5) # 5

# 答えが複数ある場合、リストの中身を「空白区切り」で出力する
ans_list = [1, 2, 3]
print(*ans_list)  # 出力: 1 2 3