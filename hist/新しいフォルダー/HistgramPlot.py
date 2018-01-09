#!/usr/bin/env python2
# -*- coding: utf-8 -*-

inputPath = "list_weight.csv"
logscale = True
bin_n = 50
title = "weight dist"
outputName = "weight_dist"

import matplotlib.pyplot as plt
import pandas as pd
from compiler.ast import flatten
import numpy as np
import os

# 読み取りDataFrame形式で返す
readData = pd.read_csv(inputPath,header=None)
# (DataFrame形式).value で縦横のラベルを剥がしてndarray形式に変更
adarrayData = readData.values
# (ndarray形式).tolist() でndarrayをリスト形式へ変換
listData = adarrayData.tolist()
# リスト形式のデータを1次元化
listData = flatten(listData)

# hist関数を利用して度数数え上げ,点データをx,yへ格納
if logscale:
    y, x, patches = plt.hist(listData,bins=np.logspace(1, 4, bin_n))
else:
    y, x, patches = plt.hist(listData,bins=bin_n)
x = x[0:len(x)]

# 描写リセット
plt.figure()

if logscale:
    plt.xscale("log")
    plt.yscale("log")
plt.title(title)
plt.plot(x[0:len(x)-1],y,color="black",marker="o",fillstyle="none",markersize="10",markeredgecolor="blue")

os.mkdir("output")
plt.savefig("output/" + outputName + ".png")
plt.savefig("output/" + outputName + ".eps")