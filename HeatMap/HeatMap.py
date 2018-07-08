# -*- coding: utf-8 -*-

### ここに入出力情報を打つ
inputPath = "aaa.csv"
outputName = "node_bc"
plotRangeX = [0,0.6]
plotRangeY = [0,0.4]
cmap = "" #hotで白→赤→黒、空文字列でhotに自動設定
#############################

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# 読み取りDataFrame形式で返す
readData_df = pd.read_csv(inputPath,header=None)
# (DataFrame形式).value で縦横のラベルを剥がしてndarray形式に変換
readData_nd = readData_df.values
# (ndarray形式).tolist() でndarrayをリスト形式へ変換
readData_ls = readData_nd.tolist()
# 縦軸反転
readData_ls = readData_ls[::-1]

# 座標データラベルを定義
# x軸
xValues = []
if len(plotRangeX)>0:
    currentXValue = plotRangeX[0]
    delta_X = (plotRangeX[1]-plotRangeX[0])/(len(readData_ls[0])-1)
    for i in range(len(readData_ls[0])):
        currentXValue = i*delta_X
        xValues.append(currentXValue)
else:
    for i in range(len(readData_ls[0])):
        xValues.append(i)
# y軸
yValues = []
if len(plotRangeY)>0:
    currentYValue = plotRangeY[1]
    delta_Y = (plotRangeY[1]-plotRangeY[0])/(len(readData_ls)-1)
    for i in range(len(readData_ls)):
        currentYValue = (len(readData_ls)-i-1)*delta_Y
        yValues.append(currentYValue)
else:
    currentYValue = len(readData_ls)-1
    for i in range(len(readData_ls)):
        yValues.append(currentYValue)
        currentYValue -= 1

# 座標データをラベルとして追加して再び、list形式->DataFrame形式、に変更
enhancedList_df = pd.DataFrame(readData_ls, index=yValues, columns=xValues)

# cmapのデフォルト設定
if len(cmap)==0:
    cmap="hot"

# ヒートマッププロット
sns.heatmap(enhancedList_df,cmap=cmap)

# 書き込み
if len(outputName)<=0:
    outputName = inputPath
if (not os.path.exists("output")):
    os.makedirs("output")

plt.savefig("output/" + outputName + ".png")
plt.savefig("output/" + outputName + ".eps", transparent=True)
plt.savefig("output/" + outputName + ".pdf", transparent=True)
# plt.savefig("a.png")
