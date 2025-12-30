# 2025 Shohei Ohtani Pitch Type Analysis

このプロジェクトは、MLBのStatcastデータを使用して、2025年シーズンの大谷翔平選手の打撃パフォーマンスを可視化します。特定の球種ごとの打球速度（Exit Velocity）の分布と、本塁打の発生ポイントを分析します。

## 概要
大谷翔平選手が対峙した球種のうち、投球数が多い上位5種類を抽出し、以下の2点を1つのグラフに描画します。
1. **バイオリン図**: 球種ごとの打球速度の密度と分布。
2. **ストリッププロット（赤点）**: 本塁打（Home Run）を放った際の打球速度。

## 必要要件
実行には Python 3.x と以下のライブラリが必要です。

* `pandas`
* `seaborn`
* `matplotlib`
* `pybaseball`

### インストール方法
```bash
pip install pandas seaborn matplotlib pybaseball
