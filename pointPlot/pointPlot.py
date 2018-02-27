#!/usr/bin/env python2
# -*- coding: utf-8 -*-

### ここに入出力情報を打つ
inputPath = ["alpha=-2_0.csv","alpha=-0_4.csv","alpha=2_0.csv"]
outputName = "node_bc"
plotRangeX = [] #自動範囲の場合[]にする
plotRangeY = [] #自動範囲の場合[]にする
withLines = True
lineColors = ["blue","black","red"]
dottedLine = [False,False,False]
withPoints = True
pointColors = ["blue","black","red"]
pointSizes = [5,5,5]
accumulationMode = 2 #0で累積なし、1で累積、2で逆累積
logscaleX = True
logscaleY = True
title = "node betweenneess"
xLabel = r"node bc"
yLabel = r"$p($node bc$)$"
withLegend = True
legendLabel = []
legendPosition = "upper right" #凡例の位置:lower,center,upperで縦方向、left,center,rightで横方向の位置を設定できる、空白で自動設定#
#############################




### ここからプログラム内容

import matplotlib.pyplot as plt
import pandas as pd
import os

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

# 累積分布の処理
if accumulationMode==1:
    for i in range(len(yList)):
        for j in range(len(yList[i])-1):
            yList[i][j+1] += yList[i][j]
if accumulationMode==2:
    for i in range(len(yList)):
        yList[i][0] = sum(yList[i]) - yList[i][0]
        for j in range(len(yList[i])-1):
            yList[i][j+1] = yList[i][j] - yList[i][j+1]

# プロット
width = 0
if len(plotRangeX)>0:
    plt.xlim(plotRangeX)
if len(plotRangeY)>0:
    plt.ylim(plotRangeY)
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
    if len(legendLabel)==len(inputPath):
        legend = legendLabel[i]
    else:
        legend = inputPath[i][:inputPath[i].find(".")]
    if len(dottedLine)>=len(inputPath) and withLines:
        if dottedLine[i]:
            style = "--"
        else:
            style = "-"
    else:
        style = ""
    if withPoints:
        plt.plot(xList[i],yList[i],linestyle=style,linewidth=width,color=lineColors[i],marker="o",fillstyle="none",markersize=pointSizes[i],markeredgecolor=pointColors[i],label=legend)
    else:
        plt.plot(xList[i],yList[i],linestyle=style,linewidth=width,color=lineColors[i],label=legend)

if withLegend:
    if len(legendPosition)>0:
        plt.legend(loc = legendPosition)
    else:
        plt.legend()

# 書き込み
if len(outputName)<=0:
    outputName = inputPath[0][:inputPath[0].find(".csv")]
if (not os.path.exists("output")):
    os.makedirs("output")
plt.savefig("output/" + outputName + ".png")
plt.savefig("output/" + outputName + ".eps", transparent=True)
plt.savefig("output/" + outputName + ".pdf", transparent=True)
