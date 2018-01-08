#!/usr/bin/env python2
# -*- coding: utf-8 -*-

inputPath = "list_degreeVSstrength.csv"
logscale = True
bin_n = 50
title = "degree VS strength"
outputName = "degreeVSstrength"

import matplotlib.pyplot as plt
import pandas as pd
from compiler.ast import flatten
import numpy as np

# 読み取りDataFrame形式で返す
readData = pd.read_csv(inputPath,header=None)
# (DataFrame形式).value で縦横のラベルを剥がしてndarray形式に変更
adarrayData = readData.values
# x,yのデータへ分離
adarrayDataX = adarrayData[:,0]
adarrayDataY = adarrayData[:,1]
# (ndarray形式).tolist() でndarrayをリスト形式へ変換
x = adarrayDataX.tolist()
y = adarrayDataY.tolist()



plt.title(title)
plt.xlabel("degree")
plt.ylabel("strength")
plt.xscale("log")
plt.yscale("log")
plt.plot(x,y,linewidth=0,marker="o",fillstyle="none",markersize="10",markeredgecolor="blue")

plt.savefig("output/" + outputName + ".png")
plt.savefig("output/" + outputName + ".eps")
