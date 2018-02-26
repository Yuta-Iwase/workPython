#!/usr/bin/env python2
# -*- coding: utf-8 -*-

### ここに入出力情報を打つ
inputPath = ["bc.csv"]
outputName = "bc_dist"
bin_n = 50 #(最大値-1)にすると良い
plotRangeX = [] #自動範囲の場合[]にする
plotRangeY = [] #自動範囲の場合[]にする
withLines = True
lineColors = ["blue"]
dottedLine = [False]
withPoints = True
pointColors = ["blue"]
pointSizes = [3]
logscaleX = True
maxDigit = 7
logscaleY = True
title = ""
xLabel = r"bc"
yLabel = r"$p($bc$)$"
withLegend = False
legendPosition = "center right" #凡例の位置:lower,center,upperで縦方向、left,center,rightで横方向の位置を設定できる、空白で自動設定#
#############################

### ここからプログラム内容

import matplotlib.pyplot as plt
import pandas as pd
from compiler.ast import flatten
import numpy as np
import os
import csv

# データ読み取り
xList = []
yList = []
for i in range(len(inputPath)):
    # 読み取りDataFrame形式で返す
    readData = pd.read_csv(inputPath[i],header=None)
    # (DataFrame形式).value で縦横のラベルを剥がしてndarray形式に変更
    adarrayData = readData.values
    # (ndarray形式).tolist() でndarrayをリスト形式へ変換
    listData = adarrayData.tolist()
    # リスト形式のデータを1次元化
    listData = flatten(listData)
    # hist関数を利用して度数数え上げ,点データをx,yへ格納
    if logscaleX:
        y, x, patches = plt.hist(listData,bins=np.logspace(0, maxDigit-1, bin_n))
    else:
        y, x, patches = plt.hist(listData,bins=bin_n)
    x = x[0:len(x)-1]
    # リストへ格納
    xList.append(x)
    yList.append(y)
    # 描写リセット
    plt.figure()

    # ファイルオープン
    f = open('output.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')

    # データをリストに保持
    csvlist = []
    csvlist.append(x)
    csvlist.append(y)
    m = np.array(csvlist)
    m = m.T
    csvlist2 = m.tolist()

    # 出力
    writer.writerows(csvlist2)

    # ファイルクローズ
    f.close()


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
