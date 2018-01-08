#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# ******
# ネットワークの辺データ(csv形式)を読み込みネットワークを構築
# 概観の表示、次数分布の表示を行う
# ******

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# 読み取りDataFrame形式で返す
readData = pd.read_csv("JPAir.csv",header=None)

# (DataFrame形式).value で縦横のラベルを剥がしてndarray形式に変更
adarrayData = readData.values

# (ndarray形式).tolist() でndarrayをリスト形式へ変換
listData = adarrayData.tolist()

# 読み込んだ辺リストデータでネットワークを構成する
G = nx.Graph()
G.add_edges_from(listData)

## 次の2つはいずれかを1つだけを実行させてください
# ネットワークの外観を表示
#nx.draw(G)

# 次数分布を出力
plt.xscale("log")
plt.yscale("log")
plt.plot(nx.degree_histogram(G),".")