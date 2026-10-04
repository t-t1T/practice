import sys
import bisect

def main():
    # 入力をすべて受け取って空白で分ける
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k_modes = int(input_data[1])
    # sigma は誤差の最小化（事後確率の最大化）の比較には使わないので読み飛ばす
    
    a = [float(x) for x in input_data[3:3+n]]
    mu = [float(x) for x in input_data[3+n:]]
    
    mu_1 = mu[0]
    mu_rest = mu[1:]
    
    # 累積和の準備（ループのたびに計算すると遅いので事前にまとめて計算する）
    # s1: 最初から i 個目までモード1だった場合の誤差の合計
    s1 = [0.0] * (n + 1)
    for i in range(n):
        s1[i+1] = s1[i] + (a[i] - mu_1) ** 2
        
    # sum_a: 後ろから i 個目までの重さの合計
    # sum_a2: 後ろから i 個目までの重さの2乗の合計
    sum_a = [0.0] * (n + 1)
    sum_a2 = [0.0] * (n + 1)
    for i in range(n - 1, -1, -1):
        sum_a[i] = sum_a[i+1] + a[i]
        sum_a2[i] = sum_a2[i+1] + a[i] ** 2
        
    min_error = float('inf')
    best_t = -1
    best_x = -1
    
    # tは2個目からN個目まで
    for t in range(2, n + 1):
        idx = t - 1
        count = n - t + 1
        
        # t個目以降の実際の重さの平均値
        target_mean = sum_a[idx] / count
        
        # 実際の平均値に一番近いモードを、二分探索で素早く探す
        pos = bisect.bisect_left(mu_rest, target_mean)
        
        candidates = []
        if pos < len(mu_rest):
            candidates.append(pos)
        if pos - 1 >= 0:
            candidates.append(pos - 1)
            
        for cand_pos in candidates:
            cand_mu = mu_rest[cand_pos]
            
            # そのモードだった場合の誤差を計算（事前に計算した累積和を使うから一瞬で終わる）
            err = s1[idx] + sum_a2[idx] - 2 * cand_mu * sum_a[idx] + count * (cand_mu ** 2)
            
            if err < min_error:
                min_error = err
                best_t = t
                best_x = cand_pos + 2 # mu_1を除いた配列でのインデックスなので+2する
                
    print(f"{best_t} {best_x}")

if __name__ == '__main__':
    main()