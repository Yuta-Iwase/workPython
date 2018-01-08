#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# ******
# エルデシュ・レイニー(ER)モデルの構築を行う
# 連結成分の解析を行う
# ERモデルはpが1/N付近を境に最大連結成分サイズが相転移を起こす
# 今回のプログラムではその相転移を確認する
# ******


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# ネットワークの設定
n = 500
# 解析の設定
imax = 20
jmax = 2
minRange = (1.0/n)/10
maxRange = 1.0
## 解析開始
# 変数初期化
xList = []
yList = []
width = (maxRange-minRange)/imax
p = minRange
for i in range(imax):
    sumLCCSize=0
    for j in range(jmax):
        # 頂点数n,確率pのエルデシュ・レイニーモデルを構築
        G = nx.erdos_renyi_graph(n,p)
        # 連結成分のデータ構造を取得(generator形式で返される)
        cc = nx.connected_components(G)
        # ccをサイズの大きい順にソート(ついでに変数の型をlistにできる)
        l = sorted(cc)
        # 最大連結成分(LCC)を合計値に加算する
        sumLCCSize = sumLCCSize+len(l[0])
    # 横軸の座標を登録
    xList.append(p)
    # 縦軸の座標を登録
    yList.append(sumLCCSize/jmax)
    # 次のpへ更新
    p = p+width

# 結果表示
plt.plot(xList,yList,".")