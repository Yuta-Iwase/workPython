#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# ***手動でネットワーク作り、描写・保存する***

import networkx as nx
import matplotlib.pyplot as plt

# 空のネットワークを生成
G = nx.Graph()
# 頂点を手動で追加
NList=[1,2,3,4,5,6,7,8,9,10]
G.add_nodes_from(NList)
# 辺を手動で追加
EList= [(1,2),(1,8),(2,3),(2,4),(4,5),(6,7),(6,8),(8,9),(8,10)]
G.add_edges_from(EList)

# グラフィックをコンソールに出力
nx.draw(G)

# コンソールに出た図をファイルに保存
plt.savefig("testNetwork.png")
plt.savefig("testNetwork.eps")
plt.close()