#!/usr/bin/env python2
# -*- coding: utf-8 -*-

### ここに入出力情報を打つ
inputPath = ["not_shuffle.csv","shuffle.csv"]
outputName = ""
withLines = True
lineColor = "black"
withPoints = True
pointColors = ["red","blue"]
logscaleX = False
logscaleY = False
title = "biased RW"
xLabel = r"$\alpha$"
yLabel = "HS frac"
#############################




### ここからプログラム内容

import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# データ読み取り
xList = []
yList = []
for i in range(len(inputPath)):
    # 読み取りDataFrame形式で返す
    readData = pd.read_csv(inputPath[i],header=None)
    # (DataFrame形式).value で縦横のラベルを剥がしてndarray形式に変更
    adarrayData = readData.values
    # x,yのデータへ分離
    adarrayDataX = adarrayData[:,0]
    adarrayDataY = adarrayData[:,1]
    # (ndarray形式).tolist() でndarrayをリスト形式へ変換
    x = adarrayDataX.tolist()
    xList.append(x)
    y = adarrayDataY.tolist()
    yList.append(y)


# プロット
width = 0
if withLines:
    width = 2
if logscaleX:
    plt.xscale("log")
if logscaleY:
    plt.yscale("log")
plt.title(title)
plt.xlabel(xLabel)
plt.ylabel(yLabel)

for i in range(len(inputPath)):
    legend = inputPath[i][:inputPath[i].find(".csv")]
    if withPoints:
        plt.plot(xList[i],yList[i],linewidth=width,color=lineColor,marker="o",fillstyle="none",markersize="10",markeredgecolor=pointColors[i],label=legend)
    else:
        plt.plot(xList[i],yList[i],linewidth=width,color=lineColor,label=legend)
plt.legend()

# 書き込み
if len(outputName)<=0:
    outputName = inputPath[0][:inputPath[0].find(".csv")]
if (not os.path.exists("output")):
    os.makedirs("output")
plt.savefig("output/" + outputName + ".png")
plt.savefig("output/" + outputName + ".eps", transparent=True)
plt.savefig("output/" + outputName + ".pdf", transparent=True)
