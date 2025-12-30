import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pybaseball import statcast_batter

# 1. データの取得
player_id = 660271 
df = statcast_batter('2025-03-01', '2025-11-30', player_id)

# 2. データの加工
df_hits = df.dropna(subset=['launch_speed', 'pitch_type']).copy()
major_pitches = df_hits['pitch_type'].value_counts().nlargest(5).index
df_major = df_hits[df_hits['pitch_type'].isin(major_pitches)].copy()

# 3. 描画設定
plt.figure(figsize=(12, 7))
sns.set_style("darkgrid")

# 球種ごとのバイオリン図
sns.violinplot(data=df_major, x='pitch_type', y='launch_speed', 
               palette="viridis", inner="quartile", hue='pitch_type', legend=False)

# 本塁打（HR）をプロット（labelを指定）
df_hr = df_major[df_major['events'] == 'home_run']
sns.stripplot(data=df_hr, x='pitch_type', y='launch_speed', 
              color='red', size=5, jitter=0.2, zorder=10, label='Home Run')

# 4. 仕上げの装飾
plt.title('2025 Shohei Ohtani: Exit Velocity Distribution by Pitch Type', fontsize=16, fontweight='bold')
plt.xlabel('Pitch Type (Statcast Code)', fontsize=12)
plt.ylabel('Exit Velocity (mph)', fontsize=12)

# 凡例を1つだけ表示する処理
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc='lower center', ncol=1)

# 画像を保存
plt.savefig('ohtani_2025_pitch_type_analysis.png', dpi=300, bbox_inches='tight')

plt.show()