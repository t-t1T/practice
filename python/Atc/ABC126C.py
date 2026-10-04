

import math

# 入力を受け取る
N, K = map(int, input().split())

# 最終的な確率を貯める変数
ans = 0

# サイコロの目 i を 1 から N まで順番に試す
for i in range(1, N + 1):
    current_score = i
    coin_count = 0
    
    # スコアが K 未満の間は、コインを振り続ける（2倍にする）
    while current_score < K:
        current_score *= 2
        coin_count += 1
    
    # この目が出る確率は (1/N)
    # その後、連続で表が出る確率は (1/2) の coin_count 乗
    prob = (1 / N) * ((1 / 2) ** coin_count)
    
    # 全体の確率に足す
    ans += prob

# 結果を小数で出力
print(ans)