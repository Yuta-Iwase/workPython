# -*- coding: utf-8 -*-

### ここに入出力情報を打つ
inputPath = ["test.csv"]
outputName = "kk_vs_w"
plotRangeX = [] #自動範囲の場合[]にする
plotRangeY = [] #自動範囲の場合[]にする
withLines = False
lineColors = ["blue","black","red"]
dottedLine = [False,False,False]
withPoints = True
pointColors = ["blue","black","red"]
pointSizes = [5,5,5]
pointDescription = ["o", "^", "^"] #マーカーの形、"o"で丸、"^"で三角、詳しくはhttps://pythondatascience.plavox.info/matplotlib/%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC%E3%81%AE%E5%90%8D%E5%89%8D
withAnnotate = True
accumulationMode = 0 #0で累積なし、1で累積、2で逆累積
logscaleX = True
logscaleY = True
title = r"$kk$ vs $w$"
xLabel = r"$k_i k_j$"
yLabel = r"$w_{ij}$"
withLegend = True
legendLabel = [r"${\alpha}=1.5$"] #凡例の名前、空欄ならファイル名がそのままに名前になる
legendPosition = "upper left" #凡例の位置:lower,center,upperで縦方向、left,center,rightで横方向の位置を設定できる、空白で自動設定
### 追加情報
function_List = ["y=(x**1.5)/800"] ##関数を定義。y=(xの関数)の形式で書く。例:"y=x**2"
function_LineColors = ["red"]
function_DottedLine = [True]
function_LegendLabel = [r"$y=x^{1.5}/800$"]
#############################




### ここからプログラム内容

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# データ読み取り
xList = []
yList = []
annotateList = []
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
    # annotate情報を確認、格納
    an = []
    if len(adarrayData[0])>2:
        adarrayAnnotate = adarrayData[:,2]
        an = adarrayAnnotate.tolist()
    annotateList.append(an)


# 累積分布の処理
if accumulationMode==1:
    for i in range(len(yList)):
        for j in range(len(yList[i])-1):
            yList[i][j+1] += yList[i][j]
if accumulationMode==2:
    for i in range(len(yList)):
        length = len(yList[i])
        for j in range(len(yList[i])-1):
            inv_j = length-1-j
            yList[i][inv_j-1] += yList[i][inv_j]

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
        m = "o"
        if len(pointDescription)>0:
            m = pointDescription[i]
        plt.plot(xList[i],yList[i],linestyle=style,linewidth=width,color=lineColors[i],marker=m,fillstyle="none",markersize=pointSizes[i],markeredgecolor=pointColors[i],label=legend)
    else:
        plt.plot(xList[i],yList[i],linestyle=style,linewidth=width,color=lineColors[i],label=legend)
    if (len(annotateList[i])>0 and withAnnotate):
        currentAnnotate = annotateList[i]
        currentX = xList[i]
        currentY = yList[i]
        for p in range(len(currentAnnotate)):
            plt.annotate(currentAnnotate[p], (currentX[p], currentY[p]), color=pointColors[i])

if len(function_List)>0:
    xLim = plt.xlim()
    beforeYLim = plt.ylim()
    x = np.linspace(xLim[0],xLim[1],100)
    for i in range(len(function_List)):
        exec(function_List[i]) ##ここでを計算
        if len(function_LegendLabel)>=len(function_List):
            legend = function_LegendLabel[i]
        else:
            legend = function_List[i]
        if len(function_DottedLine)>=len(function_List):
            if function_DottedLine[i]:
                style = "--"
            else:
                style = "-"
        plt.plot(x, y, linestyle=style, linewidth=2, color=function_LineColors[i], markersize=0, label=legend)
    plt.ylim(beforeYLim)
    del x
    del y

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
