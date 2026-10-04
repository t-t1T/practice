S = input()

# 前半2桁と後半2桁を数値として取得
first = int(S[:2])
last = int(S[2:])

# それぞれが「月(01-12)」として有効か判定
is_first_month = 1 <= first <= 12
is_last_month = 1 <= last <= 12

# 判定結果に基づいて出力
if is_first_month and is_last_month:
    print("AMBIGUOUS")
elif is_first_month:
    print("MMYY")
elif is_last_month:
    print("YYMM")
else:
    print("NA")