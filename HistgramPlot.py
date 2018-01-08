#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 10:48:25 2017

@author: owner
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# 読み取りDataFrame形式で返す
readData = pd.read_csv("list.csv",header=None)

# (DataFrame形式).value で縦横のラベルを剥がしてndarray形式に変更
adarrayData = readData.values

# (ndarray形式).tolist() でndarrayをリスト形式へ変換
listData = adarrayData.tolist()

plt.hist(listData)
