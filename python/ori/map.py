import numpy as np
import matplotlib.pyplot as plt

# マップサイズ
width = 120
height = 80

# ランダム生成（病気発生リスク）
np.random.seed(42)
risk_map = np.random.rand(height, width)

# 中央付近を高リスク化
for y in range(height):
    for x in range(width):
        distance = ((x - 70) ** 2 + (y - 40) ** 2) ** 0.5
        risk_map[y, x] += np.exp(-distance / 20)

# 正規化
risk_map = risk_map / risk_map.max()

# 描画
plt.figure(figsize=(8, 5))

heatmap = plt.imshow(
    risk_map,
    cmap="RdYlGn_r",   # 緑→黄→赤
    interpolation="bilinear"
)

# カラーバー
cbar = plt.colorbar(heatmap)
cbar.set_label("発生リスク")

# タイトル
plt.title("病害発生リスクマップ", fontsize=18)

# 軸ラベル
plt.xlabel("圃場 X")
plt.ylabel("圃場 Y")

# グリッド
plt.grid(color='white', linestyle='--', linewidth=0.3)

plt.tight_layout()
plt.show()