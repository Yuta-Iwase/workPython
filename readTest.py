#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:18:57 2017

@author: owner
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# 読み取りDataFrame形式で返す
readData = pd.read_csv("BA_model.csv",header=None)

# (DataFrame形式).value で縦横のラベルを剥がしてndarray形式に変更
adarrayData = readData.values

# (ndarray形式).tolist() でndarrayをリスト形式へ変換
listData = adarrayData.tolist()

# 読み込んだ辺リストデータでネットワークを構成する
G = nx.Graph()
G.add_edges_from(listData)
nx.draw(G)
readData.to_csv("clone_csv.csv")

# 有向グラフの定義
Gd = nx.DiGraph()