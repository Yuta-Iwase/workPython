#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# ******
# バルバシ・アルバートモデルを構築
# 他のソフトでも読み込めるように辺データ(csv形式)を出力
# また、概観や次数分布を出力
# ******

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# 変数定義
N = 1000
M0 = 1
M = (N-M0)*M0

# 変数をもとにバルバシ・アルバートモデルを構築
#G = nx.barabasi_albert_graph(N,M0)
G = nx.watts_strogatz_graph(100,4,0)
# csvでedgeListを出力
df = pd.DataFrame(nx.edges(G))
df.to_csv("WS.csv",header=False,index=False)

# グラフィックをコンソールに出力
#nx.draw(G)

# コンソールに出た図をファイルに保存
#plt.savefig("BA_model.png")
#plt.savefig("BA_model.eps")
#plt.close()

# 次数分布を出力
#plt.xscale("log")
#plt.yscale("log")
#plt.plot(nx.degree_histogram(G), ".")